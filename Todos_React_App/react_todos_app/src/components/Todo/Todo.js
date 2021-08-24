import React, { useState } from "react"
import { useDispatch } from "react-redux"

import { isEmpty, formatWhitespace } from "utils/string"
import * as actions from "modules/action"

import "./styles.css"

const Todo = ({todo}) => {
  const [editMode, setEditMode] = useState(false)
  const toggleEditMode = () => setEditMode(!editMode)

  const [updatedText, setUpdatedText] = useState(todo.todo_text)

  const onChange = (event) => {
    const text = formatWhitespace(event.target.value)
    setUpdatedText(text)
  }

  const dispatch = useDispatch()
  const updateTodoText = () => {
    if (isEmpty(updatedText)) return toggleEditMode()
    const updatedTodo = { ...todo, todo_text: updatedText }
    dispatch(actions.updateTodo(updatedTodo))
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
        <div onClick={() => dispatch(actions.deleteTodo(todo))}>X</div>
        <div onClick={setEditMode}>✎</div>
      </div>
    </div>
  )
}

export default Todo
