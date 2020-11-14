import "../App.css";
import React from "react";
import DocuQuery from "../components/Documents";
import NavBar from "../components/NavBar.js";
import Table from "../components/TermTable";

const QueryPage = () => {
  return (
    <div>
      <NavBar />
      <div className="Container">
        <div className="QueryPage-Head"></div>
        <div className="QueryPage-Body">
          <DocuQuery/>
          <Table />
        </div>
      </div>
    </div>
  );
};
export default QueryPage;
