import React, { useState, useEffect } from "react";
import { Link, Redirect } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import * as actions from "modules/authentication/action";
import { notify } from "../notification";
import "./signIn.css";

const SignIn = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [usernameError, setUsernameError] = useState("");

  const dispatch = useDispatch();
  const handleSubmit = (event) => {
    event.preventDefault();
    dispatch(actions.signIn({ username, password }));
  };

  const isSignedIn = useSelector((state) => state.authReducer.message);

  useEffect(() => {
    const alreadySignedIn = JSON.parse(decodeURI(localStorage.getItem("user")));
    if (alreadySignedIn !== null) {
      dispatch(actions.alreadySignedIn(alreadySignedIn));
    }

    if (alreadySignedIn === null && isSignedIn.SuccessOrErrorCode === 200) {
      notify("Congratulations!", "Successfully Signed In", "success");
      return <Redirect to="/" />;
    }
    if (isSignedIn.SuccessOrErrorCode === 401) {
      const errors = Object.keys(isSignedIn.SuccessOrErrorText);
      if (errors.includes("detail")) {
        setUsernameError("User with these credentials does not exists!");
        setTimeout(() => {
          setUsernameError("");
        }, 4000);
      }
    }
  }, [isSignedIn]);
  if (isSignedIn.SuccessOrErrorCode === 200) {
    return <Redirect to={localStorage.getItem("refreshPath")} />;
  }

  return (
    <div className="signIn-container">
      <form className="signIn-form-container" onSubmit={handleSubmit}>
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
