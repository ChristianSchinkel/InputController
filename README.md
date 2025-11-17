# InputController

## Typesafe CLI input helper for Python

`InputController` provides a small, dependency-free helper class to collect and
validate common primitive input types in CLI programs (strings, integers,
floats and booleans). It includes normalization for decimal separators and
basic thousand-separator handling so users can input numbers in common
localized formats.

**Key features**
- Prompt-driven helpers: `format_int`, `format_float`, `format_bool`.
- Helpers for localized number input (commas/dots and thousand separators).
- Small, single-class API for easy import into scripts.

## Installation

Install editable from the project root for development:

```bash
pip install -e .
```

Or install normally:

```bash
python3 setup.py install
```

## Quick usage

Import the controller and call the methods you need. Example:

```python
from InputController import InputController

ctrl = InputController()

# Validate a string
print(ctrl.check_input_is_string("hello"))  # True

# Prompt for an integer (re-prompts until a valid integer is given)
value = ctrl.format_int("Enter an integer: ")
print(value)

# Prompt for float; accepts "1.234,56" or "1,234.56" style input
f = ctrl.format_float("Enter a float: ")
print(f)

# Prompt for boolean (yes/no, y/n, true/false)
b = ctrl.format_bool("Continue? [y/n]: ")
print(b)
```

You can also run the example CLI inside the package:

```bash
python -m InputController.inputController
```

## API reference (short)

- `InputController()` — main class.
- `check_input_is_string(user_input: str) -> bool` — returns True if input is a Python `str`.
- `format_int(prompt: str) -> int` — prompt until a valid integer is entered.
- `format_float(prompt: str) -> float` — prompt until a valid float is entered; accepts `,` or `.` decimal separators and handles thousand separators heuristically.
- `format_bool(prompt: str) -> bool` — prompt until a yes/no answer is given; accepts `yes/no`, `y/n`, `true/false` (case-insensitive).
- `contain_float_separator(user_input: str) -> bool` — returns True if `.` or `,` is present.
- `is_integer(user_input: str) -> bool` — heuristic check whether a string represents an integer.
- `replace_float_separator(user_input: str) -> str` — replace comma with dot.
- `is_floatable(user_input: str) -> bool` — returns True if string can be parsed as a float after normalization.
- `thousand_separator_remover(user_input: str) -> str` — removes thousand separators when both `.` and `,` are present.
- `decimal_normalizer(user_input: str) -> str` — normalize decimal separator to `.`.

## Notes

- The float parsing logic tries to be forgiving for localized input. If both
	`.` and `,` appear, the code makes a heuristic guess about which is the
	thousand separator based on their positions.
- This project intentionally avoids adding external dependencies; it's meant
	to be a tiny helper for CLI scripts.

## License

MIT
