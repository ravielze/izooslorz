import "../App.css";
import React, { useState } from "react";
import NavBar from "../components/NavBar.js";
import LinkScraping from "../components/LinkScraping.js";
import ControlledOpenSelect from "../components/DropDown.js";

import Image from "../img/logo.jpg";
import axios from "axios";

const WebScraping = () => {
  const [search, setSearch] = useState("");
  const [lang, setLang] = useState("bahasa_indonesia");

  const handleKeyPress = (ev) => {
    if (ev.key === "Enter") {
      const formData = new FormData();

      formData.append("url", search);

      formData.append("lang", lang);

      console.log(search);
      console.log(lang);
      axios.post("http://localhost:5000/webscraping", formData);
    }
  };

  return (
    <div>
      <NavBar />
      <div className="App-header">
        <img src={Image} />
        <br />
        <LinkScraping
          value={search}
          handleChange={setSearch}
          handleKeyPress={handleKeyPress}
        />
        <ControlledOpenSelect value={lang} handleChange={setLang} />
      </div>
    </div>
  );
};
export default WebScraping;
