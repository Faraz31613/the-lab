import { useSelector } from "react-redux";
import http from "httpCommon";

export async function getNotification(authToken) {
  return await http.get("/show_notifications/", {
    headers: { Authorization: `Bearer ${authToken}` },
  });
}

export async function markAsRead(data) {
  return await http.put(
    "/show_notifications/",
    { id: data["id"] },
    { headers: { Authorization: `Bearer ${data["authToken"]}` } }
  );
}
