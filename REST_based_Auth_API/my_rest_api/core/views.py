from django.db.models.query import QuerySet
from django.http.request import QueryDict
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
    HomeSerializer,
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


class RegisterUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        print(self.request.data)
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.serializer_class(user).data)


class GetUsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user
        return self.queryset.filter(user=signed_in_user)


class HomeView(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user
        friends = Friend.objects.filter(user=signed_in_user) | Friend.objects.filter(
            friend=signed_in_user
        )

        home_posts = self.queryset.filter(user=signed_in_user)

        for friend in friends:
            if friend.user.id is not signed_in_user.id:
                home_posts = QuerySet.union(
                    home_posts, self.queryset.filter(user=friend.user))
            else:
                home_posts = QuerySet.union(
                    home_posts, self.queryset.filter(user=friend.friend))

        return home_posts.order_by("-id")


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()

    def get_queryset(self):
        post_id = self.request.GET.get("post")
        comment_id = None
        if(self.request.GET.get("comment") != "null"):
            comment_id = self.request.GET.get("comment")

        query = dict(comment=comment_id) if comment_id else dict(post=post_id)
        return self.queryset.filter(**query)

    def create(self, request, *args, **kwargs):

        signed_in_user = self.request.user

        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        parent_post = get_object_or_404(Post, pk=post_id)

        post_or_comment_author = parent_post.user

        if comment_id:
            parent_comment = get_object_or_404(Comment, pk=comment_id)
            post_or_comment_author = parent_comment.user
            notification_text = (
                f"{signed_in_user.username} has replied to a commented on your post"
            )
        else:
            notification_text = f"{signed_in_user.username} has commented on your post"

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        if post_or_comment_author != signed_in_user:
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


class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user.id

        return Request.objects.filter(
            requestee=signed_in_user, status=Request.Status.PENDING
        )

    def create(self, request, *args, **kwargs):
        signed_in_user_id = self.request.user.id
        signed_in_user = self.request.user

        requestee_id = self.request.data["requestee"]

        if signed_in_user_id == requestee_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if Request.objects.filter(
            requestor_id=signed_in_user_id
        ) & Request.objects.filter(requestee_id=requestee_id):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=self.request.data)

        serializer.is_valid(raise_exception=True)

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


class ChangeStatusView(viewsets.ModelViewSet):
    serializer_class = ChangeRequestStatusSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    def update(self, request, *args, **kwargs):
        signed_in_user_id = self.request.user.id
        signed_in_user = self.request.user

        request_id = request.data["id"]
        request_status = self.request.data["status"]

        friend_request = get_object_or_404(Request, pk=request_id)
        requestee_id = friend_request.requestee_id
        requestor_id = friend_request.requestor_id

        if (
            request_status == Request.Status.ACCEPTED
            and requestee_id == signed_in_user_id
        ):

            self.queryset.filter(pk=request_id).update(status=request_status)

            Notification.objects.create(
                user=User(requestor_id),
                notification=f"{signed_in_user.username} has accepted your friend request",
                user_by=signed_in_user,
                notification_source_type=Notification.NotificationType.REQUEST,
            )

            Friend.objects.create(
                user=User(requestor_id), friend=signed_in_user, request=friend_request
            )

            data = self.serializer_class(Request.objects.get(pk=request_id))
            return Response(data.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        signed_in_user = request.user.id

        request_id = request.data["id"]
        request_status = self.request.data["status"]

        request = get_object_or_404(Request, pk=request_id)
        requestee_id = request.requestee_id
        requestor_id = request.requestor_id

        if not (
            request_status == Request.Status.REJECTED
            and requestor_id == signed_in_user
            or requestee_id == signed_in_user
        ):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Notification.objects.filter(
            user=requestee_id,
            user_by=requestor_id,
            notification_source_type=Notification.NotificationType.REQUEST,
        ).delete()

        self.queryset.filter(pk=request_id).delete()

        return Response(status=status.HTTP_200_OK)


class FriendsView(viewsets.ModelViewSet):
    serializer_class = FriendsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Friend.objects.all()

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

    def destroy(self, request, *args, **kwargs):
        signed_in_user = self.request.user

        friend_id = self.request.data["friend"]

        try:
            friend = Friend.objects.get(user=signed_in_user, friend=friend_id)
        except Friend.DoesNotExist:
            friend = get_object_or_404(
                Friend, user=friend_id, friend=signed_in_user)

        request = friend.request
        requestor_id = request.requestor_id
        requestee_id = request.requestee_id

        friends = self.queryset.filter(
            user=requestor_id, friend=requestee_id
        ) | self.queryset.filter(user=requestee_id, friend=requestor_id)
        friends.delete()

        Request.objects.filter(pk=request.id).delete()

        Notification.objects.filter(
            user=requestee_id,
            user_by=requestor_id,
            notification_source_type=Notification.NotificationType.REQUEST,
        ).delete()

        Notification.objects.filter(
            user=requestor_id,
            user_by=requestee_id,
            notification_source_type=Notification.NotificationType.REQUEST,
        ).delete()

        return Response(status=status.HTTP_200_OK)


class ShowNotifications(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user.id
        return self.queryset.filter(user=signed_in_user)

    def update(self, request, *args, **kwargs):
        signed_in_user_id = self.request.user.id
        signed_in_user = self.request.user

        notification_id = self.request.data["id"]
        print(notification_id)
        self.queryset.filter(pk=notification_id).update(is_read=True)

        data = self.serializer_class(
            Notification.objects.get(pk=notification_id))
        return Response(data.data, status=status.HTTP_200_OK)


class SignedInUserLikesView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()

    def get_queryset(self):
        signedInUser = self.request.user
        return self.queryset.filter(user=signedInUser, is_like=True)


class LikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()

    def get_queryset(self):
        post_id = self.request.GET.get("post")
        comment_id = None
        if(self.request.GET.get("comment") != "null"):
            comment_id = self.request.GET.get("comment")

        query = dict(comment=comment_id) if comment_id else dict(post=post_id)
        return self.queryset.filter(**query)

    def create(self, request, *args, **kwargs):
        signed_in_user = self.request.user

        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        likeExits = self.queryset.filter(
            comment=comment_id, post=post_id, user=signed_in_user.id)

        if likeExits.exists():
            return Response()

        parent_post = get_object_or_404(Post, pk=post_id)

        post_or_comment_author = parent_post.user

        comment = None
        if comment_id:
            comment = get_object_or_404(Comment, pk=comment_id)

            post_or_comment_author = comment.user
            notification_text = f"{signed_in_user.username} has liked your comment"

        else:
            notification_text = f"{signed_in_user.username} has liked your post"

        serializer = self.serializer_class(data=self.request.data)

        serializer.is_valid(raise_exception=True)

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

    def destroy(self, request, *args, **kwargs):
        signed_in_user = self.request.user.id

        post_id = self.request.GET.get("id")

        like = get_object_or_404(
            Like, post=post_id, user=signed_in_user)

        post_or_comment_author = like.post.user

        self.queryset.get(post=post_id, user=signed_in_user).delete()

        Notification.objects.filter(
            user=post_or_comment_author,
            user_by=signed_in_user,
            notification_source_type=Notification.NotificationType.LIKE,
        ).delete()

        return Response(status=status.HTTP_200_OK)


class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user.id

        return self.queryset.filter(sender_id=signed_in_user) | self.queryset.filter(
            receiver_id=signed_in_user
        )

    def create(self, request, *args, **kwargs):
        signed_in_user = self.request.user

        receiver = self.request.data["receiver"]

        serializer = self.serializer_class(data=self.request.data)

        serializer.is_valid(raise_exception=True)

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
