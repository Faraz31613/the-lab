import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

const Friends = () => {
  const user = useSelector((state) => state.authReducer.signIn);
  const isSignedIn = user.isSignedIn;

  if (isSignedIn) {
    localStorage.setItem("refreshPath", "/friends");
  }
  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return (
    <div className="friends-container">
      <h3>Friends</h3>
    </div>
  );
};

export default Friends;
