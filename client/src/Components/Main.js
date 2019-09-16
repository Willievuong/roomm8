import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'
import LandingPage from './LandingPage'
import Login from './Login'
import SignUp from './SignUp'
import ErrorPage from './404Page'

class Main extends Component {
  render(){
    return(
      <main className="Site-body">
          <Switch>
            <Route exact path='/' component={LandingPage}/>
            <Route exact path='/Home' component={LandingPage}/>
            {/* <Route path='/SignUp' component={SignUp}/>
            <Route path='/Login' component={Login}/> */}
            <Route path='*' component={ErrorPage}/>
          </Switch>
      </main>
    );
  }
}

export default Main