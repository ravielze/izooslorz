import "../App.css";
import React from 'react';
import axios from 'axios';
import DocuQuery from "../components/Documents";
import Table from "../components/TermTable";
import { useEffect } from "react";
import NavBar from "../components/NavBar.js";
import SearchBar from "../components/SearchBar.js";
import SearchIcon from "@material-ui/icons/Search";
import Image from "../img/logo.jpg";

export default class QueryPage extends React.Component {
  state = {
    name: this.props.location.query,
    data: [],
    termtable: [{documents: []}],
  }
  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    const search = {
      'keyword': this.state.name,
      'lang': "en"
    };
    axios.post(`http://localhost:5000/search`, search)
      .then(res => {
        console.log(res.data.data);
        this.setState({data: res.data.data});
        this.setState({termtable: res.data.termtable})
      })
  }
  render() {
    return (
      <div>
        <NavBar />
        <div className="Container">
          <div className="QueryPage-Head">
            <img src={Image} class="App-logo" alt="" style={{width: 200, marginRight: 50}}></img>
            <form onSubmit={this.handleSubmit} style={{display: "flex", justifyContent: "row", alignItems: "center"}}>
              <input type="text" name="name" onChange={this.handleChange} style={{height: 40, borderRadius: 10}}/>
              <button type="submit" style={{height: 40}}>
                <SearchIcon />
              </button>
            </form>
          </div>
          <div className="QueryPage-Body">
            <DocuQuery data = {this.state.data}/>
            <Table data = {this.state.termtable}/>
          </div>
        </div>
      </div>
    )
  }
}
