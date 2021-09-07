import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

const Profile = () => {
  const user = useSelector((state) => state.authReducer.signIn);
  const isSignedIn = user.isSignedIn;

  if (isSignedIn) {
    localStorage.setItem("refreshPath", "/profile");
  }
  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return (
    <div className="profile-container">
      <h3>{user.user.f_name + " " + user.user.l_name}</h3>
    </div>
  );
};

export default Profile;
