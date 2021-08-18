import React, { useState } from "react";
// import Tasks from "./tasks";

export default function ToDoApp() {
  const initialState = [];
  const [tasks, addTask] = useState(initialState);
  const [todo, getToDo] = useState([]);

  function handleChangeTask(event) {
    const { name, value, type ,checked} = event.target;
    if (type === "checkbox") {
        // addTask(prevTasks => prevTasks.map((prevTask)=>{
        //     if(prevTask["work"]===value){
        //         prevTask["completed"]==!prevTask["completed"]
        //     }
        //     return prevTask
        // }))
    }else{
        getToDo((prevToDo) => ({ work: value, completed: false }));
    }
    console.log(tasks)
  }

  function addToDoTask(event) {
    if (todo["work"] !== "") {
      addTask((prevTasks) => [...prevTasks, todo]);
    }
  }

  return (
    <div>
      <div>
        <input
          type="text"
          className="tasks"
          name="task"
          placeholder="What needs to be done?  "
          onChange={handleChangeTask}
        />
        <button className="addTaskBtn" onClick={addToDoTask}>
          Add Task
        </button>
      </div>
      <div className="taskSheet">
        {/* <Tasks tasks={tasks}/> */}
        {tasks.map((task) => (
          <div className="contentDiv">
            <input
              className="addedTaskBox"
              type="checkbox"
              value={task["work"]}
              onChange={handleChangeTask}
            />
            <label className="addedTask">{task["work"]}</label>
          </div>
        ))}
      </div>
    </div>
  );
}
