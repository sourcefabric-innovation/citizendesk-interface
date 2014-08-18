Feature: citizen aliases

Scenario: simple query request
    Given one alias
     When we ask for aliases
     Then we get the alias in the collection

Scenario: simple specific request
    Given one alias
     When we ask for that alias
     Then we get the alias

Scenario: simple specific request with embed
    Given one alias
     When we ask for that alias with embedded lists
     Then we get the alias

Scenario: embedded lists
    Given a list
      And an alias referring to it
     When we ask for the alias with the embedded list
     Then we get tags in the alias
      and we get the alias with the embedded list
