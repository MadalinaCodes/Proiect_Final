Feature: Login capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button

  @smoke
  Scenario: I login with valid credentials
    When login: I login with user "admin" and pass "Admin123!"
    Then books: I should land on books page

  @regression
  Scenario Outline: I login with invalid credentials
    When login: I login with user "<user>" and pass "<pswd>"
    Then login: I validate that error message is displayed

  Examples:
    | user    | pswd       |
    | admin   | Admin123   |
    | admin   | Admin1234  |


