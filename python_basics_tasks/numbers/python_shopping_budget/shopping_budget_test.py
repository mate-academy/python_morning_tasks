import shopping_budget


VARIABLES = shopping_budget

expected_variables = {"budget": 50, "milk_price": 3, "bread_price": 2, "result": 45}


def test_variables_are_defined():
    variable_names = [
        name for name in dir(shopping_budget) if not name.startswith("__")
    ]

    for var_name in variable_names:
        var_value = getattr(VARIABLES, var_name)
        if var_name in expected_variables:
            expected_value = expected_variables.get(var_name)
            assert (
                var_value == expected_value
            ), f"Failed. Variable {var_name} should be defined and set to {expected_value}"
        else:
            rest = expected_variables["result"]
            assert (
                var_value == rest
            ), f"Failed. Your calculations are wrong: {var_name} is set to {var_value} != {rest}"
