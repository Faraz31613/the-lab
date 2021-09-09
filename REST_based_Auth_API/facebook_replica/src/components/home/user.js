import React from "react";

const User = (props) => {
    const post=props.post
    const postAuthor = post.user
  return (
    <header className="post-author">
      <i className="fas fa-user"></i>
      {" " + post.user.first_name + " " + post.user.last_name}
    </header>
  );
};

export default User;
