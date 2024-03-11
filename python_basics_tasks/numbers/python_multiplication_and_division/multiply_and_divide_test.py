import multiply_and_divide


VARIABLES = multiply_and_divide

expected_variables = {
    "length": 8,
    "width": 9,
    "multiplication": 8 * 9,
    "division": 8 / 9,
}


def test_variables_are_defined():
    for var_name in expected_variables:
        assert hasattr(
            VARIABLES, var_name
        ), f"Failed. You should define {var_name} variable"


def test_proper_formulas_with_variables():
    for var_name, var_value in expected_variables.items():
        check_var = getattr(VARIABLES, var_name)
        assert (
            check_var == var_value
        ), f"Failed. Variable {var_name} should be equal to {var_value}"
