import { call, put, takeEvery } from "redux-saga/effects";

import * as actionTypes from "./type";
import * as actions from "./action";
import * as httpServices from "services/postServices";

function* getPosts(action) {
  const res = yield call(httpServices.getPosts, action.payload);
  yield put(actions.showPosts(res.data));
}

export function* getPostsSaga() {
  yield takeEvery(actionTypes.GET_POSTS, getPosts);
}
