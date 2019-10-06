import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import CustomizedDialogs from './Widgets/Dialog'
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
      currentRoom: {},
      loaded: false
    }
  }

  async loadData(){
    // TODO: Current values for HTTP GET request are hardcoded to be the first value, need to change later 
    let room = await axios.get(BACKEND_URL + "getRoomHousehold/1/")
    let task = await axios.get(BACKEND_URL + "getTaskHousehold/1/")
    let user = await axios.get(BACKEND_URL + "getUserHousehold/1/")


    this.setState({
      // household: (await axios.get(BACKEND_URL + "household/").data),
      user : user.data,
      room : room.data,
      task : task.data,
      loaded : true
    })
  }
  
  findUser(user){
    let userList = this.state.user
    for(var i = 0; i < userList.length; i++){
      
      if(userList[i]['id'] == user){
        return userList[i]['nickname']
      }
    }

    return "NO USER FOUND"
  }

  findRoom(task, room){
    if(room['id'] == task['room_id']){
      return this.findUser(task['user_id'])
    }
  }
  
  findUserButton(user){
    let userList = this.state.user
    for(var i = 0; i < userList.length; i++){
      if(userList[i]['id'] == user){
        return(<CustomizedDialogs userList={userList} user={user} />)
      }
    }

    return "NO USER FOUND"
  }

  findRoomButton(task, room){
    if(room['id'] == task['room_id']){
      return this.findUserButton(task['user_id'])
    }
  }
  buildList(){
    let roomSize = this.state.room.length
    let userSize = this.state.user.length 
    let taskSize = this.state.task.length 

    let roomList = this.state.room 
    let user = this.state.user 
    let taskList = this.state.task 

    const page = (
    <div>{
        roomList.map((room, index) => (
          <Paper className="paper">
            <Grid container spacing={8}>
              <Grid item xs={12}> 
                  {/* <Typography variant="title" component="h3"> */}
                    {room['name']}
                  {/* </Typography> */}
              </Grid>

              {taskList.map((task, index) => (
                <Grid container xs={12}> 
                  <Grid item xs={6}>
                      {this.findRoom(task, room)}
                  </Grid>
    
                  <Grid item xs={6}>
                      {this.findRoomButton(task, room)}
                  </Grid>
                </Grid> 
              ))
              }
            </Grid>
          </Paper>
        ))
      }
    </div>
    )
    return page 
  }


  async componentDidMount(){
    this.loadData()
  }

  render(){
      return(
        <div className="landing">
          {this.state.loaded === false ?
            <div>  <CircularProgress /> </div>
            :
            this.buildList()}
        </div>
      );
  }
}

export default LandingPage