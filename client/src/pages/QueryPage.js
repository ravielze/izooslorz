import "../App.css";
import React from "react";
import DocuQuery from "../components/Documents";

const QueryPage = () => {
    return (
      <div className = "Container">
        <div className="QueryPage-Head">
        </div>
        <div className="QueryPage-Body">
          <DocuQuery/>
        </div>
      </div>
    );
  };
  export default QueryPage