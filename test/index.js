var assert = require('assert')
  , Sails = require('sails')
  , barrels = require('barrels')
  , fixtures;

// Global before hook
before(function (done) {
  // Lift Sails with test database
  Sails.lift({
    log: {
      level: 'error'
    },
    adapters: {
      default: 'test'
    }
  }, function(err, sails) {
    if (err)
      return done(err);
    // Load fixtures
    barrels.populate(function(err) {
      done(err, sails);
    });
    // Save original objects in `fixtures` variable
    fixtures = barrels.objects;
  });
});

// Global after hook
after(function (done) {
  console.log();
  sails.lower(done);
});

// Here goes a module test
describe('OAuths', function() {
  describe('#list()', function() {
    it ('should list the user keys', function() {
      Twt_oauths.find(function(err, auths) {
        var gotAuths = (fixtures['twt_oauths'].length > 0);
        var authsAreInTheDb = (auths.length === fixtures['twt_oauths'].length);
        assert(gotAuths&&authsAreInTheDb, 'There must be something!');
      });
    });
  });
});
