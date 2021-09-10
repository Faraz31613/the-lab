import React, { useState, useEffect } from "react";
import { Link, Redirect } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import * as hooks from "components/hooks";
import * as actions from "modules/authentication/action";
import { notify } from "../../components/notification";
import * as selector from "components/selector";

import "./signIn.css";

const SignIn = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [usernameError, setUsernameError] = useState("");

  const isSignedInErrorMessage = useSelector(selector.isSignedInErrorMessage);
  const signedInCreds = useSelector(selector.signedInCreds);

  const dispatch = useDispatch();

  useEffect(() => {
    const alreadySignedIn = JSON.parse(decodeURI(localStorage.getItem("user")));
    if (alreadySignedIn !== null) {
      dispatch(actions.alreadySignedIn(alreadySignedIn));
    }

    if (
      alreadySignedIn === null &&
      isSignedInErrorMessage.SuccessOrErrorCode === 200
    ) {
      localStorage.setItem("user", encodeURI(JSON.stringify(signedInCreds)));  
      notify("Congratulations!", "Successfully Signed In", "success");
      return <Redirect to="/" />;
    }
    if (isSignedInErrorMessage.SuccessOrErrorCode === 401) {
      const errors = Object.keys(isSignedInErrorMessage.SuccessOrErrorText);
      if (errors.includes("detail")) {
        setUsernameError("User with these credentials does not exists!");
        setTimeout(() => {
          setUsernameError("");
        }, 4000);
      }
    }
  }, [isSignedInErrorMessage]);

  const signIn = hooks.useSignIn(username,password)
  
  if (isSignedInErrorMessage.SuccessOrErrorCode === 200) {
    return <Redirect to={localStorage.getItem("refreshPath")} />;
  }

  return (
    <div className="signIn-container">
      <form
        className="signIn-form-container"
        onSubmit={(e) => {
          e.preventDefault();
          signIn();
        }}
      >
        <input
          name="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="username"
          required
        ></input>
        {usernameError && <p>{usernameError}</p>}
        <input
          name="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="password"
          required
        ></input>
        <button className="form-button">Login</button>
        <br />
        <br />
        <p>
          Not a User?
          <Link to="/signUp">Register Here</Link>
        </p>
      </form>
    </div>
  );
};

export default SignIn;
