import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'
import './App.css';
import Navbar from './Components/HeaderComponents/Navbar';
import Main from './Components/Main';
import Footer from './Components/FooterComponents/Footer'
import { createMuiTheme, MuiThemeProvider } from '@material-ui/core/styles';

const theme = createMuiTheme({
  palette: {
    primary: {
      light: '#0097a7', //
      main: '#00838f', //
      dark: '#006064', //
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#1de9b6',
      dark: '#ba000d',
      contrastText: '#000',
    },
  },
});

class App extends Component {
  render() {
    return (
      <MuiThemeProvider theme={theme} >
      <BrowserRouter>
        <div className="App">
          <Navbar/>
          <Main/>
          <Footer/>
        </div>
      </BrowserRouter>
      </MuiThemeProvider>
    );
  }
}

export default App;
