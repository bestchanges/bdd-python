Feature: As a lazy developer I want to test todomvc.com automatically

  Scenario: Enter new todo-item and ensure it was added
    Given user open webpage http://todomvc.com/examples/react/
    And there are no todo-item 'My first task' in the list
    When user add task 'My first task'
    Then there is todo-item 'My first task' in the list
