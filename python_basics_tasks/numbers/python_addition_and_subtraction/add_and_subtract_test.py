import add_and_subtract

from typing import Any


expected_variables = {"sum": 8, "difference": 2}


def assert_message(expected_var_name: str, expected_var_value: int, value: Any) -> str:
    return f"Failed. Variable {expected_var_name} should be equal to {expected_var_value}. Your answer: {value}"


def test_needed_variables_defined():
    variables = add_and_subtract

    for variable_name in expected_variables.keys():
        assert hasattr(
            variables, variable_name
        ), f"Failed. Variable {variable_name} should be defined"


def test_proper_values():
    variables = add_and_subtract

    for variable, value in expected_variables.items():
        var_value = getattr(variables, variable)
        assert var_value == value, assert_message(variable, value, var_value)
