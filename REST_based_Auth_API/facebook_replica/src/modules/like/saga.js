import { call, put, takeEvery } from "redux-saga/effects";

import * as actionTypes from "./type";
import * as actions from "./action";
import * as httpServices from "services/likeServices";

function* like(action) {
  yield call(httpServices.like, action.payload);
}

export function* likeSaga() {
  yield takeEvery(actionTypes.LIKE, like);
}

function* getLikes(action) {
  const res = yield call(httpServices.getlikes, action.payload);
  if (res.data[0] !== undefined) {
    yield put(actions.showLike(res.data[0]));
  }
}
export function* getLikesSaga() {
  yield takeEvery(actionTypes.GET_LIKE, getLikes);
}
