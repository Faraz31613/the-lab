import { call, put, takeLatest, all } from "redux-saga/effects"
import * as actionTypes from "./types"
import * as todoServices from "services/todoServices"


function* saveTodo(action) {
  const response = yield call(todoServices.saveTodo, action.payload)
  yield put({ type: actionTypes.ADD_TODO, payload: response.data })
}

function* saveTodoSaga() {
  yield takeLatest(actionTypes.SAVE_TODO, saveTodo)
}

function* getTodos(action) {
  const todos = yield call(todoServices.getAllTodos)
//   console.log("running getTodoSaga")
//   console.log(todos.data)
  yield put({ type: actionTypes.GET_TODOS_TO_STATE, payload: todos.data })
}

function* getTodosSaga() {
  yield takeLatest(actionTypes.GET_TODOS, getTodos)
}


export default function* rootSaga() {
  yield all([saveTodoSaga(), getTodosSaga()])
}
