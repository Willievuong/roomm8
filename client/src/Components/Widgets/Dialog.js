import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import Select from '@material-ui/core/Select';
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
const axios = require('axios')
const BACKEND_URL = "http://localhost:8000/"

export default function AlertDialog(props) {
  const [userId, setId] = React.useState(props.user)
  const [userPin, setPin] = React.useState('')
  const [checkUserId, setCheckId] = React.useState('')
  const [checkUserPin, setCheckPin] = React.useState('')
  const [open, setOpen] = React.useState(false);
  

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const findUser = (user) => {
    let userList = props.userList
     
    for(var i = 0; i < userList.length; i++){
      if(userList[i]['id'] == user){
        return userList[i]['nickname']
      }
    }
  } 

  const checkOffList = (user, oldUserList) => {
    let userList = [] 
    for(var i = 0; i < oldUserList.length; i++){
      if(oldUserList[i]['id'] != user){
        userList.push(oldUserList[i])
      }
    } 

    // console.log("PRINTING")
    // for(let i = 0; i < userList.length; i++){
    //   console.log(userList[i]['nickname'])
    // }

    // console.log(userList)
    let menuItem = userList.map(user => (
      <MenuItem key={user} value={user}>
        {user['nickname']}
      </MenuItem>
    ))

    return menuItem
  }

  const submit = async () => {    
    //Build JSON 
    currentDate = new Date() 
    let task_update  = {
      "status": "complete", 
      "end_date": currentDate,
      "user_check_id": this.state.checkUserId 
    }
    let response = await axios.post(BACKEND_URL + "task/" + task['id'] + "/", task_update)
    
    // If response is good, change status to complete 

    // If not good, prompt error 

    setOpen(false);
  }

  return (
    // Need To make all of this into a form
    <div>
      {/* Todo: Make this into a completed color */}
      <Button variant="outlined" color="secondary" onClick={handleClickOpen}>
        Incomplete
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Completed your task?"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {findUser(props.user)}
          </DialogContentText>
          <TextField
            id="standard-password-input"
            label="Pin"
            type="password"
            autoComplete="current-password"
            margin="normal"
            value={userPin}
            onChange={e => setPin(e.target.value)}
          />
        </DialogContent>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
          <form autoComplete="off">
          <FormControl>
            <InputLabel htmlFor="name-simple">Name</InputLabel>
            <Select
              value={checkUserId}
              onChange={e => setCheckId(e.target.value)}
              inputProps={{
                name: 'name',
                id: 'name-simple',
              }}
            >
              {checkOffList(props.user, props.userList)}
            </Select>
          </FormControl>
        </form>
          </DialogContentText>
          <TextField
            id="standard-password-input"
            label="Pin"
            type="password"
            autoComplete="current-password"
            margin="normal"
            value={checkUserPin}
            onChange={e => setCheckPin(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={submit} color="primary" autoFocus>
            Submit
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}