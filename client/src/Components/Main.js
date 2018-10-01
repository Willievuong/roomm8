import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'

class Main extends Component {
  render(){
    return(
      <main className="Site-body">
          <Switch>
            <Route exact path='/' component={}/>
            <Route exact path='/Home' component={}/>
            <Route path='/SignUp' component={}/>
            <Route path='/Login' component={}/>
            <Route path='*' component={}/>
          </Switch>
      </main>
    );
  }
}

export default Main