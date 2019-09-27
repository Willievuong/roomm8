import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'
import './App.css';
import Navbar from './Components/HeaderComponents/Navbar';
import Main from './Components/Main';
import Footer from './Components/FooterComponents/Footer'
import { createMuiTheme, MuiThemeProvider } from "@material-ui/core";
import { ThemeProvider } from '@material-ui/styles';

const theme = createMuiTheme()

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Navbar/>
          <MuiThemeProvider theme={theme}>
            <Main/>
          </MuiThemeProvider>
          <Footer/>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
