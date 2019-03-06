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
// mongoose
//   .connect(db, {userNewUrlParser: true})
//   .then()

// Routes 
app.get('/', (req, res) => {
  res.send('Hello World')

})

app.get('/profile/:userID', (req, res) => {
  
})

app.get('/family/:userID', (req, res) => {

})

app.get('/maintainence/:userID', (req, res) => {

})

app.post('/login', (req, res) =>{

})

app.post('/ticket/:familyID/:userID', (req, res) => {
  
})


// Production 


/*Listening*/
const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server started on port ${port}`));