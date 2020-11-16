import "../App.css";
import React, {useState} from "react";
import axios from 'axios';
import Image from "../img/logo.jpg";
import SearchBar from "../components/SearchBar.js";
import ControlledOpenSelect from "../components/DropDown.js";
import NavBar from "../components/NavBar.js";
import { useHistory } from 'react-router-dom';

const Home = () => {
  const history = useHistory()

  const handleKeyPress = (ev) => {
    if (ev.key === "Enter"){
      history.push({pathname: `/QueryPage/${search}/${lang}`, query: search});
    }
  }

  const [search, setSearch] = useState("");
  const [lang, setLang] = useState("bahasa_indonesia");

  return (
    <div>
      <NavBar/>
      <header className="App-header">
        <img src={Image} class="App-logo" alt=""></img>
        <p className="SearchComponents">
          <SearchBar value={search} handleChange={setSearch} handleKeyPress={handleKeyPress}/>
          <ControlledOpenSelect value={lang} handleChange={setLang}/>
        </p>
      </header>
    </div>
  );
};
export default Home;