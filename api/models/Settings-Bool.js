/**
 * Settings-Bool
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

  attributes: {
    /* keys can contain spaces, but try to keep them simple in order
     * to avoid typos */
    key: {
      type: 'string',
      required: true
    },
    value: {
      type: 'boolean',
      required: true
    }
  }

};
