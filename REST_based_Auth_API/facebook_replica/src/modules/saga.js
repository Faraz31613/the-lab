import { all } from "redux-saga/effects";

import { registerUserSaga, signInSaga } from "modules/authentication/saga";
import {
  getNotificationsSaga,
  markAsReadSaga,
} from "modules/notification/saga";
import { getPostsSaga } from "modules/post/saga";
import { likeSaga, getLikesSaga } from "modules/like/saga";

export default function* rootSaga() {
  yield all([
    registerUserSaga(),
    signInSaga(),
    getNotificationsSaga(),
    markAsReadSaga(),
    getPostsSaga(),
    likeSaga(),
    getLikesSaga(),
  ]);
}
