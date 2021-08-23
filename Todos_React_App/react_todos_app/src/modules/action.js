import * as actionTypes from "./types"

export const addTodo = (todo) => ({
  type: actionTypes.ADD_TODO,
  payload: todo,
})

export const updateTodo = (todo) => ({
  type: actionTypes.UPDATE_TODO,
  payload: todo,
})

export const deleteTodo = (todo) => ({
  type: actionTypes.DELETE_TODO,
  payload: todo,
})
