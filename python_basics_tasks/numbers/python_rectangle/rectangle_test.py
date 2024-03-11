import rectangle


def test_area_variable_defined_and_stores_right_value():
    expected_var_name = "area"
    length = 20
    width = 10
    expected_value = length * width

    assert hasattr(
        rectangle, "area"
    ), f"Failed. Variable {expected_var_name} should be defined"

    output_value = getattr(rectangle, "area")
    assert (
        output_value == expected_value
    ), f"Failed. {expected_var_name} variable should store valid value. {output_value} != {expected_value}"
