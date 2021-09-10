import React, { useState } from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

import * as selector from "components/selector";
import { MenuItems } from "./menuItems";

import "./navbar.css";

const Navbar = () => {
  const [menuItemClicked, setMenuItemClicked] = useState(false);

  const isSignedIn = useSelector(selector.isSignedIn);

  return (
    <nav className="navbar-items">
      <h1 className="navbar-logo">
        <i className="fab fa-facebook-square"></i> Facebook Replica
      </h1>
      <div
        className="menu-icon"
        onClick={() => {
          setMenuItemClicked(!menuItemClicked);
        }}
      >
        <i className={menuItemClicked ? "fas fa-times" : "fas fa-bars"}></i>
      </div>
      <ul className={menuItemClicked ? "nav-menu active" : "nav-menu"}>
        {MenuItems.map((item, index) => {
          if (isSignedIn === true && item.className === "nav-links") {
            return (
              <li key={index}>
                <Link className={item.className} to={item.url}>
                  {item.title}
                </Link>
              </li>
            );
          } else if (
            isSignedIn === false &&
            item.className === "nav-btn-links"
          ) {
            return (
              <li key={index}>
                <Link className={item.className} to={item.url}>
                  {item.title}
                </Link>
              </li>
            );
          }
        })}
      </ul>
    </nav>
  );
};

export default Navbar;
