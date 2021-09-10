import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as actions from "modules/authentication/action";
import * as selector from "components/selector";
import { notify } from "../notification";

export const ProtectedRoute = ({ children }) => {
  const signedInCreds = useSelector(selector.signedInCreds);
  const isSignedIn = signedInCreds.isSignedIn;

  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return children;
};

export default ProtectedRoute;
