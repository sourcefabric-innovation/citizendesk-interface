var request = require('request');
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
    var id = values.id;
    var action = values.control.switch_on ? 'start' : 'stop';
    var path = 'http://localhost:9060/feeds/twt/stream/'+id+'/'+action;
    // possibly convert the id string to an id object
    try {
      values.spec.filter_id = mongodb.ObjectID(values.spec.filter_id);
    } catch (e) {
      console.log(e);
    }
    //console.log(JSON.stringify(values));
    request.post(path, function(err, response, body) {
      console.log('request sent to', path);
      console.log('response status is', response.statusCode);
      if(err) return next(err);
      next();
    });
  }
};
