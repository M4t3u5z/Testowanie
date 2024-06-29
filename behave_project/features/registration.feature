Feature: User registration

  Scenario: Successful registration
    Given the API endpoint is "http://example.com/api/register"
    When I send a POST request to the registration endpoint with:
      | email    | test@test.pl |
      | password | Test12!@     |
    Then the response status code should be 200
    And the response should contain the keys "id" and "token"
