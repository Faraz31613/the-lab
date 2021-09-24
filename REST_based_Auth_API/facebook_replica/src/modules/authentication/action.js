import * as actionTypes from "./type";

//saga actioins
export const signUp = (userCred) => ({
  type: actionTypes.SIGN_UP,
  payload: userCred,
});
export const signIn = (userCred) => ({
  type: actionTypes.SIGN_IN,
  payload: userCred,
});

//reducer actions
export const successOrError = (message) => {
  return {
    type: actionTypes.SUCCESS_OR_ERROR,
    payload: message,
  };
};
export const emptySuccessOrError = () => ({
  type: actionTypes.EMPTY_SUCCESS_OR_ERROR,
  payload: {
    SuccessOrErrorText: null,
    SuccessOrErrorCode: null,
  },
});
export const successfullSignIn = (data) => ({
  type: actionTypes.SUCCESSFULL_SIGN_IN,
  payload: data,
});
export const logout = () => ({
  type: actionTypes.LOGOUT,
});
export const alreadySignedIn = (signedInUserData) => ({
  type: actionTypes.ALREADY_SIGNED_IN,
  payload: signedInUserData,
});
