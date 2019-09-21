import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import './css/landing.css'
const axios = require('axios')

const BACKEND_URL = "http://localhost:8000/"

class LandingPage extends Component { 
  constructor(props){
    super(props);
    this.state = {
      user: {},
      room: {},
      task: {},
    }
  }

  async loadData(){
    this.state.user = (await axios.get(BACKEND_URL + "profile/")).data
    this.state.room = (await axios.get(BACKEND_URL + "room/")).data
    this.state.task = (await axios.get(BACKEND_URL + "task/")).data

    this.state.room.map((room, index) => {
      console.log(room)
    })

  }
  
  
  buildList(room){
    this.loadData()
    let roomSize = room.length
    let userSize = this.state.user.length 
    let taskSize = this.state.task.length 

    const page = (
      <Grid container spacing={8}>
        {
          (
            <div>
              There are {roomSize} many room 
            </div>
          )
        }
        {/* <Grid item xs={12}> 
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
        </Grid> */}
      </Grid>
    )

    return page 
  }


  componentDidMount(){
    this.loadData()
  }

  render(){
    const room = this.state.room


    return(
      <div className="landing">
        {this.buildList(room)}
      </div>
    );
  }
}

export default LandingPage