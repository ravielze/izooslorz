import './App.css';
import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Upload from "./upload.js";
import Home from "./Home.js";
import AboutUs from "./AboutUsPage.js"

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path = "/" component={Home}/>
          <Route path = "/upload" component={Upload}/> 
          <Route path = "/home" component={Home}/>
          <Route path = "/aboutus" component={AboutUs}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
