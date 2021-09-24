import { call, put, takeEvery } from "redux-saga/effects";

import * as actionTypes from "./type";
import * as actions from "./action";
import * as httpServices from "services/commentServices";

function* addComment(action) {
  yield call(httpServices.addComment, action.payload);
}

export function* addCommentSaga() {
  yield takeEvery(actionTypes.ADD_COMMENT, addComment);
}

function* getComments(action) {
  const res = yield call(httpServices.getComments, action.payload);
  yield put(actions.showComments(res.data));
}

export function* getCommentsSaga() {
  yield takeEvery(actionTypes.GET_COMMENTS, getComments);
}
