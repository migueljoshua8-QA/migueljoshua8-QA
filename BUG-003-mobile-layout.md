# BUG-003 — Registration Form Overflows on Mobile

**Status:** Open  
**Severity:** Medium  
**Priority:** Medium  
**Type:** UI / Responsive  
**Environment:** Mobile viewport, 390 × 844

## Steps to Reproduce

1. Open the registration page.
2. Set the browser viewport to 390 × 844.
3. Scroll through the registration form.
4. Observe the input controls and buttons.

## Expected Result
All controls should fit within the viewport without unexpected horizontal scrolling.

## Actual Result
The form extends beyond the viewport and requires horizontal scrolling.

## Suggested Investigation
Inspect responsive CSS, fixed-width elements, container sizing, and overflow rules.
