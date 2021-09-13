import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as selector from "modules/selector";

export const ProtectedRoute = ({ children }) => {
  const { isSignedIn  } = useSelector(selector.signedInCreds);

  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return children;
};

export default ProtectedRoute;
