import * as actionTypes from "./types"

//saga actions
export const saveTodo = (todo) => ({
  type:actionTypes.SAVE_TODO,
  payload : todo,
})
export const getTodos = () =>({
  type:actionTypes.GET_TODOS,
})


//reducer actions
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
