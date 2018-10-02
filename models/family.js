const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const FamilySchema = new Schema({
  name: {
    type: String,
    required: true
  }
});

module.exports = family = mongoose.model('family', FamilySchema);