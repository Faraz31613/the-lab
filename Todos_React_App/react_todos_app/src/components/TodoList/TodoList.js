import React, { useState } from "react"

import TodoForm from "components/TodoForm/TodoForm"
import Todo from "components/Todo/Todo"

import "./styles.css"

const TodoList = () => {
  const [todos, setTodos] = useState([{ id: 100, text: "random" }])

  const addTodo = (todo) => setTodos([...todos, todo])

  const updateTodo = (updatedTodo) => {
    const updatedTodos = todos.map((todo) =>
      todo.id === updateTodo.id ? updatedTodo : todo
    )
    setTodos(updatedTodos)
  }

  const removeTodo = (id) => {
    const updatedTodos = todos.filter((todo) => todo.id !== id)
    setTodos(updatedTodos)
  }

  return (
    <div className="container">
      <h1>What's the Plan for Today?</h1>
      <TodoForm addTodo={addTodo} />
      {todos.map((todo) => (
        <Todo
          todo={todo}
          key={todo.id}
          removeTodo={removeTodo}
          updateTodo={updateTodo}
        />
      ))}
    </div>
  )
}

export default TodoList
