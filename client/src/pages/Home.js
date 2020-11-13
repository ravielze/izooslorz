import "../App.css";
import React from "react";

import Image from "../img/logo.jpg";
import SearchBar from "../components/SearchBar.js";
import Button from "@material-ui/core/Button";
import ControlledOpenSelect from "../components/DropDown.js";

const Home = () => {
  return (
    <div>
      <p className="HelloUserText" align="right">
        Welcome, user!
      </p>
      <header className="App-header">
        <img src={Image} class="App-logo" alt=""></img>
        <p className="SearchComponents">
          <SearchBar />
          <ControlledOpenSelect />
        </p>
        <p className="AboutUs">
          <a href="/upload">
            <Button variant="outlined" color="primary">
              Upload
            </Button>
          </a>
          <a href="/AboutUs">
            <Button variant="outlined" color="primary">
              About Us
            </Button>
          </a>
        </p>
      </header>
    </div>
  );
};
export default Home;