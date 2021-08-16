import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from "react-redux";
import App from './App';

import { applyMiddleware, createStore, compose } from "redux";

import createSagaMiddleware from "@redux-saga/core";
import reducer from "modules/logIn/reducer";
import signInWatcher from "modules/logIn/sagas"

const sagaMiddleware = createSagaMiddleware();

const store = createStore(reducer, applyMiddleware(sagaMiddleware));

sagaMiddleware.run(signInWatcher)


ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
