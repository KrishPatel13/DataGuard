import sys
import inspect

import fire


def get_functions(name):
    """
    Get a dictionary of function names to functions for all non-private functions

    Usage:

        if __name__ == "__main__":
            fire.Fire(utils.get_functions(__name__))

    Args:
        TODO

    Returns:
        A dictionary of function names to functions.
    """

    functions = {}
    for name, obj in inspect.getmembers(sys.modules[name]):
        if inspect.isfunction(obj) and not name.startswith("_"):
            functions[name] = obj
    return functions


if __name__ == "__main__":
    fire.Fire(get_functions(__name__))
