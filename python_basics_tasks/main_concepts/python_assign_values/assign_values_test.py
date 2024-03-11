import assign_values


def defined_var_message(var: str) -> str:
    return f"Failed. Variable {var} should be defined"


def valid_type_message(var: str, expected_type: str) -> str:
    return f"Failed. Variable {var} should be {expected_type} data type"


def test_variables_defined():
    expected_variables = ["first_name", "age", "height", "is_married"]
    variables = assign_values

    for variable in expected_variables:
        assert hasattr(variables, variable), defined_var_message(variable)


def test_valid_data_types():
    variables = assign_values

    assert isinstance(getattr(variables, "first_name"), str), valid_type_message(
        "first_name", "string"
    )
    assert isinstance(getattr(variables, "age"), int), valid_type_message(
        "age", "integer"
    )
    assert isinstance(getattr(variables, "height"), int), valid_type_message(
        "height", "integer"
    )
    assert isinstance(getattr(variables, "is_married"), bool), valid_type_message(
        "is_married", "boolean"
    )
