Feature: User management

  Scenario: Create User
    Given the API endpoint is "http://example.com/api/users"
    When I send a POST request to the user creation endpoint with:
      | name | dsw46476     |
      | job  | programista  |
    Then the response status code should be 201
    And the response should contain the keys "id" and "createdAt"
