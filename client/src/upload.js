import axios from 'axios';
import React,{Component} from 'react'; 
  
import Image from "./img/logo.jpg";

class upload extends Component { 
   
    state = { 
  
      // Initially, no file is selected 
      selectedFile: null
    }; 
     
    // On file select (from the pop up) 
    onFileChange = event => { 
        console.log(event.target);
      // Update the state 
      this.setState({ selectedFile: event.target.files[0] }); 
     
    }; 
     
    // On file upload (click the upload button) 
    onFileUpload = () => { 
     
      // Create an object of formData 
      const formData = new FormData(); 
     
      // Update the formData object 
      formData.append( 
        "myFile", 
        this.state.selectedFile, 
        this.state.selectedFile.name 
      ); 
     
      // Details of the uploaded file 
      console.log(this.state.selectedFile); 
     
      // Request made to the backend api 
      // Send formData object 
      axios.post("api/uploadfile", formData); 
    }; 
     
    // File content to be displayed after 
    // file upload is complete 
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
            <a href="/home">
                <button>
                    Back    
                </button>
            </a>
          </div> 
        ); 
      } else { 
        return ( 
          <div> 
            <br /> 
            <h4>Pilih file dulu, baru tekan tombol upload.</h4> 
            <a href="/home">
                <button>
                    Back    
                </button>
            </a>
          </div> 
        ); 
      } 
    }; 
     
    render() { 
     
      return ( 
        <div> 
            <img src={Image} class="App-logo" alt="">
            </img>
            <div>
                <h3> 
                Upload file disini! 
                </h3> 
                <div> 
                    <input type="file" onChange={this.onFileChange} /> 
                    <button onClick={this.onFileUpload}> 
                        Upload!
                    </button> 
                </div> 
            </div>
          {this.fileData()} 
        </div> 
      ); 
    } 
  } 
  
  export default upload;