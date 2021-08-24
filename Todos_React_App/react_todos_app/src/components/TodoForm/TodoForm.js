import React, { useState, useEffect, useRef } from "react"
import { useDispatch } from "react-redux"

import { isEmpty, formatWhitespace } from "utils/string"
import { saveTodo } from "modules/action"

import "./styles.css"

const TodoForm = () => {
  const [input, setInput] = useState("")

  const inputRef = useRef(null)

  useEffect(() => {
    inputRef.current.focus()
  })
  const dispatch = useDispatch()

  const onAddTodo = () => {
    const text = formatWhitespace(input)
    if (isEmpty(text)) return

    dispatch(saveTodo({ todo_text: text }))

    setInput("")
  }

  const onChange = (e) => setInput(e.target.value)

  return (
    <div className="form-container">
      <input
        className="form-input"
        value={input}
        ref={inputRef}
        onChange={onChange}
        placeholder="Add a todo"
      ></input>
      <button className="form-button" onClick={onAddTodo}>
        Add
      </button>
    </div>
  )
}

export default TodoForm
