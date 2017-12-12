# Created by johnc at 24/11/17
Feature: Client registration

  # Enter feature description here

  Scenario: Password registration requires email confirmation
    Given a new user
    When they register using email/password
    Then they are sent a email confirm email
    And the email confirm link confirms their email

  Scenario: Email registration create a new Profile and user have to set up profile
    Given a new user
    When they register using email/password
    Then the user is on the page /profile/
    And the user has a profile

  @skip
  Scenario: Email registration create generated_email when user has set up profile
    Given a new user
    When they register using email/password
    And set up their profile
    Then the user has a generated_email
    And the user has a rule_id

  @skip
  Scenario: Facebook registration requires email confirmation, because people don't update their Facebook email
    Given a new user
    When they register using Facebook
    Then they need to confirm their email

  @skip
  Scenario: Google registration doesn't requires email confirmation
    Given a new user
    When they register using Google
    Then they don't need to confirm their email
