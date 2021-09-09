import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as postActions from "modules/post/action";
import * as likeActions from "modules/like/action";
import * as selector from "components/selector";
// import * as navigator from "components/authNavigation"

import Post from "./post";

import "./home.css";

const Home = () => {
  const [addCommentFlag, setAddCommentFlag] = useState(false);
  const [postIdForComment, setPostIdForComment] = useState();

  const signedInCreds = useSelector(selector.signedInCreds);
  const authToken = signedInCreds.user.access;
  const isSignedIn = signedInCreds.isSignedIn;

  const dispatch = useDispatch();

  const posts = useSelector(selector.posts);

  useEffect(() => {
    if (!isSignedIn) {
      return <Redirect to="/signIn" />;
    }
    if (isSignedIn) {
      localStorage.setItem("user", encodeURI(JSON.stringify(signedInCreds)));
      localStorage.setItem("refreshPath", "/");
    }

    dispatch(postActions.getPosts(authToken));
    dispatch(likeActions.getSignedInUserLikes(authToken));
  }, [authToken]);

  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return (
    <div className="home-container">
      <h3>
        <i className="fas fa-house-user"></i> Home
      </h3>
      <div className="home-posts">
        {posts.map((post) => {
          return (
            <Post
              addCommentFlag={addCommentFlag}
              postIdForComment={postIdForComment}
              setAddCommentFlag={setAddCommentFlag}
              setPostIdForComment={setPostIdForComment}
              post={post}
              key = {post.id}
            />
          );
        })}
      </div>
    </div>
  );
};

export default Home;
