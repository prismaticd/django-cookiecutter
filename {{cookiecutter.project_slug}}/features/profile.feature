# Created by johnc at 24/11/17
Feature: Client login
  # Enter feature description here

  Scenario: Password reset
    Given a registered user
    When they submit a password reset request
    Then they are sent a password reset email
    And the password reset link resets their password

  @skip
  Scenario: The users without profile set up will be redirected to their profile page
    Given a registered user
    When the user logs in
    And the user has a empty profile
    Then the user is indeed redirected to "/profile/"

  @skip
  Scenario: The users that set up their profile wont't be redirected to their profile page
    Given a registered user
    When the user logs in
    And the user has a set up profile
    Then the user is not redirected to "/profile/"
