import React, { Component } from 'react'
import FacebookLogin from 'react-facebook-login'

const axios = require('axios');
axios.defaults.headers.post['Content-Type'] = 'application/JSON';
const backendRoutes = 'http://localhost:5000/'

const styles = {

}

class Login extends Component {
  
  verification = (res) => {
    
  }
  
  responseFacebook = (res) => {
    axios.post(URL + "users/" + "login", {res})
    .then( (res) => {
      //If Successful
      
      //Else Not Succesful 
    }).catch((error) =>{
      console.log(error);
    })
  }
  
  render(){
    return(
      <div>
        <form>
          <label>
            Email:
            <input type="text" name="email"/>
            Password:
            <input type="text" name="password"/>
            <button> Submit </button> 
            <button> Register </button>
          </label>
        </form>
        <FacebookLogin
                appId="1783496798419122"
                autoLoad={true}
                cookies={true}
                fields="name,email,picture"
				callback={this.responseFacebook}
			/>
      </div>
    );
  }
}

export default Login