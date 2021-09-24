import http from "httpCommon";

export async function like(createLikeCred) {
  try {
    return await http.post("/like/", createLikeCred["likeCred"], {
      headers: { Authorization: `Bearer ${createLikeCred["authToken"]}` },
    });
  } catch (error) {
    return error.response;
  }
}

export async function unlike(deleteLikeCred) {
  try {
    return await http.delete("/like/", {
      params: { id: deleteLikeCred["post"] },
      headers: { Authorization: `Bearer ${deleteLikeCred["authToken"]}` },
    });
  } catch (error) {
    return error.response;
  }
}
