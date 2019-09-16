import React, { Component } from 'react';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import './css/landing.css'


class LandingPage extends Component { 
  render(){

    return(
      <div className="landing">
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Paper> 
              <Typography variant="h5" component="h3">
                Kitchen
              </Typography>
              <Typography component="p">
                Paper can be used to build surface or other elements for your application.
              </Typography>
            </Paper>
          </Grid>
          <Grid item xs={6}>
            <Paper> 
              Janet
            </Paper>
          </Grid>
          <Grid item xs={6}>
            <Paper> 
              <Button variant="contained" color="primary"> Submit </Button>
            </Paper>
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default LandingPage