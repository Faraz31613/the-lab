import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import * as actions from "modules/notification/action";

import "./notifications.css";

const Notifications = () => {
  const [readFlag, setReadFlag] = useState(false);

  const dispatch = useDispatch();
  const signedInUser = useSelector((state) => state.authReducer.signIn["user"]);
  const authToken = signedInUser["access"];

  useEffect(
    () => {
      dispatch(actions.getNotification(authToken));
    },
    [authToken],
    readFlag
  );

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
