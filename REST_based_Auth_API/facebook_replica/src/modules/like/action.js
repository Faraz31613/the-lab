import * as actionTypes from "./type";

export const like = (createLikeCred) => ({
  type: actionTypes.LIKE,
  payload: createLikeCred,
});

export const getLike = (likedPostOrCommentCred) => ({
  type: actionTypes.GET_LIKE,
  payload: likedPostOrCommentCred,
});

export const showLike = (likes) => ({
  type: actionTypes.SHOW_LIKE,
  payload: likes,
});
