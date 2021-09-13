import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as selector from "modules/selector";

const Profile = () => {
  const signedInCreds = useSelector(selector.signedInCreds);
  const user = signedInCreds.user;
  const isSignedIn = signedInCreds.isSignedIn;

  if (isSignedIn) {
    localStorage.setItem("refreshPath", "/profile");
  }
  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return (
    <div className="profile-container">
      <h3>{user.f_name + " " + user.l_name}</h3>
    </div>
  );
};

export default Profile;
