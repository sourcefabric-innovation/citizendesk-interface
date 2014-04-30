var request = require('request');
/**
 * Twt_streamsController
 *
 * @module      :: Controller
 * @description	:: A set of functions called `actions`.
 *
 *                 Actions contain code telling Sails how to respond to a certain type of request.
 *                 (i.e. do stuff, then send some JSON, show an HTML page, or redirect to another URL)
 *
 *                 You can configure the blueprint URLs which trigger these actions (`config/controllers.js`)
 *                 and/or override them with custom routes (`config/routes.js`)
 *
 *                 NOTE: The code you write here supports both HTTP and Socket.io automatically.
 *
 * @docs        :: http://sailsjs.org/#!documentation/controllers
 */

function askCore(req, action, res) {
  var id = req.param('id');
  var path = 'http://localhost:9060/feeds/twt/stream/'+id+'/'+action;
  request.post(path, function(err, response, body) {
    console.log('request sent to', path);
    console.log('response status is', response.statusCode);
    if(err) return res.send(500);
    res.send();
  });
}

module.exports = {
  start: function(req, res) {
    askCore(req, 'start', res);
  },
  stop: function(req, res) {
    askCore(req, 'stop', res);
  },

  /**
   * Overrides for the settings in `config/controllers.js`
   * (specific to Twt_streamsController)
   */
  _config: {}

  
};
