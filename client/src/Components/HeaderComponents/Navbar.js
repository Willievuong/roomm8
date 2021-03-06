import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import MailIcon from '@material-ui/icons/Mail';
import { Link } from "react-router-dom";
import '../css/navbar.css'

const styles = {
  root: {
    flexGrow: 1,
  },
  grow: {
    flexGrow: 1,
  },
};

class ButtonAppBar extends Component {
  state = {
    anchorEl: null,
    open: false,
  };

  /* Need Correction, there is no side here */
  toggleDrawer = (side, open) => () => {
    this.setState({
      [side]: open,
    });
  };


  handleClick = event => {
    this.setState({ anchorEl: event.currentTarget });
  };

  handleClose = () => {
    this.setState({ anchorEl: null });
  };

  render(){
    const { classes } = this.props;
    const { anchorEl }= this.state;

    const sideList = (
      <div className={classes.list}>
        <List>
          {['Home', 'Family', 'Contacts', 'Maintainence'].map((text, index) => (
            <ListItem button key={text}>
              <ListItemIcon>{<MailIcon/>}</ListItemIcon>
              <Link to={"/" + text} className="menuButton">
              <ListItemText primary={text} />
              </Link>
            </ListItem>
          ))}
        </List>
        <Divider />
        <List>
          {['All Notification', 'Tickets', 'Logout'].map((text, index) => (
            <ListItem button key={text}>
              <ListItemIcon>{<MailIcon/>}</ListItemIcon>
              <Link to={"/" + text} className="menuButton">
              <ListItemText primary={text} />
              </Link>
            </ListItem>
          ))}
        </List>
      </div>
    );

    return (
      <div className={classes.root}>
        <AppBar position="static" color="secondary">
          <Toolbar>
            {/* <Button className={classes.menuButton} onClick={this.toggleDrawer('left', true)}  color="inherit" >
              <MenuIcon 
                aria-owns={anchorEl ? 'menu' : null}
                aria-haspopup="true"
                /></Button>
            <Drawer open={this.state.left} onClose={this.toggleDrawer('left', false)}>
              <div
                tabIndex={0}
                role="button"
                onClick={this.toggleDrawer('left', false)}
                onKeyDown={this.toggleDrawer('left', false)}
              >
                {sideList}
              </div>
            </Drawer> */}
            <Typography variant="title" color="inherit" className={classes.grow}>
              Room8
            </Typography>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

ButtonAppBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ButtonAppBar);