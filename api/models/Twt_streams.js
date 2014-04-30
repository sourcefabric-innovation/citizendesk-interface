var mongodb = require('mongodb');
/**
 * Twt_streams
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

  attributes: {
  },
  // Lifecycle Callbacks
  beforeUpdate: function(values, next) {
    // possibly convert the id string to an id object
    try {
      values.spec.filter_id = mongodb.ObjectID(values.spec.filter_id);
    } catch (e) {
      console.log(e);
    }
    next();
  }
};
