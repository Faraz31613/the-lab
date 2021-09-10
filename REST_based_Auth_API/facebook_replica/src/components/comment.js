import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";

import * as selector from "components/selector";
import * as hooks from "components/hooks";

const Comment = (props) => {
  const post = props.post;

  const [comment, setComment] = useState("");
  const [showCommentFlag, setShowCommentFlag] = useState(false);
  const [addCommentFlag, setAddCommentFlag] = useState(false);

  const comments = useSelector(selector.comments);
  const signedInCred = useSelector(selector.signedInCreds);

  const user = signedInCred.user;
  const userId = user.id;
  const authToken = user.access;

  const handlePostComment = hooks.useHandlePostComment(
    post.id,
    userId,
    comment,
    authToken
  );

  const handleShowComments = hooks.useHandleShowComments(post.id, authToken);

  return (
    <>
      <button
        className="post-comment-btn"
        onClick={(e) => {
          setAddCommentFlag(!addCommentFlag);
        }}
      >
        <i className="far fa-comment"></i> comment
      </button>

      <button className="post-share-btn">
        <i className="fas fa-share"></i> share
      </button>
      <input
        className="add-comment"
        value={comment}
        onChange={(e) => {
          setComment(e.target.value);
        }}
        onKeyPress={(e) => {
          if (comment !== "" && e.key === "Enter") {
            handlePostComment();
            setComment("");
          }
        }}
        style={addCommentFlag ? { display: "block" } : { display: "none" }}
        placeholder="Add your Comment..."
      ></input>

      <a
        className="show-comment"
        onClick={() => {
          handleShowComments();
          setShowCommentFlag(!showCommentFlag);
        }}
      >
        Show Comments...
      </a>
      <section
        style={showCommentFlag ? { display: "block" } : { display: "none" }}
        className="comments-section"
      >
        {comments.map((comment) => {
          if (comment.post === post.id) {
            return (
              <p className="comment" key={comment.id}>
                <i className="fas fa-user-circle"></i>
                {" " + comment.comment_text}
              </p>
            );
          }
        })}
      </section>
    </>
  );
};

export default Comment;
