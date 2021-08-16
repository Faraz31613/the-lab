// import { useDispatch } from "react-redux";
import { takeLatest } from "@redux-saga/core/effects";

import * as actionType from  "modules/logIn/types"
import * as action from "modules/logIn/action"

function* checkUserExistsSaga(username,password){
    // const dispatch =useDispatch()
    const response = fetch("http://127.0.0.1:8000/api/token/");
    const data = response.json()
    // dispatch (action.signIn)
    console.log(data)
    return data
}

export default function* signInWatcher (){
    yield takeLatest(actionType.CHECK_USER_EXITS,checkUserExistsSaga)
}