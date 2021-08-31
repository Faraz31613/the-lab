import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

const Home = () => {
  const isSignedIn = useSelector(
    (state) => state.authReducer.signIn["isSignedIn"]
  );
  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return (
    <div className="home-container">
      <h3>Home</h3>
    </div>
  );
};

export default Home;
