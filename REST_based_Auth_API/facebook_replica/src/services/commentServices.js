import http from "httpCommon";
import { request } from "./request";

// const request = (orginalconfig) => {

//   const {auth, ...config} = orginalconfig;
//   const authToken = localStorage.get("key");
//   const headers = config.auth 
//       ? {...config.headers, Authorization: `Bearer: ${authToken}`}
//       : config.headers;
//   return http.request({headers, ...config});
// }

// export const exampleRequest = async(comment) => {
//   try {
//     return await request({
//      url: "/comment/", 
//      auth: true,
//      method: "get",
//      data: comment,
//      headers: { accept_confi: "asda" }
//     });
//   } catch (error) {
//     return error.response;
//   }

// }

export async function addComment(commentCred) {
  // try {
  //   return await request({
  //    url: "/comment/", 
  //    auth: true,
  //    method: "post",
  //    data: commentCred["comment"],
  //    headers: {}
  //   });
  // } catch (error) {
  //   return error.response;
  // }

  try {
    return await http.post("/comment/", commentCred["comment"], {
      headers: { Authorization: `Bearer ${commentCred["authToken"]}` },
    });
  } catch (error) {
    return error.response;
  }
}

export async function getComments(commentedPostCreds) {
  try {
    return await http.get("/comment/", {
      params: { post: commentedPostCreds["post"] },
      headers: { Authorization: `Bearer ${commentedPostCreds["authToken"]}` },
    });
  } catch (error) {
    return error.response;
  }
}
