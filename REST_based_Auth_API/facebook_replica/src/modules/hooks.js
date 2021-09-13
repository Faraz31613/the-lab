import { useDispatch } from "react-redux";

import * as postActions from "modules/post/action";
import * as likeActions from "modules/like/action";
import * as commentActions from "modules/comment/action";
import * as notificationActions from "modules/notification/action";
import * as signInActions from "modules/authentication/action";
import * as signUpActions from "modules/authentication/action";

export const useGetPosts = (authToken) => {
  const dispatch = useDispatch();
  return () => {
    dispatch(postActions.getPosts(authToken));
  };
};
export const useHandlePostLike = (isLiked, postId, userId, authToken) => {
  const dispatch = useDispatch();
  if (isLiked === false) {
    const createLikeCred = {
      likeCred: {
        post: postId,
        user: userId,
        comment: null,
        is_like: true,
        like_type: "P",
      },
      authToken: authToken,
    };
    return () => {
      dispatch(likeActions.like(createLikeCred));
    };
  } else {
    const deleteLikeCred = {
      post: postId,
      authToken,
    };
    return () => {
      dispatch(likeActions.unlike(deleteLikeCred));
    };
  }
};

export const useHandlePostComment = (
  postId,
  userId,
  comment,
  authToken,
  setComment
) => {
  const dispatch = useDispatch();
  const commentCreds = {
    comment: {
      user: userId,
      comment_text: comment,
      comment: null,
      post: postId,
    },
    authToken: authToken,
  };
  if (comment === "") {
    return;
  }
  return () => {
    dispatch(commentActions.addComment(commentCreds));
    setComment("");
  };
};

export const useHandleShowComments = (
  postId,
  authToken,
  showCommentFlag,
  setShowCommentFlag
) => {
  const dispatch = useDispatch();
  const commentedPostCreds = {
    post: postId,
    authToken: authToken,
  };
  return () => {
    dispatch(commentActions.getComments(commentedPostCreds));
    setShowCommentFlag(!showCommentFlag);
  };
};

export const useGetNotification = (authToken) => {
  const  dispatch = useDispatch()
  return () => {
    dispatch(notificationActions.getNotification(authToken));
  }
}
export const useMarkAsRead = () => {
  const dispatch = useDispatch();
  return (authToken, notificationId) => {
    const notificationCred = {
      authToken,
      id: notificationId,
    };
    dispatch(notificationActions.markAsRead(notificationCred));
  };
};

export const useSignIn = (username, password) => {
  const dispatch = useDispatch();
  return () => {
    dispatch(signInActions.signIn({ username, password }));
  };
};

export const useSignUp = (username, firstName, lastName, email, password) => {
  const dispatch = useDispatch();
  return () => {
    dispatch(
      signUpActions.signUp({
        username,
        email,
        password,
        first_name: firstName,
        last_name: lastName,
      })
    );
  };
};
