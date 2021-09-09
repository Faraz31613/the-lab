import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as selector from "./selector";

export const AuthNavigation = () => {
  const isSignedIn = useSelector(selector.isSignedIn);
  
  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }
};
