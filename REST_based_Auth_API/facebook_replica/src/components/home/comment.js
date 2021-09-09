import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import * as selector from "components/selector";
import * as hooks from "./hooks";

const Comment = (props) => {
  const [comment, setComment] = useState("");
  const [showCommentFlag, setShowCommentFlag] = useState(false);

  const postId = props.postId;
  const addCommentFlag = props.addCommentFlag;
  const postIdForComment = props.postIdForComment;

  const comments = useSelector(selector.comments);
  const signedInCred = useSelector(selector.signedInCreds);

  const user = signedInCred.user;
  const userId = user.id;
  const authToken = user.access;

  const dispatch = useDispatch();

  return (
    <>
      <input
        className="add-comment"
        value={comment}
        onChange={(e) => {
          setComment(e.target.value);
        }}
        onKeyPress={(e) =>
          hooks.handlePostComment(
            e,
            dispatch,
            postId,
            userId,
            comment,
            authToken,
            setComment
          )
        }
        style={
          addCommentFlag && postIdForComment === postId
            ? { display: "block" }
            : { display: "none" }
        }
        placeholder="Add your Comment..."
      ></input>

      <a
        className="show-comment"
        onClick={() =>
          hooks.handleShowComments(
            dispatch,
            postId,
            authToken,
            showCommentFlag,
            setShowCommentFlag
          )
        }
      >
        Show Comments...
      </a>
      <section
        style={showCommentFlag ? { display: "block" } : { display: "none" }}
        className="comments-section"
      >
        {comments.map((comment) => {
          if (comment.post === postId) {
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
