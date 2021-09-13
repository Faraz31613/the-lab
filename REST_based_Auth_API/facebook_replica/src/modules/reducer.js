import { combineReducers } from "redux";

import authReducer from "./authentication/reducer";
import notificationReducer from "./notification/reducer";
import postReducer from "./post/reducer";
import likeReducer from "./like/reducer";
import commentReducer from "./comment/reducer";

export default combineReducers({
  notification: notificationReducer,
  auth: authReducer,
  post: postReducer,
  like: likeReducer,
  comment: commentReducer,
});
