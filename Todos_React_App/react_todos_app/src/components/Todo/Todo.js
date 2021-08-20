import React, { useState } from "react"

import { isEmpty, formatWhitespace } from "utils/string"

import "./styles.css"

const Todo = ({ todo, removeTodo, updateTodo }) => {
  const [editMode, setEditMode] = useState(false)
  const toggleEditMode = () => setEditMode(!editMode)

  const [updatedText, setUpdatedText] = useState(todo.text)

  const onChange = (event) => {
    const text = formatWhitespace(event.target.value)
    setUpdatedText(text)
  }

  const updateTodoText = () => {
    if (isEmpty(updatedText)) return toggleEditMode()

    updateTodo({ ...todo, text: updatedText })
    toggleEditMode()
  }

  const todoClasses = editMode ? "todo-editable" : "todo-disabled"

  return (
    <div className="todo-container">
      <input
        className={`todo-input ${todoClasses}`}
        value={updatedText}
        disabled={!editMode}
        onBlur={updateTodoText}
        onChange={onChange}
      />
      <div className="todo-buttons">
        <div onClick={() => removeTodo(todo.id)}>X</div>
        <div onClick={setEditMode}>✎</div>
      </div>
    </div>
  )
}

export default Todo
