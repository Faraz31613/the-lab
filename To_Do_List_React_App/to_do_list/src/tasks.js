import React from "react";

export default function Tasks(props) {
  const initialStyle = {
    fontStyle: "italic",
    color: "#cdcdcd",
    textDecoration: "line-through",
  };

  function handleCheck(event) {
    const { type, value, checked } = event.target;
    if (type === "checkbox" && checked === true) {
      document
        .getElementsByName(value)[0]
        .setAttribute(
          "style",
          "text-decoration:" +
            initialStyle.textDecoration +
            ";color:" +
            initialStyle.color +
            ";font-style:" +
            initialStyle.fontStyle
        );
    } else {
      document.getElementsByName(value)[0].setAttribute("style", null);
    }
  }
  console.log(props.tasks);
  return (
    <div>
      {props.tasks.map((task) => (
        <div className="contentDiv">
          <input
            className="addedTaskBox"
            type="checkbox"
            value={task}
            onChange={handleCheck}
          />
          <label className="addedTask" name={task}>
            {task}
          </label>
        </div>
      ))}
    </div>
  );
}
