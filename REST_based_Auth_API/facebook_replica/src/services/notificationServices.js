import http from "httpCommon";

export async function getNotification(authToken) {
  return await http.get("/show_notifications/", {
    headers: { Authorization: `Bearer ${authToken}` },
  });
}

export async function markAsRead(data) {
  console.log("in services", data["id"]);
  return await http.put(
    "/show_notifications/",
    { id: data["id"] },
    { headers: { Authorization: `Bearer ${data["authToken"]}` } }
  );
}
