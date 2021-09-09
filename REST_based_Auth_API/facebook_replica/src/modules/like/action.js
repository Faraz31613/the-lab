import * as actionTypes from "./type";

//saga actions
export const like = (createLikeCred) => ({
  type: actionTypes.LIKE,
  payload: createLikeCred,
});

export const getSignedInUserLikes = (authToken) => ({
  type: actionTypes.GET_SIGNEDIN_USER_LIKES,
  payload: authToken,
});

export const unlike = (deleteLikeCred) => ({
  type: actionTypes.UNLIKE,
  payload: deleteLikeCred,
});


//reducer actions
export const showSignedInUserLikes = (likes) => ({
  type: actionTypes.SHOW_SIGNEDIN_USER_LIKES,
  payload: likes,
});
