import React from "react";
import { useSelector } from "react-redux";

import * as selector from "modules/selector";
import * as hooks from "modules/hooks";

const Like = (props) => {
  const postId = props.post.id;
  const isLiked = props.post.is_liked;

  const signedInCred = useSelector(selector.signedInCreds);

  const user = signedInCred.user;
  const userId = user.id;
  const authToken = user.access;

  const handlePostLike = hooks.useHandlePostLike(
    isLiked,
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
