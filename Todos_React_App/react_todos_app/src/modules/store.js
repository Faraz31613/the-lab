import {createStore, applyMiddleware} from "redux"
import createSagaMiddleware from "@redux-saga/core"

import reducer from "./reducer"
import logger from "redux-logger"
import rootSaga from "./saga"


const sagaMiddleWare = createSagaMiddleware()
export const store = createStore(reducer,applyMiddleware(logger,sagaMiddleWare))
sagaMiddleWare.run(rootSaga)
export default store