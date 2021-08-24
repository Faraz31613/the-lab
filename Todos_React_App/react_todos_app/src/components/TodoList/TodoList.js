import React, { useEffect } from "react"
import { useSelector, useDispatch } from "react-redux"

import TodoForm from "components/TodoForm/TodoForm"
import Todo from "components/Todo/Todo"


import "./styles.css"
import { getTodos } from "modules/action"

const TodoList = () => {
  const todos = useSelector((state) => state.todos)

  const dispatch = useDispatch()
  useEffect(() => {
    dispatch(getTodos())
  }, 1)

  return (
    <div className="container">
      <h1>What's the Plan for Today?</h1>
      <TodoForm />
      {todos.map((todo) => (
        <Todo todo={todo} key={todo.id} />
      ))}
    </div>
  )
}

export default TodoList
