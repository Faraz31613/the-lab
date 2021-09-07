import { initialState } from "./init";
import * as actionTypes from "./type";

const likeReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SHOW_LIKE:
      return {
        ...state,
        likes: [...state.likes, action.payload],
      };
    default:
      return state;
  }
};

export default likeReducer;
