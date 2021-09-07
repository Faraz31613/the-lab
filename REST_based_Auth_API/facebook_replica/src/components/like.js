import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import * as likeActions from "modules/like/action";

const Like = (props) => {
  const user = useSelector((state) => state.authReducer.signIn);
  const likes = useSelector((state) => state.likeReducer.likes);
  const authToken = user.user.access;
  const dispatch = useDispatch();
  const handlePostLike = (event) => {
    const createLikeCred = {
      likeCred: {
        post: props.postId,
        user: props.userId,
        comment: null,
        is_like: true,
        like_type: "P",
      },
      authToken: authToken,
    };
    dispatch(likeActions.like(createLikeCred));
  };

  useEffect(() => {
    const likedPostOrCommentCred = {
      likedCred: {
        comment: null,
        post: props.postId,
      },
      authToken: authToken,
    };
    dispatch(likeActions.getLike(likedPostOrCommentCred));
  }, likes);
  
  return (
    <>
      {}
      <button className="post-like-btn" onClick={handlePostLike}>
        <i className="far fa-thumbs-up"></i> Like
      </button>
    </>
  );
};

export default Like;
