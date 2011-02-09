Feature: Project maintenance
  As a NSI site administrator
  I want to handle project data
  In order to know what we are doing and what we did

  Scenario: Projects page
    Given exist a project:
      | name     | description              | logo    | sponsor | status | start_date | end_date   |
      | NSI Site | The terrific site of NSI | images/projects/nsi.png | NSI     | aberto | 2010-11-10 | 2011-02-01 |
    When I go to "the projects page"
    Then I should see "1 project"
    And I should see "NSI Site"
    And I should see "The terrific site of NSI"
    And I should see "Patrocinador: NSI"
    And I should see "Status: aberto"
    And I should see "Duração: 10/11/2010 a 01/02/2011"
    And I should see an image called "nsi.png"

  Scenario: Projects page for non-closed projects
    Given exist a project:
      | name     | description              | logo    | sponsor | status | start_date |
      | NSI Site | The terrific site of NSI | nsi.png | NSI     | aberto | 2010-11-10 |
    When I go to "the projects page"
    Then I should see "1 project"
    And I should see "NSI Site"
    And I should see "The terrific site of NSI"
    And I should see "Patrocinador: NSI"
    And I should see "Status: aberto"
    And I should see "Início: 10/11/2010"

