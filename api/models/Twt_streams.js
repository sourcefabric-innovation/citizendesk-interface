var request = require('request');
/**
 * Twt_streams
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

  attributes: {
  	
  	/* e.g.
  	nickname: 'string'
  	*/
    
  },
  // Lifecycle Callbacks
  beforeUpdate: function(values, next) {
    var id = values.id;
    var action = values.control.switch_on ? 'start' : 'stop';
    var path = 'http://localhost:9054/feeds/twt/stream/'+id+'/'+action;
    //console.log(JSON.stringify(values));
    request.post(path, function(err, httpResponse, body) {
      if(err) return next(err);
      next();
    });
  }
};
