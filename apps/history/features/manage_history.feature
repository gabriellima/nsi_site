Feature: History maintenance
  As a NSI site administrator
  I want to maintain history data
  In order to keep people informed about the glorious history of NSI

  Scenario: History page
    Given current history is "Hello, we are the glorious NSI."
    When I go to "the history page"
    Then I should see "Hello, we are the glorious NSI."

  Scenario: Accepts restructuredText format input
    Given current history is "*NSI* rules!"
    When I go to "the history page"
    Then I should have "<em>NSI</em> rules!" as HTML

