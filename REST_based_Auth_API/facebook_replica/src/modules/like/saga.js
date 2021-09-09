import { call, put, takeEvery } from "redux-saga/effects";

import * as actionTypes from "./type";
import * as actions from "./action";
import * as httpServices from "services/likeServices";

function* like(action) {
  yield call(httpServices.like, action.payload);
  yield put(actions.getSignedInUserLikes(action.payload.authToken))
}

export function* likeSaga() {
  yield takeEvery(actionTypes.LIKE, like);
}

function* getSignedInUserLikes(action) {
  const res = yield call(httpServices.getSignedInUserLikes, action.payload);
  yield put(actions.showSignedInUserLikes(res.data));
}
export function* getSignedInUserLikesSaga() {
  yield takeEvery(actionTypes.GET_SIGNEDIN_USER_LIKES, getSignedInUserLikes);
}

function* unlike(action) {
  yield call(httpServices.unlike, action.payload);
  yield put(actions.getSignedInUserLikes(action.payload.authToken))
}

export function* unlikeSaga() {
  yield takeEvery(actionTypes.UNLIKE, unlike);
}
