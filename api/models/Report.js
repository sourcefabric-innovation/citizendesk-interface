/**
 * Report
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

  attributes: {
    channels: [
      {
        filter: {
          track: "STRING"
        },
        type: "STRING",
        value: "STRING"
      }
    ],
    checks: [ ],
    citizens: [
      {
        authority: "STRING",
        identifiers: {
          user_id: "STRING",
          user_name: "STRING"
        }
      }
    ],
    feed_type: "STRING",
    modified: {
      $date: "DATETIME"
    },
    produced: {
      $date: "DATETIME"
    },
    proto: true,
    publishers: [
      {
        type: "STRING",
        value: "STRING"
      }
    ],
    texts: [
      "STRING"
    ],
    verification: "STRING",
  }

};
