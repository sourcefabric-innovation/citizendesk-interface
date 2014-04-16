/**
 * Twt_oauths
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

var functions = require('./functions.js');

module.exports = {

  attributes: {
  	
  	/* e.g.
  	nickname: 'string'
  	*/
    
    // Override toJSON instance method
    // to hide secret values
    toJSON: function() {
      var obj = this.toObject();
      var h = functions.hide;
      obj.spec.consumer_key = h(obj.spec.consumer_key);
      obj.spec.access_token_key = h(obj.spec.access_token_key);
      obj.spec.consumer_secret = h(obj.spec.consumer_secret);
      obj.spec.access_token_secret = h(obj.spec.access_token_secret);
      return obj;
    }
  }

};
