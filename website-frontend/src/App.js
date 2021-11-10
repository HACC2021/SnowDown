import React from 'react';
import {
  HashRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Basetemplate from './Router/BaseRoute';
import Usertemplate from './Router/UserRoute';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path='/User'>
            <Usertemplate/>
          </Route>
          <Route path='/'>
            <Basetemplate/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
