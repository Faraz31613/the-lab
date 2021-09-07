import * as actionTypes from "./type";

//saga actions
export const getPosts = (data) => ({
  type: actionTypes.GET_POSTS,
  payload: data,
});

//reducer actions
export const showPosts = (posts) => ({
  type: actionTypes.SHOW_POSTS,
  payload: posts,
});
