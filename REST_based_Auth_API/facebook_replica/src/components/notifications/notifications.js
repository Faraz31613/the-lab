import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as actions from "modules/notification/action";
import * as selector from "components/selector";
import * as hooks from "./hooks";

import "./notifications.css";

const Notifications = () => {
  const [readFlag, setReadFlag] = useState(false);

  const dispatch = useDispatch();
  // const user = useSelector((state) => state.authReducer.signIn);
  // const authToken = user.user.access;
  // const isSignedIn = user.isSignedIn;

  const signedInCreds = useSelector(selector.signedInCreds);
  const authToken = signedInCreds.user.access;
  const isSignedIn = signedInCreds.isSignedIn;

  useEffect(() => {
    console.log("in notifications");
    if (!isSignedIn) {
      return <Redirect to="/signIn" />;
    }
    if (isSignedIn) {
      localStorage.setItem("refreshPath", "/notifications");
    }

    dispatch(actions.getNotification(authToken));
  }, [authToken, readFlag]);

  const notifications = useSelector(selector.notifications);

  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }
  return (
    <div className="notifications-container">
      <ul className="notifications-list">
        {notifications.map((notification) => {
          return (
            <li className="notification" key={notification.id}>
              <a
                to="#"
                className={
                  notification.is_read === true
                    ? "read-notification"
                    : "unread-notification"
                }
              >
                {notification.notification}
              </a>
              <a
                onClick={(e) => {
                  hooks.masrkAsRead(
                    e,
                    dispatch,
                    authToken,
                    notification.id,
                    setReadFlag
                  );
                }}
                notificationId={notification.id}
                className={
                  notification.is_read === false
                    ? "mark-read"
                    : "marked-already"
                }
              >
                mark as read
              </a>
              <hr className="notification-seperator"></hr>
            </li>
            // {/* <hr className="notification-seperator"></hr> */}
          );
        })}
      </ul>
    </div>
  );
};

export default Notifications;
