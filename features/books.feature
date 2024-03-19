Feature: Books capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button
    When login: I login with user "admin" and pass "Admin123!"

  @books
  Scenario: I validate the stock count
    Then books: I validate that 8 books are displayed

  @books
  Scenario Outline: I validate the search is working
    When books: I search after "<query>"
    Then books: I validate that only "Learning JavaScript Design Patterns" book is displayed

    Examples:
      | query                               |
      | Learning JavaScript Design Patterns |
      | Addy Osmani                         |
#      | Git                                 |
#      | Richard                             |

  @test
  Scenario: I validate that clear search is working
    When books: I search after "test"
    When books: I clear search input
    Then books: I validate that 8 books are displayed