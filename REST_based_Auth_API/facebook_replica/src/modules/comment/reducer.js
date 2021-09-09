import { initialState } from "./init";
import * as actionTypes from "./type";

const commentReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SHOW_COMMENTS:
      return {
        ...state,
        comments: action.payload,
      };
    default:
      return state;
  }
};

export default commentReducer;
