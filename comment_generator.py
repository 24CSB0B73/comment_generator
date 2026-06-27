def generate_comment(func_name, params, return_expr):
    # Simple verb inference
    if func_name.startswith("add"):
        action = "adds"
    elif func_name.startswith("mul"):
        action = "multiplies"
    elif func_name.startswith("sub"):
        action = "subtracts"
    elif func_name.startswith("div"):
        action = "divides"
    else:
        action = "processes"

    params_str = ", ".join(params)

    comment = f"This function {action} {params_str} and returns {return_expr}."
    return comment
