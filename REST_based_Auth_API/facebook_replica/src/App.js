import { Provider } from "react-redux";
import { Route, BrowserRouter, Switch } from "react-router-dom";
import ReactNotification from "react-notifications-component";

import Home from "./components/home";
import SignUp from "./components/signUp";
import SignIn from "./components/signIn";
import store from "modules/authentication/store";

import "react-notifications-component/dist/theme.css";
import "./App.css";

function App() {
  return (
    <Provider store={store}>
      <ReactNotification />
      <div className="App">
        <h3>facebook replica</h3>
        <BrowserRouter>
          <div>
            <Switch>
              <Route path="/" exact>
                <Home />
              </Route>
              <Route path="/signUp">
                <SignUp />
              </Route>
              <Route path="/signIn">
                <SignIn />
              </Route>
            </Switch>
          </div>
        </BrowserRouter>
      </div>
    </Provider>
  );
}

export default App;
