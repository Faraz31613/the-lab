import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as actions from "modules/notification/action";
import * as selector from "components/selector";
import * as hooks from "components/hooks";

import "./notifications.css";

const Notifications = () => {
  const [readFlag, setReadFlag] = useState(false);
  const [notificationId, setNotificationId] = useState(null);

  const dispatch = useDispatch();

  const signedInCreds = useSelector(selector.signedInCreds);
  const authToken = signedInCreds.user.access;
  const isSignedIn = signedInCreds.isSignedIn;

  const markAsRead = hooks.useMarkAsRead(authToken, notificationId);

  useEffect(() => {
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
                  setNotificationId(notification.id);
                  markAsRead(authToken, notificationId);
                  setReadFlag(true);
                }}
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
          );
        })}
      </ul>
    </div>
  );
};

export default Notifications;
