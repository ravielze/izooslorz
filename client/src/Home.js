import './App.css';
import React from "react";

import Image from "./img/logo.jpg";
import SearchBar from "./SearchBar.js";

const Home = () => {
    
    return(
    <div>
        <p className="HelloUserText" align="right">
        Welcome, user!
      </p>
      <header className="App-header">
        <img src={Image} class="App-logo" alt="">
        </img>
        <SearchBar/>
      <p>
        <a href="">Bahasa Indonesia</a> | <a href="">Bahasa Inggris</a>
      </p>
      <a href = "/upload">
        <button>Upload File</button>
      </a>
      <p className="AboutUs">
        <a href="/AboutUs">About us</a>
      </p>
      </header>
    </div>
    )
} 
export default Home

