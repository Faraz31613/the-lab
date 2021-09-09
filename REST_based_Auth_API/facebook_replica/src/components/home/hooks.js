import * as likeActions from "modules/like/action";
import * as commentActions from "modules/comment/action";

export const handlePostLike = (
  dispatch,
  isLiked,
  likeId,
  postId,
  userId,
  authToken
) => {
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
    dispatch(likeActions.like(createLikeCred));
  } else {
    const deleteLikeCred = {
      likeId: likeId,
      authToken: authToken,
    };
    dispatch(likeActions.unlike(deleteLikeCred));
  }
  dispatch(likeActions.getSignedInUserLikes(authToken));
};

export const handlePostComment = (
  e,
  dispatch,
  postId,
  userId,
  comment,
  authToken,
  setComment,
) => {
  if (e.key === "Enter" && comment.trim() !== "") {
    const commentCreds = {
      comment: {
        user: userId,
        comment_text: comment,
        comment: null,
        post: postId,
      },
      authToken: authToken,
    };
    dispatch(commentActions.addComment(commentCreds));
    setComment("");
  }
};

export const handleShowComments = (
  dispatch,
  postId,
  authToken,
  showCommentFlag,
  setShowCommentFlag
) => {
  const commentedPostCreds = {
    post: postId,
    authToken: authToken,
  };
  dispatch(commentActions.getComments(commentedPostCreds));
  setShowCommentFlag(!showCommentFlag);
};
