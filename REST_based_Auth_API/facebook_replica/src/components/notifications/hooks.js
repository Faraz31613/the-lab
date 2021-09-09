import * as actions from "modules/notification/action";

export const masrkAsRead = (
  e,
  dispatch,
  authToken,
  notificationId,
  setReadFlag
) => {
  dispatch(
    actions.markAsRead({
      authToken,
      id: notificationId,
    })
  );
  setReadFlag(true);
};
