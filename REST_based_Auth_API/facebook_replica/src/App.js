import { Route, BrowserRouter, Link, Switch } from "react-router-dom";

import SignIn from "components/signIn";
import SignUp from "components/signUp";
import Home from "components/Home";
import "./App.css";

function App() {
  return (
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
  );
}

export default App;
