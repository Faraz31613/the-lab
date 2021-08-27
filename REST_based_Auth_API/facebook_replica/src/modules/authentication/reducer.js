import { initialState } from "./init";
import * as actionTypes from "./type";

const reducer = (state = initialState, action) => {
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
    default:
      return state;
  }
};

export default reducer;
