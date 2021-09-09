//for navidator,navbar
export const isSignedIn = (state) => state.authReducer.signIn.isSignedIn;

//for signUp
export const isSignedUpErrorMessage = (state) => state.authReducer.message;
//for signIn
export const isSignedInErrorMessage = (state) => state.authReducer.message;

//for home,notifications
export const signedInCreds = (state) => state.authReducer.signIn;

//for home
export const posts = (state) => state.postReducer.posts;
export const signedInUserLikes = (state) => state.likeReducer.likes;
export const comments = (state) => state.commentReducer.comments;

//for notifications
export const notifications = (state) => state.notificationReducer.notifications;
