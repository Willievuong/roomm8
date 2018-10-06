import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'
import './App.css';
import Navbar from './Components/Navbar';
import Main from './Components/Main';


class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Navbar/>
          <Main/>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
