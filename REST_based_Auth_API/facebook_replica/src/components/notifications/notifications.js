import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as actions from "modules/notification/action";

import "./notifications.css";

const Notifications = () => {
  const [readFlag, setReadFlag] = useState(false);

  const dispatch = useDispatch();
  const user = useSelector((state) => state.authReducer.signIn);
  const authToken = user.user.access;
  const isSignedIn = user.isSignedIn;

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

  const handleMarkRead = (event) => {
    dispatch(
      actions.markAsRead({
        authToken: authToken,
        id: event.target.getAttribute("notificationId"),
      })
    );
    setReadFlag(true);
  };

  const notifications = useSelector(
    (state) => state.notificationReducer.notifications
  );
  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }
  return (
    <div className="notifications-container">
      <ul className="notifications-list">
        {notifications.map((notification, index) => {
          return (
            <>
              <li className="notification" key={index}>
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
                  onClick={handleMarkRead}
                  notificationId={notification.id}
                  className={
                    notification.is_read === false
                      ? "mark-read"
                      : "marked-already"
                  }
                >
                  mark as read
                </a>
              </li>
              <hr className="notification-seperator"></hr>
            </>
          );
        })}
      </ul>
    </div>
  );
};

export default Notifications;
