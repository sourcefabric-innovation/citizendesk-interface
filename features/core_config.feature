Feature: handling core config

  Scenario: create a config doc
     given no docs in the core config collection
      when we create a new invented doc
      then the request fails

  Scenario: update a config doc
     given an sms doc in the database
      when we fetch the sms doc
       and we update the sms doc
      then the request is successful

  Scenario: fetch a config doc
     given an sms doc in the database
      when we fetch the sms doc
      then the request is successful
       and we get a list containing one document
