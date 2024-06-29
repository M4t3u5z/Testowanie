import requests
from behave import given, when, then
from hamcrest import assert_that, equal_to, has_key

print("Loading step definitions...")

@given('the API endpoint is "{url}"')
def step_given_api_endpoint(context, url):
    print(f"Given step with URL: {url}")
    context.url = url

@when('I send a POST request to the registration endpoint with:')
def step_when_send_post_request_registration(context):
    print("When step for registration")
    payload = {}
    for row in context.table:
        payload[row['email']] = row['password']
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(context.url, json=payload, headers=headers)

@when('I send a POST request to the login endpoint with:')
def step_when_send_post_request_login(context):
    print("When step for login")
    payload = {}
    for row in context.table:
        payload[row['email']] = row['password']
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(context.url, json=payload, headers=headers)

@when('I send a POST request to the user creation endpoint with:')
def step_when_send_post_request_user_creation(context):
    print("When step for user creation")
    payload = {}
    for row in context.table:
        payload[row['name']] = row['job']
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(context.url, json=payload, headers=headers)

@then('the response status code should be {status_code:d}')
def step_then_response_status_code(context, status_code):
    print(f"Then step for status code: {status_code}")
    assert_that(context.response.status_code, equal_to(status_code))

@then('the response should contain the keys "{key1}" and "{key2}"')
def step_then_response_contains_two_keys(context, key1, key2):
    print(f"Then step for keys: {key1}, {key2}")
    response_json = context.response.json()
    assert_that(response_json, has_key(key1))
    assert_that(response_json, has_key(key2))

@then('the response should contain the key "{key}"')
def step_then_response_contains_one_key(context, key):
    print(f"Then step for key: {key}")
    response_json = context.response.json()
    assert_that(response_json, has_key(key))
