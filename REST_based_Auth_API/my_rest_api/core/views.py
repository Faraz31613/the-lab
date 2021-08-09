from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status, viewsets

from .models import Comment, Friend, Like, Message, Notification, Post, Request
from .serializers import (
    CommentSerializer,
    FriendsSerializer,
    LikeSerializer,
    NotificationSerializer,
    UserSerializer,
    PostSerializer,
    RequestSerializer,
    MessageSerializer,
    ChangeRequestStatusSerializer,
    MyTokenObtainPairSerializer,
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello Faraz!"}
        return Response(content)


# API for register User
class RegisterUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.serializer_class(user).data)


# API for getting all the users
class GetUsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


# API for making post on Facebook replica and getting the posts of the user who is signed in
class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


# API for commenting on a post or replying to a comment
class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()

    # returning the comments
    def get_queryset(self):
        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        # query with refernce to a specific comment or post
        query = dict(comment=comment_id) if comment_id else dict(post=post_id)
        return self.queryset.filter(**query)

    # method for commenting
    def create(self, request, *args, **kwargs):

        # user object who is signed in
        signed_in_user = self.request.user

        # passed data
        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        # getting the parent post where comment is being made
        parent_post = get_object_or_404(Post, pk=post_id)

        # getting user_id whose post it was where comment is being made
        post_or_comment_author = parent_post.user

        # if comment_id was passed, it means it is a reply to comment or comment on a comment
        if comment_id:
            parent_comment = get_object_or_404(Comment, pk=comment_id)
            post_or_comment_author = parent_comment.user
            notification_text = (
                f"{signed_in_user.username} has replied to a commented on your post"
            )
        # if comment_id is null, it means is a comment on a post
        else:
            notification_text = f"{signed_in_user.username} has commented on your post"

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        # send notification to the author of the post that someone has commented on yout post
        Notification.objects.create(
            user=post_or_comment_author,
            notification=notification_text,
            user_by=signed_in_user,
            post=Post(post_id),
            comment=Comment(comment_id) if comment_id else None,
            notification_source_type=Notification.NotificationType.COMMENT,
        )
        comment = serializer.save()
        return Response(self.serializer_class(comment).data)


# API for sending or seeing the friend request that a user have received
class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    # method for seeing the friend requests that someone has sent to signed in user
    def get_queryset(self):
        signed_in_user = self.request.user.id

        # requestee is the signed in user in Request model
        return Request.objects.filter(
            requestee=signed_in_user, status=Request.Status.PENDING
        )

    # method for sending a friend request
    def create(self, request, *args, **kwargs):
        signed_in_user_id = self.request.user.id
        signed_in_user = self.request.user

        # passed data
        requestee_id = self.request.data["requestee"]
        requestor_id = self.request.data["requestor"]  # signed_in_user_id

        # requestee is the signed in user in Request model
        # signed in  user cannot send a request to himself
        # will raise an exception
        if signed_in_user_id == requestee_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # request_exists_or_not
        # it will also handle a case if the requestor and requestee already are friends, then their request will exists
        if Request.objects.filter(
            requestor_id=signed_in_user_id
        ) | Request.objects.filter(requestee_id=requestee_id):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=self.request.data)

        serializer.is_valid(raise_exception=True)

        # send notification to a user whom the signed in user has sent request
        Notification.objects.create(
            user=User(requestee_id),
            notification=f"{signed_in_user.username} has sent you a friend request",
            user_by=signed_in_user,
            notification_source_type=Notification.NotificationType.REQUEST,
        )

        request = serializer.save()
        return Response(
            self.serializer_class(request).data, status=status.HTTP_201_CREATED
        )


# API for accepting/rejecting the friend request
class ChangeStatusView(viewsets.ModelViewSet):
    serializer_class = ChangeRequestStatusSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    # update the status of request if accepted is passed
    # handles Accepted status
    # for reject status, call delete/destroy method
    def update(self, request, *args, **kwargs):
        signed_in_user_id = self.request.user.id
        signed_in_user = self.request.user

        # passed data
        request_id = request.data["id"]
        request_status = self.request.data["status"]

        # request object
        friend_request = get_object_or_404(Request, pk=request_id)
        requestee_id = friend_request.requestee_id  # sign_in_user_id
        requestor_id = friend_request.requestor_id

        # if signed in user accepts a request and request belongs to the sign in user
        if (
            request_status == Request.Status.ACCEPTED
            and requestee_id == signed_in_user_id
        ):

            # updates the request status to accepted from pending
            # as the requsts with pending status are shown to the sign in user in get_queryset of request API
            self.queryset.filter(pk=request_id).update(status=request_status)

            # send notification to the newly-made friend of the signed in user whose request is accepted
            Notification.objects.create(
                user=User(requestor_id),
                notification=f"{signed_in_user.username} has accepted your friend request",
                user_by=signed_in_user,
                notification_source_type=Notification.NotificationType.REQUEST,
            )

            # saves signed in user as friend of the the other user whose request is accepted
            Friend.objects.create(
                user=User(requestor_id), friend=signed_in_user, request=friend_request
            )

            data = self.serializer_class(Request.objects.get(pk=request_id))
            return Response(data.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # deletes the friend request from database as signed in user rejects a request
    # 1) requestor can use this method to cancel the request that is pending
    # 2) requestee can use this method to reject the request sent to him
    def destroy(self, request, *args, **kwargs):
        signed_in_user = request.user.id

        # passed data
        request_id = request.data["id"]
        request_status = self.request.data["status"]

        # request object
        request = get_object_or_404(Request, pk=request_id)
        requestee_id = request.requestee_id  # sign_in_user_id
        requestor_id = request.requestor_id

        # early return
        if not (
            request_status == Request.Status.REJECTED
            and requestor_id == signed_in_user
            or requestee_id == signed_in_user
        ):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # requestor cancels request or requestee rejects request
        # delete notification of friend request from database that was send to requestee
        Notification.objects.filter(
            user=requestee_id,
            user_by=requestor_id,
            notification_source_type=Notification.NotificationType.REQUEST,
        ).delete()

        # delete the request from database
        self.queryset.filter(pk=request_id).delete()

        return Response(status=status.HTTP_200_OK)


# API for getting the friend list of user  and to unfriend a friend user
class FriendsView(viewsets.ModelViewSet):
    serializer_class = FriendsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Friend.objects.all()

    # get a friend list of the signed in user
    def get_queryset(self):
        signed_in_user = self.request.user
        friends_list = self.queryset.filter(user=signed_in_user) | self.queryset.filter(
            friend=signed_in_user
        )
        for friend in friends_list:
            if friend.user.id is not signed_in_user.id:
                friend.friend = friend.user
                friend.user = signed_in_user

        return friends_list

    # unfriend a friend user
    def destroy(self, request, *args, **kwargs):
        signed_in_user = self.request.user

        # passed data
        friend_id = self.request.data["friend"]

        # friend object of the friend to delete
        try:
            friend = Friend.objects.get(user=signed_in_user, friend=friend_id)
        except Friend.DoesNotExist:
            friend = get_object_or_404(Friend, user=friend_id, friend=signed_in_user)

        # request object from friend object
        request = friend.request
        requestor_id = request.requestor_id
        requestee_id = request.requestee_id

        # delete friend record
        friends = self.queryset.filter(
            user=requestor_id, friend=requestee_id
        ) | self.queryset.filter(user=requestee_id, friend=requestor_id)
        friends.delete()

        # delete the request by which they made friends with each other
        Request.objects.filter(pk=request.id).delete()

        # delete two notifications of friend request sent and accepted
        # delete notification of friend request sent from database that was send to requestee by requestor
        Notification.objects.filter(
            user=requestee_id,
            user_by=requestor_id,
            notification_source_type=Notification.NotificationType.REQUEST,
        ).delete()
        # delete notification of friend request accepted from database that was send to requestor by requestee
        Notification.objects.filter(
            user=requestor_id,
            user_by=requestee_id,
            notification_source_type=Notification.NotificationType.REQUEST,
        ).delete()

        return Response(status=status.HTTP_200_OK)


# API for getting the list of notification refernced to a user
class ShowNotifications(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user.id
        return self.queryset.filter(user=signed_in_user)


# API for like functionality on facebook replica
class LikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()

    # method to get the list of likes to a post or comment that someone has liked
    def get_queryset(self):

        # passed data
        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        # checking comment_id because it can be null
        query = dict(comment=comment_id) if comment_id else dict(post=post_id)
        return self.queryset.filter(**query)

    # method to like a comment or post
    def create(self, request, *args, **kwargs):
        signed_in_user = self.request.user

        # passed data
        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        # parent post that is liked
        parent_post = get_object_or_404(Post, pk=post_id)

        # post_author(user who made the post) from post object,
        post_or_comment_author = parent_post.user

        # if comment_id is not null, it means a comment is liked
        if comment_id:
            # comment which is liked
            comment = get_object_or_404(Comment, pk=comment_id)

            # comment author, who made the comment which is liked
            post_or_comment_author = comment.user
            notification_text = f"{signed_in_user.username} has liked your comment"

        # id comment_id is null, it means a post is liked
        else:
            notification_text = f"{signed_in_user.username} has liked your post"

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        # send notification to the post/comment author whose post/comment is liked
        # if signed in user likes his own comment or post
        # notification not needed then
        # early return
        if signed_in_user.id == post_or_comment_author.id:
            like = serializer.save()
            return Response(self.serializer_class(like).data)
        Notification.objects.create(
            user=post_or_comment_author,
            notification=notification_text,
            user_by=signed_in_user,
            post=parent_post,
            comment=comment,
            notification_source_type=Notification.NotificationType.LIKE,
        )
        like = serializer.save()
        return Response(self.serializer_class(like).data)


# API for message communication between users
class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()

    # method to get a list of chat messages between two users
    def get_queryset(self):
        signed_in_user = self.request.user.id

        return self.queryset.filter(sender_id=signed_in_user) | self.queryset.filter(
            receiver_id=signed_in_user
        )

    # method to send a message to the other user
    def create(self, request, *args, **kwargs):
        signed_in_user = self.request.user

        # passed data
        receiver = self.request.data["receiver"]

        serializer = self.serializer_class(data=self.request.data)

        serializer.is_valid(raise_exception=True)

        # send a notification of message to the receiver from sender
        Notification.objects.create(
            user=User(receiver),
            notification=f"{signed_in_user.username} has sent you a message",
            user_by=signed_in_user,
            notification_source_type=Notification.NotificationType.MESSAGE,
        )
        message = serializer.save()

        return Response(
            self.serializer_class(message).data, status=status.HTTP_201_CREATED
        )
