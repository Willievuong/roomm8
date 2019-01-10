const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path'); 

/*Insert Data Schema Here*/

/* Server */
const app = express();

// Bodyparser Middleware
app.use(bodyParser.json());

// Db config  
const db = require('./config/config.js').mongoURI;

// Connecting to Mongo 
mongoose
  .connect(db, {userNewUrlParser: true})
  .then 

// Routes 

// Production 


/*Listening*/
const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server started on port ${port}`));