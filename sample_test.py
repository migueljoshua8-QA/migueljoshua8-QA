def validate_login_response(status_code, response):
    """Simple QA-oriented example using plain Python."""
    assert status_code == 200, "Login request should return HTTP 200"
    assert "user" in response, "Successful response should contain user"

    user = response["user"]
    assert "email" in user, "User object should contain email"
    assert user["email"], "Email should not be empty"


def test_valid_login_response():
    response = {
        "user": {
            "id": 101,
            "email": "qa@example.com"
        }
    }

    validate_login_response(200, response)


if __name__ == "__main__":
    test_valid_login_response()
    print("QA validation passed.")
