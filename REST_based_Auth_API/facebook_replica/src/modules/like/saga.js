import { call, put, takeEvery } from "redux-saga/effects";

import * as actionTypes from "./type";
import * as postActions from "modules/post/action";
import * as httpServices from "services/likeServices";

function* like(action) {
  yield call(httpServices.like, action.payload);
  yield put(postActions.getPosts(action.payload.authToken));
}

export function* likeSaga() {
  yield takeEvery(actionTypes.LIKE, like);
}

function* unlike(action) {
  yield call(httpServices.unlike, action.payload);
  yield put(postActions.getPosts(action.payload.authToken));
}

export function* unlikeSaga() {
  yield takeEvery(actionTypes.UNLIKE, unlike);
}
