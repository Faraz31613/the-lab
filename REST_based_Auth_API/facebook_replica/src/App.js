import { Provider } from "react-redux";
import { Route, BrowserRouter, Switch } from "react-router-dom";
import ReactNotification from "react-notifications-component";

import Home from "./components/home/home";
import SignUp from "./components/signUp/signUp";
import SignIn from "./components/signIn/signIn";
import Logout from "components/logout";
import Profile from "components/profile/profile";
import Friends from "components/friends/friends";
import Notifications from "components/notifications/notifications";
import Navbar from "components/navbar/navbar";

import store from "modules/store";

import "react-notifications-component/dist/theme.css";
import "./App.css";

function App() {
  return (
    <Provider store={store}>
      <ReactNotification />
      <div className="App">
        <BrowserRouter>
          <Navbar />
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
              <Route path="/logout">
                <Logout />
              </Route>
              <Route path="/profile">
                <Profile />
              </Route>
              <Route path="/friends">
                <Friends />
              </Route>
              <Route path="/notifications">
                <Notifications />
              </Route>
            </Switch>
          </div>
        </BrowserRouter>
      </div>
    </Provider>
  );
}

export default App;
