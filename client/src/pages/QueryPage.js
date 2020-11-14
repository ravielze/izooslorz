import "../App.css";
import React from "react";
import DocuQuery from "../components/Documents";
import Table from "../components/TermTable";

const QueryPage = () => {
    return (
      <div className = "Container">
        <div className="QueryPage-Head">
        </div>
        <div className="QueryPage-Body">
          <DocuQuery/>
          <Table />
        </div>
      </div>
    );
  };
  export default QueryPage