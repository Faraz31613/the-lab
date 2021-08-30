import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

const Home = () => {
  const isSignedIn = useSelector((state) => state.signIn["isSignedIn"]);
  if(!isSignedIn){
    return <Redirect to="/signIn" />
  }

  return <h3>Home</h3>;
};

export default Home;
