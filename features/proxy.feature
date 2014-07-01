Feature: using the proxy

Scenario: using the given proxy

    Given a request to start a twitter search
     then the request is forwarded to the core
      and the request is successful
