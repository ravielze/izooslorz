import axios from "axios";
import React, { Component } from "react";

import Image from "../img/logo.jpg";
import NavBar from "../components/NavBar.js";
import ControlledOpenSelect from "../components/DropDown.js";

class upload extends Component {
  state = {
    selectedFile: null,
    lang: "bahasa_indonesia",
  };

  onFileChange = (event) => {
    console.log(event.target);
    this.setState({ ...this.state, selectedFile: event.target.files[0] });
  };

  handleChange = (lang) => {
    this.setState({ ...this.state, lang:lang});
  }

  onFileUpload = () => {
    const formData = new FormData();

    formData.append(
      "file",
      this.state.selectedFile,
      this.state.selectedFile.name
    );

    formData.append(
      "lang",
      this.state.lang,
    )

    console.log(this.state.lang);
    console.log(this.state.selectedFile);

    axios.post("http://localhost:5000/upload", formData);
  };

  fileData = () => {
    if (this.state.selectedFile) {
      return (
        <div>
          <h2>File Details:</h2>
          <p>File Name: {this.state.selectedFile.name}</p>
          <p>File Type: {this.state.selectedFile.type}</p>
          <p>
            Last Modified:{" "}
            {this.state.selectedFile.lastModifiedDate.toDateString()}
          </p>
          <ControlledOpenSelect value={this.state.lang} handleChange={this.handleChange} />
        </div>
      );
    } else {
      return (
        <div>
          <br />
          <h4>Pilih file dulu, baru tekan tombol upload.</h4>
          <ControlledOpenSelect value={this.state.lang} handleChange={this.handleChange}/>
        </div>
      );
    }
  };

  render() {
    return (
      <div>
        <NavBar/>
        <div className="container">
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <img src={Image} class="App-logo" alt=""></img>
          <div>
            <h3>Upload file disini!</h3>
            <div>
              <input type="file" onChange={this.onFileChange} />
              <button onClick={this.onFileUpload}>Upload!</button>
            </div>
          </div>
          {this.fileData()}
        </div>
      </div>
    );
  }
}
export default upload;
