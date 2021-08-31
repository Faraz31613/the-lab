import { call, put, takeEvery } from "redux-saga/effects";

import * as actionTypes from "./type";
import * as actions from "modules/notification/action";
import * as httpServices from "services/notificationServices";

function* getNotifications(action) {
  const notifications = yield call(
    httpServices.getNotification,
    action.payload
  );
  yield put(actions.showNotifications(notifications.data));
}
export function* getNotificationsSaga() {
  yield takeEvery(actionTypes.GET_NOTIFICAIONS, getNotifications);
}

function* markAsRead(action) {
  const response = yield call(httpServices.markAsRead, action.payload);
  if (response.status === 200) {
    yield put(actions.getNotification(action.payload["authToken"]));
  }
}

export function* markAsReadSaga() {
  yield takeEvery(actionTypes.MARK_AS_READ, markAsRead);
}
