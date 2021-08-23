import React from "react"
import TodoList from "components/TodoList/TodoList"

import "App.css"
import { store } from "modules/store"
import { Provider } from "react-redux"

const App = () => {
  return (
    <Provider store={store}>
      <div className="todo-app">
        <TodoList />
      </div>
    </Provider>
  )
}

export default App
