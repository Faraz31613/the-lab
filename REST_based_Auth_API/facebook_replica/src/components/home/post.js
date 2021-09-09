import React, { useState } from "react";

import User from "./user";
import Like from "./like";
import Comment from "./comment";

const Post = (props) => {
  //   const [addCommentFlag, setAddCommentFlag] = useState(false);
  //   const [postIdForComment, setPostIdForComment] = useState();
  const addCommentFlag = props.addCommentFlag;
  const postIdForComment = props.postIdForComment;
  const setAddCommentFlag = props.setAddCommentFlag;
  const setPostIdForComment = props.setPostIdForComment;

  const post = props.post;
  return (
    <section
        onMouseOver={(e) => {
          if (postIdForComment !== post.id) {
            setAddCommentFlag(false);
          }
        }}
      className="post-section"
    >
      <User post={post} />

      <p className="post-text">{post.text_post}</p>

      <Like postId={post.id} />

      <button
        className="post-comment-btn"
        onClick={(e) => {
          setAddCommentFlag(!addCommentFlag);
          setPostIdForComment(post.id);
        }}
      >
        <i className="far fa-comment"></i> comment
      </button>

      <button className="post-share-btn">
        <i className="fas fa-share"></i> share
      </button>

      <Comment
        postId={post.id}
        addCommentFlag={addCommentFlag}
        postIdForComment={postIdForComment}
      />
    </section>
  );
};

export default Post;
