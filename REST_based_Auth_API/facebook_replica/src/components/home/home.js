import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

import * as postActions from "modules/post/action";
import * as likeActions from "modules/like/action";
import Like from "components/like";

import "./home.css";

const Home = () => {
  const user = useSelector((state) => state.authReducer.signIn);
  const authToken = user.user.access;
  const isSignedIn = user.isSignedIn;

  const dispatch = useDispatch();
  useEffect(() => {
    if (!isSignedIn) {
      return <Redirect to="/signIn" />;
    }
    if (isSignedIn) {
      localStorage.setItem("user", encodeURI(JSON.stringify(user)));
      localStorage.setItem("refreshPath", "/");
    }

    dispatch(postActions.getPosts(authToken));
  }, authToken);

  const posts = useSelector((state) => state.postReducer.posts);

  if (!isSignedIn) {
    return <Redirect to="/signIn" />;
  }

  return (
    <div className="home-container">
      <h3>
        <i className="fas fa-house-user"></i> Home
      </h3>
      <div className="home-posts">
        {posts.map((post, index) => {
          return (
            <>
              <section className="post-section" key={index} postId={post.id}>
                <header className="post-author" userId={post.user.id}>
                  <i className="fas fa-user"></i> {post.user.first_name}{" "}
                  {post.user.last_name}
                </header>
                <p className="post-text">{post.text_post}</p>
                <Like postId={post.id} userId={user.user.id}></Like>
                <button className="post-comment-btn">
                  <i className="far fa-comment"></i> comment
                </button>
                <button className="post-share-btn">
                  <i className="fas fa-share"></i> share
                </button>
              </section>
            </>
          );
        })}
      </div>
    </div>
  );
};

export default Home;
