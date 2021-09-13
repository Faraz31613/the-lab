import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import * as actions from "modules/notification/action";
import * as selector from "modules/selector";
import * as hooks from "modules/hooks";

import "./notifications.css";

const Notifications = () => {
  const signedInCreds = useSelector(selector.signedInCreds);
  const authToken = signedInCreds.user.access;
  const isSignedIn = signedInCreds.isSignedIn;

  const markAsRead = hooks.useMarkAsRead();
  const getNotification = hooks.useGetNotification(authToken);

  useEffect(() => {
    if (isSignedIn) {
      localStorage.setItem("refreshPath", "/notifications");
    }

    getNotification();
  }, [authToken]);

  const notifications = useSelector(selector.notifications);

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
                onClick={() => {
                  markAsRead(authToken, notification.id);
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
