import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'
import LandingPage from './LandingPage'
import Login from './Login'
import SignUp from './SignUp'
import ErrorPage from './404Page'
import { createMuiTheme, MuiThemeProvider } from '@material-ui/core/styles';

const theme = createMuiTheme({
  palette: {
    primary: {
      light: '#4caf50', //green
      main: '#ffca28', //yellow
      dark: '#cddc39', //lime
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#f44336',
      dark: '#ba000d',
      contrastText: '#000',
    },
  },
});

class Main extends Component {
  render(){
    return(
      <MuiThemeProvider theme={theme} >
      <main className="Site-body">
          <Switch>
            <Route exact path='/' component={LandingPage}/>
            <Route exact path='/Home' component={LandingPage}/>
            <Route path='/SignUp' component={SignUp}/>
            <Route path='/Login' component={Login}/>
            <Route path='*' component={ErrorPage}/>
          </Switch>
      </main>
      </MuiThemeProvider>
    );
  }
}

export default Main