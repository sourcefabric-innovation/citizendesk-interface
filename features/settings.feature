Feature: handling settings

  Scenario: create a boolean setting
     given no boolean settings in the database
      when we create a new boolean setting
      then the request is successful
       and we get the id in the request

  Scenario: update a boolean setting
     given no boolean settings in the database
      when we create a new boolean setting
       and we update the boolean setting
      then the request is successful
