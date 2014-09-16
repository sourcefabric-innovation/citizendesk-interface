Feature: using the proxy

 The proxy blueprint acts as a connector between frontend requests and
 core requests

Scenario: start a twitter search
    Given a request to start a twitter search
     then the request is forwarded to the core
      and the request is successful

Scenario: twitter alias request
    Given a request to fetch a twitter alias
     then the fetch request is forwarded to the core

Scenario: publish report
    Given a request to publish a report
     then the publish request is forwarded to the core

Scenario: unpublish report
    Given a request to unpublish a report
     then the unpublish request is forwarded to the core

Scenario: ingest from location
    given a request to ingest from a location
     then the ingestion request is forwarded to the core
