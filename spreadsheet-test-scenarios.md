# Spreadsheet Product Testing

## Testing Approach

For a spreadsheet product, I would test both spreadsheet functionality and data integrity.

### Functional Scenarios

| ID | Scenario | Expected |
|---|---|---|
| SS-001 | Enter text into a cell | Value is saved correctly |
| SS-002 | Enter numeric value | Number is stored/calculated correctly |
| SS-003 | Enter formula | Correct result is displayed |
| SS-004 | Copy formula | References behave correctly |
| SS-005 | Sort data | Rows remain associated with correct data |
| SS-006 | Filter data | Only matching records are displayed |
| SS-007 | Undo/Redo | Changes are restored correctly |
| SS-008 | Save and reopen | Data and formulas remain intact |

### Edge Cases

- Empty cells
- Zero values
- Negative numbers
- Very large numbers
- Decimal values
- Long text
- Special characters
- Duplicate records
- Invalid formulas
- Circular references
- Copy/paste across ranges
- Sorting with blank rows
- Filtering with mixed data types

### Data Integrity Check

Example:

```text
Quantity = 10
Unit Price = 25
Expected Total = 250
```

The displayed spreadsheet value should be `250`.
