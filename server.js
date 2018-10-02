const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path'); 

/*Insert Data Scheme Here*/

/* Server */
const app = express();

// Bodyparser Middleware
app.use(bodyParser.json());

