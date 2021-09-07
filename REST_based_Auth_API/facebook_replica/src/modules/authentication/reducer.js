import { initialState } from "./init";
import * as actionTypes from "./type";

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SUCCESS_OR_ERROR:
      return { ...state, message: action.payload };
    case actionTypes.EMPTY_SUCCESS_OR_ERROR:
      return { ...state, message: action.payload };
    case actionTypes.SUCCESSFULL_SIGN_IN:
      return {
        ...state,
        message: action.payload.message,
        signIn: action.payload.signIn,
      };
    case actionTypes.LOGOUT:
      return {
        ...state,
        message: {
          SuccessOrErrorText: null,
          SuccessOrErrorCode: null,
        },
        signIn: {
          isSignedIn: false,
          user: {},
        },
        isValidToken: false,
      };
      case actionTypes.ALREADY_SIGNED_IN:
        return {
          ...state,
          message: {
            SuccessOrErrorText: "success",
            SuccessOrErrorCode: 200,
          },
          signIn: action.payload,
        }
    default:
      return state;
  }
};

export default authReducer;
