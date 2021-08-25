import React from "react";
import { Redirect } from "react-router-dom";
export const Home = () => {
  const isAutheticated = false;
  if (!isAutheticated) {
    return <Redirect to="/signIn" />;
  }
  return <h3>Home</h3>;
};

export default Home;
