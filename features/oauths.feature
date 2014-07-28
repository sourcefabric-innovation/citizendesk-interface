Feature: masking key values

Scenario: masking the key served to the client
    given a key in the database
     when the user asks for the key
     then he gets masked values
