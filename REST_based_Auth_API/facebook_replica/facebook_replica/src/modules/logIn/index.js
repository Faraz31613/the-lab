import React from "react";
import { useDispatch } from "react-redux";
import * as actionType from "modules/logIn/types"
import style from "modules/logIn/index.css"

export default function Login() {
  const dispatch = useDispatch();
  return (
    <div className="login-page">
      <form className="login-form" style={style.login_form}>
        <label>
          username:
          <input type="text" placeholder="enter your username" />
        </label>
        <br />
        <label>
          password:
          <input type="password" placeholder="enter your password" />
        </label>
        <br />
        <button type ="submit" onClick={() => dispatch(actionType.CHECK_USER_EXITS)}>
          Login
        </button>
      </form>
    </div>
  );
}
