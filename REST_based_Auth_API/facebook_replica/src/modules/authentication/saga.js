import { call, put, takeEvery } from "redux-saga/effects";

import * as actionTypes from "./type";
import * as actions from "./action";
import * as httpServices from "services/authServices";

function* registerUser(action) {
  const response = yield call(httpServices.registerUser, action.payload);
  yield put(
    actions.successOrError({
      SuccessOrErrorText: response.data,
      SuccessOrErrorCode: response.status,
    })
  );
}

export function* registerUserSaga() {
  yield takeEvery(actionTypes.SIGN_UP, registerUser);
}

function* signIn(action) {
  const response = yield call(httpServices.signIn, action.payload);
  if (response.status === 200) {
    yield put(
      actions.successfullSignIn({
        message: {
          SuccessOrErrorText: "success",
          SuccessOrErrorCode: response.status,
        },
        signIn: {
          isSignedIn: true,
          user: response.data,
        },
      })
    );
  } else {
    yield put(
      actions.successOrError({
        SuccessOrErrorText: response.data,
        SuccessOrErrorCode: response.status,
      })
    );
  }
}

export function* signInSaga() {
  yield takeEvery(actionTypes.SIGN_IN, signIn);
}
