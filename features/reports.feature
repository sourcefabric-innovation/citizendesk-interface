Feature: handling reports

  Scenario: get reports
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
