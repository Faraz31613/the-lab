import http from "httpCommon"

export async function getAllTodos(){
    return await http.get("/todo/")
}

export function saveTodo(data){
    return http.post("/todo/",data)
}

