import { combineReducers } from "redux";

import authReducer from "./authentication/reducer";
import notificationReducer from "./notification/reducer";
import postReducer from "./post/reducer";
import likeReducer from "./like/reducer";

export default combineReducers({
  notificationReducer,
  authReducer,
  postReducer,
  likeReducer,
});
