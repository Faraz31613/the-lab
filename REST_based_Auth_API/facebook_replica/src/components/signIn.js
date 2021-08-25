import React, { useState } from "react";
// import { Redirect, useLocation } from "react-router";
import { Link } from "react-router-dom";

import "./signIn.css";

const SignIn = () => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  //   const [isSignedIn,setIsSignedIn] = useState(false)

  const handleSubmit = (event) => {
    if (email !== "" && password !== "") {
      //dispatch actions
      //is signed in true
    }
  };

  const onFillCredetials = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case "email":
        setEmail(value);
      case "password":
        setPassword(value);
    }
  };

  return (
    <div className="signIn-form-container">
      <input
        name="email"
        type="email"
        onChange={onFillCredetials}
        placeholder="email"
      ></input>
      <input
        name="password"
        type="password"
        onChange={onFillCredetials}
        placeholder="password"
      ></input>
      <button className="form-button" onSubmit={handleSubmit}>
        Login
      </button>
      <br />
      <br />
      <p>
        Not a User?
        <Link to="/signUp">Register Here</Link>
      </p>
    </div>
  );
};

export default SignIn;
