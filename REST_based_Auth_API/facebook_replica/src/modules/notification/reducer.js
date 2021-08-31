import { initialState } from "./init";
import * as actionTypes from "modules/notification/type";

const notificationReducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.SHOW_NOTIFICATIONS:
      return { ...state, notifications: action.payload };
    default:
      return state;
  }
};
export default notificationReducer;
