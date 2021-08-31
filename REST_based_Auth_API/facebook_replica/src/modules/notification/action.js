import * as actionTypes from "./type";

//saga actions
export const getNotification = (data) => ({
  type: actionTypes.GET_NOTIFICAIONS,
  payload: data,
});

export const markAsRead = (data) => ({
  type: actionTypes.MARK_AS_READ,
  payload: data,
});

//reducer actions
export const showNotifications = (notifications) => ({
  type: actionTypes.SHOW_NOTIFICATIONS,
  payload: notifications,
});
