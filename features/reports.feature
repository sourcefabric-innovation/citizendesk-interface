Feature: handling reports

  Scenario: create report
      when we insert a report
      then the request is successful
       and the report gets a report id

  Scenario: get a posted report
      when we insert a report
       and we get the inserted report
      then the request is successful

  Scenario: modify a created report
      when we insert a report
       and we modify the inserted report
      then the request is successful

  Scenario: modify a created report
      when we insert a report
       and we modify the inserted report
       and we get the inserted report
      then the request is successful
       and the report entity tag is updated upon change

  Scenario: get reports
     given no reports
      when we ask reports
      then we get an empty list

  Scenario: get assigned reports
     given one report assigned to user 1
      when we ask reports assigned to user id 1
      then we get the assigned report

  Scenario: get assigned reports when there is none
     given one report assigned to user 1
      when we ask reports assigned to user id 2
      then we get an empty list
