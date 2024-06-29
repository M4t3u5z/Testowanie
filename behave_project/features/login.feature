Feature: User login

  Scenario: Successful login
    Given the API endpoint is "http://example.com/api/login"
    When I send a POST request to the login endpoint with:
      | email    | eve.holt@reqres.in |
      | password | pistol             |
    Then the response status code should be 200
    And the response should contain the key "token"
