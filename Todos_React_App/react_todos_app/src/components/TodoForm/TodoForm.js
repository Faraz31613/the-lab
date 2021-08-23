import React, { useState, useEffect, useRef } from "react"
import {useDispatch} from 'react-redux'

import { isEmpty, formatWhitespace } from "utils/string"
import { addTodo } from "modules/action"

import "./styles.css"

let latestID = 1

const uniqueID = () => latestID++

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
    const todo = { id: uniqueID(), text }
    
    dispatch(addTodo(todo))
    
    // addTodo(todo)
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
