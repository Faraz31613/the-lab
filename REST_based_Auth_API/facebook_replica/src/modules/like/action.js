import * as actionTypes from "./type";

//saga actions
export const like = (createLikeCred) => ({
  type: actionTypes.LIKE,
  payload: createLikeCred,
});

export const unlike = (deleteLikeCred) => ({
  type: actionTypes.UNLIKE,
  payload: deleteLikeCred,
});
