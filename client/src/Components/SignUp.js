import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';

const styles = theme => ({
  root: {
    ...theme.mixins.gutters(),
    paddingTop: theme.spacing.unit * 2,
    paddingBottom: theme.spacing.unit * 2,
  },
});

class SignUp extends Component {
  state = {
    name: 'name goes here',
  }
  render(){
    const { classes } = this.props;

    return(
      <Grid container
            spacing={0} 
            justify="center" 
            alignItems="center"
        >
        <Grid item>
          <Paper>
            <Grid container 
                  spacing={0}
                  justify="center"
                  alignItems="center"
                  direction="column"
              >
              <form noValidate autoComplete="off">
                <Grid item>
                  <TextField
                    required
                    id="outlined-name"
                    label="Name"
                    className={classes.textField}
                    value={this.state.name}
                  // onChange={this.handleChange('name')}
                    margin="normal"
                    variant="outlined"
                  />
                </Grid>
                <Grid item>
                  <TextField
                    required
                    id="outlined-email"
                    label="Required"
                    defaultValue="user@something.com"
                    className={classes.textField}
                    margin="normal"
                    variant="outlined"
                  />   
                </Grid> 
              </form>
            </Grid>
          </Paper>
        </Grid>
      </Grid>
    );
  }
}

SignUp.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SignUp);