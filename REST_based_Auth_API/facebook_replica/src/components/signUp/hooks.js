// import { signUp } from "modules/authentication/action";
import * as actions from "modules/authentication/action";

export const signUp = (
  e,
  dispatch,
  username,
  firstName,
  lastName,
  email,
  password,
  confirmedPassword,
  setConfirmPasswordError
) => {
  e.preventDefault();
  if (password !== confirmedPassword) {
    setConfirmPasswordError("password does not match");
    return;
  }

  dispatch(
    actions.signUp({
      username,
      email,
      password,
      first_name: firstName,
      last_name: lastName,
    })
  );
};
