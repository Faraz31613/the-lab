import { initialState } from "./init";
import * as actionTypes from "./type";

const postReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SHOW_POSTS:
        return { ...state, posts : action.payload }
    default:
      return state;
  }
};

export default postReducer
