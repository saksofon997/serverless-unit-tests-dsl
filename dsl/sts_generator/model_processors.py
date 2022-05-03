from textx.exceptions import TextXSemanticError
from textx import get_location

def duplicate_function_names_check(model, metamodel):
    function_names = [fun.name for fun in model.functions]

    duplicate_names = set(
        [name for name in function_names if function_names.count(name) > 1])

    if len(duplicate_names) != 0:
        raise TextXSemanticError(
            f"Duplicate function names found {duplicate_names}")


def duplicate_case_names_check(model, metamodel):
    for function in model.functions:
        cases_names = [case.name for case in function.cases]

        duplicate_names = set(
            [name for name in cases_names if cases_names.count(name) > 1])

        if len(duplicate_names) != 0:
            raise TextXSemanticError(
                f"Duplicate case names found {duplicate_names}, on\n\n{get_location(function)}")


def check_env_override(model, metamodel):
    for function in model.functions:
        if function.env:
            for case in function.cases:
                if case.env:
                    print(
                        f"Function environment variables will be overridden, on\n\n{get_location(case)}")