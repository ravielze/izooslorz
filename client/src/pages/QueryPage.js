import "../App.css";
import React, {useState} from "react";
import DocuQuery from "../components/Documents";
import NavBar from "../components/NavBar.js";
import Table from "../components/TermTable";
import { useEffect } from "react";
import axios from "axios";

const lang = {
    "bahasa_indonesia" : "id",
    "english" : "en"
}

const QueryPage = (props) => {
  const [data,setData] = useState([]);
  useEffect(() => {
      const lang_converted = lang[props.match.params.lang]
      const search = props.match.params.query
    axios
    .post(`localhost:5000/search?keyword=${search}&lang=${lang_converted}`)
    .then((res) => {
        res = res.data.data
        setData(res)
    })

  });
  return (
    <div>
      <NavBar />
      <div className="Container">
        <div className="QueryPage-Head"></div>
        <div className="QueryPage-Body">
          <DocuQuery data={data} />
          <Table />
        </div>
      </div>
    </div>
  );
};
export default QueryPage;
