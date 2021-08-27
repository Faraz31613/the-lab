import http from "httpCommon";

export async function registerUser(userCred) {
  try {
    return await http.post("/register/", userCred);
  } catch (error) {
    return error.response;
  }
}

export async function signIn(userCred) {
  try {
    return await http.post("/api/token/", userCred);
  } catch (error) {
    return error.response;
  }
}
