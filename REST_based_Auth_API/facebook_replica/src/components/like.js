import React from "react";
import { useSelector } from "react-redux";

import * as selector from "components/selector";
import * as hooks from "components/hooks";

const Like = (props) => {
  const postId = props.postId;

  const signedInUserLikes = useSelector(selector.signedInUserLikes);
  const signedInCred = useSelector(selector.signedInCreds);

  const user = signedInCred.user;
  const userId = user.id;
  const authToken = user.access;

  let isLiked = false;
  let likeId = null;
  signedInUserLikes.forEach((like) => {
    if (like.post === postId) {
      isLiked = like.is_like;
      likeId = like.id;
    }
  });
  const handlePostLike = hooks.useHandlePostLike(
    isLiked,
    likeId,
    postId,
    userId,
    authToken
  );
  return (
    <button className="post-like-btn" onClick={() => handlePostLike()}>
      <i className={isLiked ? "fas fa-thumbs-up" : "far fa-thumbs-up"}></i>{" "}
      {isLiked ? "liked" : "Like"}
    </button>
  );
};

export default Like;
