import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'
import LandingPage from './LandingPage'

class Main extends Component {
  render(){
    return(
      <main className="Site-body">
          <Switch>
            <Route exact path='/' component={LandingPage}/>
            <Route exact path='/Home' component={LandingPage}/>
            {/* <Route path='/SignUp' component={}/>
            <Route path='/Login' component={}/>
            <Route path='*' component={}/> */}
          </Switch>
      </main>
    );
  }
}

export default Main