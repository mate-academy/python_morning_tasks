import change_the_names


vars_mapper = {"n": "name", "l": "surname", "a": "age"}


def defined_var_message(variable: str) -> str:
    return f"Failed. Variable {variable} should be defined"


def renamed_var_message(bad_named_var: str, good_name_var: str) -> str:
    return f"Failed. The name {bad_named_var} is bad and unclear. Should be renamed into {good_name_var}"


def test_bad_named_vars_renamed():
    variables = change_the_names

    for bad_name, good_name in vars_mapper.items():
        assert hasattr(variables, good_name), defined_var_message(good_name)
        assert not hasattr(variables, bad_name), renamed_var_message(
            bad_name, good_name
        )
