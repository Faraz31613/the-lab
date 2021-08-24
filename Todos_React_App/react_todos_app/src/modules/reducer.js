import { initialState } from "./init"
import * as actionTypes from "./types"

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.ADD_TODO:
      return { ...state, todos: [...state.todos, action.payload] }
    case actionTypes.UPDATE_TODO:
      const updatedTodos = state.todos.map((todo) =>
        todo.id === action.payload.id ? action.payload : todo
      )
      return { ...state, todos: updatedTodos }
    case actionTypes.DELETE_TODO:
      const updatedTodo = state.todos.filter(
        (todo) => todo.id !== action.payload.id
      )
      return { ...state, todos: updatedTodo }
    case actionTypes.GET_TODOS_TO_STATE:
      return { todos: action.payload }
    default:
      return state
  }
}
export default reducer
