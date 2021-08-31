import { combineReducers } from "redux";

import authReducer from "./authentication/reducer";
import notificationReducer from "./notification/reducer";

export default combineReducers({
  notificationReducer,
  authReducer,
});
