import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import './css/landing.css'
const axios = require('axios')

const BACKEND_URL = "https://localhost:8000/"

class LandingPage extends Component { 
  constructor(props){
    super(props);
    this.state = {
      user: {},
      room: {},
      task: {},
      loaded: false
    }
  }

  async loadData(){
    this.setState({
      user :(await axios.get(BACKEND_URL + "profile/")).data,
      room : (await axios.get(BACKEND_URL + "room/")).data,
      task : (await axios.get(BACKEND_URL + "task/")).data,
      loaded : true
    })
  }
  
  
  buildList(){
    let roomSize = this.state.room.length
    let userSize = this.state.user.length 
    let taskSize = this.state.task.length 

    let room = this.state.room 
    let user = this.state.user 
    let task = this.state.task 


    const page = (
    <div>{
        room.map((value, index) => (
          <Paper className="paper">
            <Grid container spacing={8}>
              <Grid item xs={12}> 
                {/* <Paper className="paper"> */}
                  <Typography variant="title" component="h3">
                    {value['name']}
                  </Typography>
                {/* </Paper> */}

              </Grid>
              <Grid item xs={6}>
                  Janet
              </Grid>

              <Grid item xs={6}>
                  <Button variant="contained" color="secondary"> Incomplete </Button>
              </Grid>
            </Grid>
          </Paper>
        ))
      }
    </div>
    )
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

    return page 
  }


  componentDidMount(){
    this.loadData()
  }

  render(){
      return(
        <div className="landing">
          {this.state.loaded === false ?
            <div> Loading... </div>
            :
            this.buildList()}
        </div>
      );
  }
}

export default LandingPage