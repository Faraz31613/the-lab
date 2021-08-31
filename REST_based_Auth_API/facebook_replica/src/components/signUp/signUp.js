import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, Link } from "react-router-dom";

import { signUp } from "modules/authentication/action";
import { notify } from "../notification";
import * as actions from "modules/authentication/action";

import "./signUp.css";

const SignUp = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmedPassword, setConfirmedPassword] = useState("");

  const [usernameError, setUsernameError] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [confirmPasswordError, setConfirmPasswordError] = useState("");

  const dispatch = useDispatch();

  const handleSignUp = (event) => {
    event.preventDefault();
    if (password !== confirmedPassword) {
      setConfirmPasswordError("password does not match");
      return;
    }

    dispatch(signUp({ username, email, password }));
  };
  const isSignedUp = useSelector((state) => state.authReducer.message);
  useEffect(() => {
    if (password.length >= 8 || password.length === 0) {
      setPasswordError("");
    } else {
      setPasswordError("password is too short! use minimum 8 characters");
    }

    if (password === confirmedPassword) {
      setConfirmPasswordError("");
    }
    if (username.length >= 5 || username.length === 0) {
      setUsernameError("");
    } else {
      setUsernameError("Username is too short! use minimum 5 characters");
    }
    if (isSignedUp.SuccessOrErrorCode === 200) {
      setUsername("");
      setEmail("");
      setPassword("");
      setConfirmedPassword("");
      dispatch(actions.emptySuccessOrError());
      notify("Congratulations!", "Successfully registered", "success");
    }
    if (isSignedUp.SuccessOrErrorCode === 400) {
      const errors = Object.keys(isSignedUp.SuccessOrErrorText);
      if (errors.includes("username")) {
        setUsernameError("username already exists");
      }
      if (errors.includes("email")) {
        setEmailError("email already exists");
      }
    }
  }, [isSignedUp, username, password, confirmedPassword]);
  if (isSignedUp.SuccessOrErrorCode === 200) {
    return <Redirect to="/signIn" />;
  }
  return (
    <div className="signUp-container">
      <form className="signUp-form-container" onSubmit={handleSignUp}>
        <input
          name="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="username"
          required
        ></input>
        {usernameError && <p>{usernameError}</p>}
        <input
          name="email"
          value={email}
          type="email"
          onChange={(e) => setEmail(e.target.value)}
          placeholder="email"
          required
        ></input>
        {emailError && <p>{emailError}</p>}
        <input
          name="password"
          value={password}
          type="password"
          onChange={(e) => setPassword(e.target.value)}
          placeholder="password"
          required
        ></input>
        {passwordError && <p>{passwordError}</p>}
        <input
          name="confirmPassword"
          value={confirmedPassword}
          type="password"
          onChange={(e) => setConfirmedPassword(e.target.value)}
          placeholder="confirm password"
          required
        ></input>
        {confirmPasswordError && <p>{confirmPasswordError}</p>}
        <button className="form-button">Sign Up</button>
        <br />
        <br />
        <p>
          Already Registered?
          <Link to="/signIn">Login here</Link>
        </p>
      </form>
    </div>
  );
};

export default SignUp;
