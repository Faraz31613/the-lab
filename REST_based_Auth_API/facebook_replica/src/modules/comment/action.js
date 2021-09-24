import * as actionTypes from "./type";

//saga actions
export const addComment = (commentCreds) => ({
  type: actionTypes.ADD_COMMENT,
  payload: commentCreds,
});

export const getComments = (commentedPostCreds) => ({
  type: actionTypes.GET_COMMENTS,
  payload: commentedPostCreds,
});

//reducer actions
export const showComments = (comments) => ({
  type: actionTypes.SHOW_COMMENTS,
  payload: comments,
});
