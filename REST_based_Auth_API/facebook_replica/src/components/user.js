import React from "react";

const User = (props) => {
    const postAuthor = props.user
  return (
    <header className="post-author">
      <i className="fas fa-user"></i>
      {" " + postAuthor.first_name + " " + postAuthor.last_name}
    </header>
  );
};

export default User;
