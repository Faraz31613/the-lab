import React, { useState } from "react";

import "./signUp.css";

const SignUp = () => {
  const [username, setUsername] = useState();
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const [confirmedPassword, setConfirmedPassword] = useState();

  const onFillCredetials = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case "username":
        setUsername(value);
      case "email":
        setEmail(value);
      case "password":
        setPassword(value);
      case "confirmPassword":
        setConfirmedPassword(value);
    }
  };

  return (
    <div className="signUp-form-container">
      <input
        name="username"
        // onChange={onFillCredetials}
        placeholder="username"
      ></input>
      <input
        name="email"
        type="email"
        // onChange={onFillCredetials}
        placeholder="email"
      ></input>
      <input
        name="password"
        type="password"
        // onChange={onFillCredetials}
        placeholder="password"
      ></input>
      <input
        name="confirmPassword"
        type="password"
        // onChange={onFillCredetials}
        placeholder="confirm password"
      ></input>
      <button className="form-button">Sign Up</button>
    </div>
  );
};

export default SignUp;
