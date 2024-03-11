import hours_to_study


predefined_values = {"study_hours_computer": 2, "study_hours_phone": 1, "study_days": 6}


def test_count_hours():
    weekly_computer = (
        predefined_values["study_days"] * predefined_values["study_hours_computer"]
    )
    weekly_phone = (
        predefined_values["study_days"] * predefined_values["study_hours_phone"]
    )
    total = weekly_computer + weekly_phone

    with open("hours_to_study.py", "r") as file:
        lines = file.readlines()

        for row in range(len(lines) - 1, -1, -1):
            line = lines[row].strip()

            if line and not line.startswith("#"):
                last_line = line
                break

        parts = last_line.split(" =")

        variable_name = parts[0].strip()
        value_formula = parts[1].strip()

        splitted_formula = value_formula.split()
        for element in splitted_formula:
            assert (
                not element.isdigit()
            ), "Failed. Avoid hardcoding and use predefined variables to make calculations"

    variable_value = getattr(hours_to_study, variable_name)
    assert (
        variable_value == total
    ), f"Failed. Got variable {variable_name} with value {variable_value} != {total}"
