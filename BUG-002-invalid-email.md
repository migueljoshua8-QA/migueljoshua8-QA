# BUG-002 — Invalid Email Format Accepted

**Status:** Open  
**Severity:** Medium  
**Priority:** High  
**Type:** Validation  
**Environment:** Firefox / Windows desktop

## Steps to Reproduce

1. Open the registration page.
2. Enter `test@` into the email field.
3. Fill the other required fields with valid data.
4. Submit the form.

## Expected Result
The application should reject the invalid email format and display a clear validation message.

## Actual Result
The form accepts the invalid email format and proceeds to the next step.

## Reproducibility
4/5 attempts.

## Test Data
- `test@`
- `user`
- `user.example.com`
- `@example.com`

## Suggested Investigation
Review client-side and server-side email validation rules.
