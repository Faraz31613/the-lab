import * as signInActions from "modules/authentication/action";

export const signIn = (e, dispatch, username, password) => {
  e.preventDefault();
  dispatch(signInActions.signIn({ username, password }));
};
