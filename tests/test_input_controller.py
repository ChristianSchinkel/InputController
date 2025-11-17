import pytest

from InputController.inputController import InputController


def test_check_input_is_string():
    ctrl = InputController()
    assert ctrl.check_input_is_string("hello")
    assert not ctrl.check_input_is_string(5)


def test_contain_and_normalize_and_replace():
    ctrl = InputController()
    assert ctrl.contain_float_separator("1.2")
    assert ctrl.contain_float_separator("1,2")
    assert not ctrl.contain_float_separator("12")
    assert ctrl.decimal_normalizer("1,23") == "1.23"
    assert ctrl.decimal_normalizer("1.23") == "1.23"
    assert ctrl.replace_float_separator("1,23") == "1.23"


def test_thousand_separator_remover():
    ctrl = InputController()
    # '.' appears before ',' => treat '.' as thousand separator
    assert ctrl.thousand_separator_remover("1.234,56") == "1234,56"
    # ',' appears before '.' => treat ',' as thousand separator
    assert ctrl.thousand_separator_remover("1,234.56") == "1234.56"


def test_is_integer_and_is_floatable():
    ctrl = InputController()
    assert ctrl.is_integer("123")
    assert not ctrl.is_integer("1.23")
    assert ctrl.is_floatable("1.23")
    assert ctrl.is_floatable("1,23")
    assert not ctrl.is_floatable("abc")
    assert not ctrl.is_floatable("123")


def test_format_int_reprompts(monkeypatch):
    ctrl = InputController()
    inputs = iter(["abc", "7"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    assert ctrl.format_int("Enter: ") == 7


def test_format_bool_reprompts(monkeypatch):
    ctrl = InputController()
    inputs = iter(["maybe", "Y"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    assert ctrl.format_bool("?") is True


def test_format_float_reprompts_then_accepts(monkeypatch):
    ctrl = InputController()
    # first input looks like integer and should be rejected for float
    inputs = iter(["123", "1.5"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    assert ctrl.format_float("Enter float: ") == 1.5


def test_format_float_with_thousand_separator(monkeypatch):
    ctrl = InputController()
    inputs = iter(["1.234,56"])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    assert ctrl.format_float("Enter: ") == 1234.56
