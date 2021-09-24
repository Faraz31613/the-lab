import React, { useEffect } from "react";
import { useSelector } from "react-redux";

import * as selector from "modules/selector";
import * as hooks from "modules/hooks";

import Post from "components/post";

import "./home.css";

const Home = () => {
  const signedInCreds = useSelector(selector.signedInCreds);
  const authToken = signedInCreds.user.access;
  const isSignedIn = signedInCreds.isSignedIn;

  const posts = useSelector(selector.posts);

  const getPosts = hooks.useGetPosts(authToken);
  
  useEffect(() => {
    if (isSignedIn) {
      localStorage.setItem("refreshPath", "/");
    }

    getPosts();
  }, [authToken]);

  return (
    <div className="home-container">
      <h3>
        <i className="fas fa-house-user"></i> Home
      </h3>
      <div className="home-posts">
        {posts.map((post) => {
          return <Post post={post} key={post.id} />;
        })}
      </div>
    </div>
  );
};

export default Home;
