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

export async function getlikes(likedPostOrCommentCred) {
  try {
    return await http.get("/like/", {
      params: {
        post: likedPostOrCommentCred["likedCred"].post,
        comment: likedPostOrCommentCred["likedCred"].comment,
      },
      headers: {
        Authorization: `Bearer ${likedPostOrCommentCred["authToken"]}`,
      },
    });
  } catch (error) {
    return error.response;
  }
}
