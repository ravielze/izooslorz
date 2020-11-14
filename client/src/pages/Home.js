import "../App.css";
import React from "react";

import Image from "../img/logo.jpg";
import SearchBar from "../components/SearchBar.js";
import Button from "@material-ui/core/Button";
import ControlledOpenSelect from "../components/DropDown.js";
import NavBar from "../components/NavBar.js";

const Home = () => {
  return (
    <div>
      <NavBar/>
      <p className="HelloUserText" align="right">
        Welcome, user!
      </p>
      <header className="App-header">
        <img src={Image} class="App-logo" alt=""></img>
        <p className="SearchComponents">
          <SearchBar />
          <ControlledOpenSelect />
        </p>
      </header>
    </div>
  );
};
export default Home;