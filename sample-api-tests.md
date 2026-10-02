# API Testing — Sample Scenarios

These are demonstration scenarios for a REST-style API.

## GET Users
**Endpoint:** `GET /api/users`

Checks:
- HTTP status code
- Response time
- JSON structure
- Required fields
- Data types
- Empty response handling
- Pagination behavior

## POST User
**Endpoint:** `POST /api/users`

Checks:
- Valid request body
- Missing required fields
- Invalid field types
- Duplicate values
- Boundary-length values
- Correct HTTP status
- Response schema

## Negative Testing

```json
{
  "email": "invalid-email",
  "name": ""
}
```

Expected behavior: the API should reject invalid data with an appropriate status and useful validation response.

## QA Checklist
- [ ] Status code is correct
- [ ] Response body is valid JSON
- [ ] Required fields are present
- [ ] Data types are correct
- [ ] Error messages are meaningful
- [ ] Sensitive information is not exposed
- [ ] Authentication/authorization rules are respected
