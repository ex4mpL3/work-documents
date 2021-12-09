import inspect


def input_arguments_with_prompts(*prompts):
    """
    Decorator is applied to functions that require data entry

    Parameters
        ----------
        prompts : |str| or |Tuple[str]|, optional
            Inputs an unlimited number of prompts and asks for data entry for each prompt

    Examples
    --------
    >>> @input_arguments_with_prompts("Input the number shelf: ")
    ... def add_shelf_with_input_value(new_shelf: str):
        ...      return add_shelf(new_shelf)

    >>> @staticmethod
    ... def add_shelf(new_shelf: str):
        ... if new_shelf in directories:
            ...raise KeyError
        ... directories[new_shelf] = []
        ... return
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            parameter_list = list(inspect.signature(func).parameters.items())
            if parameter_list[0][0] in ('self', 'cls'):
                parameter_list = parameter_list[1:]
            for prompt, (name, parameter) in zip(prompts, parameter_list):
                while True:
                    value = input(prompt)
                    if parameter.annotation is inspect._empty:
                        converted_value = value
                        break
                    try:
                        converted_value = parameter.annotation(value)
                    except ValueError:
                        pass
                    else:
                        break
                kwargs[name] = converted_value
            return func(*args, **kwargs)
        return wrapper
    return decorator
