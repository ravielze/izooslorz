import "../App.css";
import React from "react";
import DocuQuery from "../components/Documents";
import NavBar from "../components/NavBar.js";

const QueryPage = () => {
  return (
    <div>
      <NavBar />
      <div className="Container">
        <div className="QueryPage-Head"></div>
        <div className="QueryPage-Body">
          <DocuQuery />
        </div>
      </div>
    </div>
  );
};
export default QueryPage;
