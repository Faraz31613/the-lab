import React from "react";
import { useSelector } from "react-redux";

const Profile = () => {
  const signedInUser = useSelector((state) => state.authReducer.signIn["user"]);
  console.log(signedInUser);

  return (
    <div className="profile-container">
      <h3>{signedInUser.fName + " " + signedInUser.lName}</h3>
    </div>
  );
};

export default Profile;
