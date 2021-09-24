import { all } from "redux-saga/effects";

import { registerUserSaga, signInSaga } from "modules/authentication/saga";
import {
  getNotificationsSaga,
  markAsReadSaga,
} from "modules/notification/saga";
import { getPostsSaga } from "modules/post/saga";
import { likeSaga, unlikeSaga } from "modules/like/saga";
import { addCommentSaga, getCommentsSaga } from "modules/comment/saga";

export default function* rootSaga() {
  yield all([
    registerUserSaga(),
    signInSaga(),
    getNotificationsSaga(),
    markAsReadSaga(),
    getPostsSaga(),
    likeSaga(),
    unlikeSaga(),
    addCommentSaga(),
    getCommentsSaga(),
  ]);
}
