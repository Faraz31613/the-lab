import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as selector from "modules/selector";

const Friends = () => {
  const isSignedIn = useSelector(selector.isSignedIn);

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
