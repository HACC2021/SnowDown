import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Basetemplate from './Router/BaseRoute'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route to=''>
            <Basetemplate/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
