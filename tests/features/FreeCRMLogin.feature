@CRM
Feature: Free CRM Login Feature
  As a CRM User
  I want to login into the application
  so that i can work on CRM application




  Background:
    Given User is already on login page

Scenario: Free CRM Login Test Scenario

  #Given User is already on login page
  When title of Login page is Free CRM
  And user enters username and password
  And user clicks on login button
  Then user is on home page
  And Close the browser

  #WIthout examples keyword using parameter
Scenario: Free CRM Login Test Scenario1 using parameter
  #Given User is already on login page
  When title of Login page is Free CRM
  When user enters "Dranadheer" and "test@1234"
  And user clicks on login button
  Then user is on home page
  And Close the browser

Scenario Outline: Free CRM Login Test Scenario2
  #Given User is already on login page
  When title of Login page is Free CRM
  When user enters "<username>" and "<password>"
  And user clicks on login button
  Then user is on home page
  And Close the browser

Examples: login details
		|  username   | password |
		| Dranadheer  | test@1234 |
		| tom         | Test@456 |
        | Dranadheer1 | test@1234 |
		| tom123      | Test@456 |






