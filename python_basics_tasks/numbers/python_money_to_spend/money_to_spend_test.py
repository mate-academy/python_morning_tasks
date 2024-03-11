import money_to_spend


predefined_vars = {"yearly_salary": 1000000, "days": 365}


def test_daily_profit_calculation():
    daily_salary = predefined_vars.get("yearly_salary") / predefined_vars.get("days")

    result_variable_name = [
        name for name in dir(money_to_spend) if not name.startswith("__")
    ]

    assert (
        len(result_variable_name) >= 2
    ), "Failed, you need to define at least one additional variable in order to calculte daily salary "

    for var_name in result_variable_name:
        var_value = getattr(money_to_spend, var_name)

        if var_name in predefined_vars:
            assert var_value == predefined_vars.get(
                var_name
            ), f"Failed. variable {var_name} had been changed to {var_value}"
        else:
            assert (
                var_value == daily_salary
            ), f"Failed. Your output {var_value} != {daily_salary}"
