import http from "httpCommon";

export const request = (orginalconfig) => {
  const { auth, ...config } = orginalconfig;
  const signedInUserCred = JSON.parse(decodeURI(localStorage.getItem("user")));
  const authToken = signedInUserCred.user.access;
  const headers = config.auth
    ? { ...config.headers, Authorization: `Bearer: ${authToken}` }
    : config.headers;
  return http.request({ headers, ...config });
};
