## Tests
- Automated Tests
- Unit tests (aka Test Case): Specifically designed to test **one function**.
- Test output: pass, fail, or gives an error
- Nominal vs. Edge Cases
  - Edge Cases: Positive vs. Negative
  - Positive: ??  
  - Negative: ??  
- Run tests from the terminal with the command **pytest**

### Anatomy of a test function:
**Test name**  
**Arrange**: set up variables  
**Act**: call the tested function  
**Assert**: Assertion statement: compare result of function with expected outcome.  

**Assert statement:** checks for truthin-ess.    
- **If truthy --> pass**, moves on to next line.  
- **if falsy --> fail**; the test execution will leave that test, and move on to the next test.  

### Test Naming
- Must start wtih: **test_** or end with **_test** to be recognized by pytest.
- Example name: **test_calculate_non_numbers_returns_type_error()**  
- A name should include:  
  - the tested function
  - context (possibly the kinds of arguments)
  - its expected outcome (usually the return value)
---