import {createStore, applyMiddleware} from "redux"

import reducer from "./reducer"
import logger from "redux-logger"

export const store = createStore(reducer,applyMiddleware(logger))
export default store