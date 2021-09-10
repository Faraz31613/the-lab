//for navidator,navbar
export const isSignedIn = (state) => state.auth.signIn.isSignedIn;

//for signUp
export const isSignedUpErrorMessage = (state) => state.auth.message;
//for signIn
export const isSignedInErrorMessage = (state) => state.auth.message;

//for home,notifications
export const signedInCreds = (state) => state.auth.signIn;

//for home
export const posts = (state) => state.post.posts;
export const signedInUserLikes = (state) => state.like.likes;
export const comments = (state) => state.comment.comments;

//for notifications
export const notifications = (state) => state.notification.notifications;
