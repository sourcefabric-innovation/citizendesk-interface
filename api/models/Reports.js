/**
 * Reports
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

  attributes: {
    id: 'string'
  },

  beforeCreate: function(values, next) {
    values.created = new Date();
    next();
  }
};
