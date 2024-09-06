# DFA Simulator

This project implements a Deterministic Finite Automaton (DFA) simulator in Python.

## Author

Rodolfo Lopez

## Date

September 30, 2021

## Files

- `pa1.py`: Contains the main DFA class implementation.
- `test_pa1.py`: Test script to validate the DFA simulator.
- Various `.txt` files: Input files for DFA definitions and test strings.

## DFA Class

The `DFA` class in `pa1.py` simulates a DFA. It includes methods to:

- Initialize a DFA from a file (`__init__`)
- Simulate the DFA on an input string (`simulate`)
- Handle state transitions (`transition`)

## Usage

To use the DFA simulator:

1. Create a DFA instance by providing a DFA definition file:

   ```python
   dfa = DFA("dfa1.txt")
   ```

2. Simulate the DFA on an input string:
   ```python
   result = dfa.simulate("010101")
   ```

The `simulate` method returns `True` if the input string is accepted by the DFA, and `False` otherwise.

## Testing

The `test_pa1.py` script tests the DFA simulator against various input files. It compares the results with expected outputs to verify correctness.

To run the tests:

```bash
    python test_pa1.py
```

## Input File Formats

- DFA definition files (e.g., `dfa1.txt`): Specify the DFA structure.
- String files (e.g., `str1.txt`): Contain input strings to test.
- Correct output files (e.g., `correct1.txt`): Contain expected results for validation.
