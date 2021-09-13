import React from "react";

import User from "./user";
import Like from "./like";
import Comment from "./comment";

const Post = (props) => {
  const post = props.post;
  return (
    <section className="post-section">
      <User user={post.user} />

      <p className="post-text">{post.text_post}</p>

      <Like post={post} />

      <Comment post={post} />
    </section>
  );
};

export default Post;
