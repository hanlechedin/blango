# Sample Solution - Post Analyzer Exercise

## Overview
This directory contains a reference implementation of the Post Analyzer practical exercise. This is provided for interviewers to understand what a good solution looks like.

## Files
- `post_analyzer.py`: Complete implementation of the PostAnalyzer class
- `test_post_analyzer.py`: Comprehensive test suite using PyTest
- `sample_data.json`: Sample JSON file for testing file loading

## Key Features Demonstrated

### Code Quality
- Clear, readable code with good naming conventions
- Proper error handling (FileNotFoundError, ValueError)
- Type hints for better code documentation
- Docstrings for all public methods

### Python Best Practices
- Use of built-in libraries (collections.Counter)
- List comprehensions for filtering
- Proper exception handling
- Method chaining support (filter methods return new instances)

### Testing Approach
- **Fixtures**: Reusable test data setup
- **Parametrized tests**: Testing multiple scenarios efficiently
- **Edge cases**: Empty data, missing fields, division by zero
- **Integration tests**: Full workflow testing
- **Good test names**: Descriptive, follows convention

## Running the Tests

```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
pytest test_post_analyzer.py -v

# Run with coverage
pip install pytest-cov
pytest test_post_analyzer.py --cov=post_analyzer --cov-report=term-missing
```

## Expected Test Output

All tests should pass. Expected output:
```
test_post_analyzer.py::test_init_with_no_data PASSED
test_post_analyzer.py::test_init_with_data PASSED
test_post_analyzer.py::test_load_from_file_success PASSED
...
========================= XX passed in X.XXs =========================
```

## What Makes This a Good Solution

### Strengths
1. **Complete functionality**: All required methods implemented
2. **Error handling**: Graceful handling of edge cases
3. **Clean code**: Easy to read and understand
4. **Well-tested**: Comprehensive test coverage
5. **Extensible**: Easy to add new features

### Areas for Discussion
During the interview, you might discuss:
- Performance optimizations for large datasets
- Alternative approaches (e.g., using pandas)
- Additional features that could be added
- How to handle database storage instead of JSON
- Caching strategies for expensive calculations

## Variations You Might See

Candidates might approach this differently, and that's okay:
- Using different data structures
- Different error handling strategies
- More or fewer abstractions
- Different testing approaches

The key is that they:
- Solve the core requirements
- Write clean, understandable code
- Think about edge cases
- Can explain their decisions

## Time Expectations

A strong candidate should (based on 35 minutes of implementation time):
- Complete core functionality in 20-25 minutes
- Have basic tests in 25-30 minutes
- Handle some edge cases by 30-35 minutes
- Be ready to discuss by 35 minutes

It's okay if they don't finish everything - the goal is to see their approach and thinking process.
