import React, { useEffect } from "react";
import { useDispatch } from "react-redux";
import { Redirect } from "react-router-dom";

import { notify } from "./notification";
import * as actions from "modules/authentication/action";

const Logout = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(actions.logout());
    localStorage.clear();
    notify("Congratulations!", "Successfully Logged out", "success");
  });

  return <Redirect to="/signIn" />;
};

export default Logout;
