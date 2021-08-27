import { store } from "react-notifications-component";

const notification = {
  title: "title!",
  message: "message",
  type: "success",
  insert: "top",
  container: "top-right",
  animationIn: ["animate__animated", "animate__fadeIn"],
  animationOut: ["animate__animated", "animate__fadeOut"],
  dismiss: {
    duration: 2500,
    onScreen: true,
    pauseOnHover: true,
  },
};

export const notify = (title, message, type) => {
  store.addNotification({
    ...notification,
    title,
    message,
    type,
  });
};
