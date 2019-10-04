import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import SimpleSelect from './Select'

export default function AlertDialog(props) {
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
            <SimpleSelect/>
          </DialogContentText>
          <TextField
            id="standard-password-input"
            label="Pin"
            type="password"
            autoComplete="current-password"
            margin="normal"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary" autoFocus>
            Submit
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}