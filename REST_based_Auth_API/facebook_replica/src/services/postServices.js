import http from "httpCommon";

export async function getPosts(authToken) {
  return await http.get("/home/", {
    headers: { Authorization: `Bearer ${authToken}` },
  });
}
