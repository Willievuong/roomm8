import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import './css/landing.css'
const axios = require('axios')

const BACKEND_URL = "http://localhost:8000/"

class LandingPage extends Component { 
  constructor(props){
    super(props);
    
  }

  async loadData(){
    this.state.user = (await axios.get(BACKEND_URL + "profile/")).data
    this.state.room = (await axios.get(BACKEND_URL + "room/")).data
    console.log(this.state.user)
    console.log("HELLO")
    // this.state.task = (await axios.get()).data

  }
  
  componentDidMount(){
    this.loadData()
  }

  render(){
  
    return(
      <div className="landing">
        <Grid container spacing={8}>
          <Grid item xs={12}>
            <Paper className="paper"> 
              <Typography variant="title" component="h3">
                Kitchen
              </Typography>
              <Typography component="p">
                Paper can be used to build surface or other elements for your application.
              </Typography>
            </Paper>
          </Grid>
          <Grid item xs={6}>
            <Paper className="paper"> 
              Janet
            </Paper>
          </Grid>
          <Grid item xs={6}>
            <Paper className="paper"> 
              <Button variant="contained" color="secondary"> Incomplete </Button>
            </Paper>
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default LandingPage