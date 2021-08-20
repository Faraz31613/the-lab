import { createStore } from 'redux';

import 'App.css';
import TodoList from "components/TodoList/TodoList"

// const store = createStore(todosReducer)


function App() {
  return (
    <div className="todo-app">
      <TodoList />
    </div>
  );
}

export default App;
