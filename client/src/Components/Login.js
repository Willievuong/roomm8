import React, { Component } from 'react';

const styles = {

}

class Login extends Component {
  render(){
    return(
      <div>
        <form>
          <label>
            Email:
            <input type="text" name="email"/>
            Password:
            <input type="text" name="password"/>
            {/*Need to work on action */}
            <button> Submit </button> 
            <button> Register </button>
          </label>
        </form>
      </div>
    );
  }
}

export default Login