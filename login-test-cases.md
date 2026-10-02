# Login Test Cases

| ID | Test Scenario | Test Data | Expected Result | Priority |
|---|---|---|---|---|
| TC-LOGIN-001 | Login with valid credentials | Valid email + password | User is logged in successfully | High |
| TC-LOGIN-002 | Invalid password | Valid email + wrong password | Error message is displayed | High |
| TC-LOGIN-003 | Invalid email format | `user@` | Validation message is displayed | High |
| TC-LOGIN-004 | Empty email | Blank | Email is required message appears | High |
| TC-LOGIN-005 | Empty password | Blank | Password is required message appears | High |
| TC-LOGIN-006 | Both fields empty | Blank | Required-field validation appears | High |
| TC-LOGIN-007 | Password masking | Any password | Password is hidden while typing | Medium |
| TC-LOGIN-008 | Leading/trailing spaces | ` user@example.com ` | Handling follows requirements | Medium |
| TC-LOGIN-009 | Multiple failed attempts | Wrong password repeatedly | Security behavior follows requirements | High |
| TC-LOGIN-010 | Responsive login page | Mobile viewport | Page remains usable | Medium |

## Example Execution

1. Open the login page.
2. Enter a registered email.
3. Enter the correct password.
4. Click **Login**.
5. Verify the dashboard/home page appears.

**Expected:** User is authenticated and redirected.

**Result:** Pass/Fail to be recorded during execution.
