import { Provider } from "react-redux";
import { Route, BrowserRouter, Switch } from "react-router-dom";
import ReactNotification from "react-notifications-component";

import Home from "./pages/home/home";
import SignUp from "./pages/signUp/signUp";
import SignIn from "./pages/signIn/signIn";
import Logout from "components/logout";
import Profile from "pages/profile/profile";
import Friends from "pages/friends/friends";
import Notifications from "pages/notifications/notifications";
import Navbar from "pages/navbar/navbar";
import ProtectedRoute from "components/protected-route/protected-route"

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
              <ProtectedRoute path="/" exact>
                <Home />
              </ProtectedRoute>
              <Route path="/signUp">
                <SignUp />
              </Route>
              <Route path="/signIn">
                <SignIn />
              </Route>
              <ProtectedRoute path="/logout">
                <Logout />
              </ProtectedRoute>
              <ProtectedRoute path="/profile">
                <Profile />
              </ProtectedRoute>
              <ProtectedRoute path="/friends">
                <Friends />
              </ProtectedRoute>
              <ProtectedRoute path="/notifications">
                <Notifications />
              </ProtectedRoute>
            </Switch>
          </div>
        </BrowserRouter>
      </div>
    </Provider>
  );
}

export default App;
