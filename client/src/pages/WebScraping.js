import "../App.css";
import React from "react";
import NavBar from "../components/NavBar.js";
import LinkScraping from "../components/LinkScraping.js";

import Image from "../img/logo.jpg";

const WebScraping = () => {
  return (
    <div>
      <NavBar />
      <div className="App-header">
        <img src={Image} />
        <br/>
        <LinkScraping />
      </div>
    </div>
  );
};
export default WebScraping;
