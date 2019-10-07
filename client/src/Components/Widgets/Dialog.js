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

export default function AlertDialog(props) {
  const [values, setValues] = React.useState({
    userId: props.user,
    userPin: '',
    checkUserId: '',
    checkUserPin: '',
  });
  const [open, setOpen] = React.useState(false);
  

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  
  };

  const handleChange = event => {
    setValues(oldValues => ({
      ...oldValues,
      [event.target.name]: event.target.value,
    }));
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

  const submit = () => {
    console.log("SUBMITTING")
    console.log(values.userId)
    console.log(values.userPin)
  }

  return (
    // Need To make all of this into a form
    <div>
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
          />
        </DialogContent>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
          <form autoComplete="off">
          <FormControl>
            <InputLabel htmlFor="name-simple">Name</InputLabel>
            <Select
              value={values.userId}
              onChange={handleChange}
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
            value={values.userPin}
            onChange={handleChange}
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