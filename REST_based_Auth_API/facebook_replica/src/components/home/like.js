import React from "react";
import { useSelector, useDispatch } from "react-redux";

import * as selector from "components/selector";
import * as hooks from "./hooks";

const Like = (props) => {
  const postId = props.postId;

  const signedInUserLikes = useSelector(selector.signedInUserLikes);
  const signedInCred = useSelector(selector.signedInCreds);

  const user = signedInCred.user;
  const userId = user.id;
  const authToken = user.access;

  const dispatch = useDispatch();

  var isLiked = false;
  var likeId = null;
  signedInUserLikes.forEach((like) => {
    if (like.post === postId) {
      isLiked = like.is_like;
      likeId = like.id;
    }
  });
  return (
    <button
      className="post-like-btn"
      onClick={() => hooks.handlePostLike(dispatch, isLiked, likeId, postId, userId, authToken)}
    >
      <i className={isLiked ? "fas fa-thumbs-up" : "far fa-thumbs-up"}></i>{" "}
      {isLiked ? "liked" : "Like"}
    </button>
  );
};

export default Like;
