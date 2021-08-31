import React, { useState } from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

import { MenuItems } from "./menuItems";

import "./navbar.css";

const Navbar = () => {
  const [menuItemClicked, setMenuItemClicked] = useState(false);

  const handleClick = () => {
    setMenuItemClicked(!menuItemClicked);
  };

  const isSignedIn = useSelector(
    (state) => state.authReducer.signIn["isSignedIn"]
  );

  return (
    <nav className="navbar-items">
      <h1 className="navbar-logo">
        <i className="fab fa-facebook-square"></i> Facebook Replica
      </h1>
      <div className="menu-icon" onClick={handleClick}>
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
