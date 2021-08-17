import React, {useState} from "react"
import Tasks from "./tasks"

export default function ToDoApp(){

    const initialState = []
    const [tasks,addTask] = useState(initialState)

    function addToDoTask(event){
        const task = document.getElementsByClassName("tasks")[0].value
        if (task!==""){
            addTask(prevTasks => [...prevTasks,task])
            document.getElementsByClassName("tasks")[0].value = ""
        }
    }

    return (
        <div>
            <div>
            <input className="tasks" name="task" placeholder="What needs to be done?  " />
            <button className="addTaskBtn" onClick={addToDoTask}>Add Task</button>
            </div>
            <div className='taskSheet'>
                <Tasks tasks={tasks}/>
            </div>
        </div>
    )
}