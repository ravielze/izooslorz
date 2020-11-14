import './App.css';
import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Upload from "./pages/upload.js";
import Home from "./pages/Home.js";
import AboutUs from "./pages/AboutUsPage.js";
import QueryPage from "./pages/QueryPage.js";
import WebScraping from "./pages/WebScraping.js";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path = "/" component={Home}/>
          <Route path = "/upload" component={Upload}/> 
          <Route path = "/home" component={Home}/>
          <Route path = "/aboutus" component={AboutUs}/>
          <Route path = "/QueryPage" component={QueryPage}/>
          <Route path = "/WebScraping" component={WebScraping}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
