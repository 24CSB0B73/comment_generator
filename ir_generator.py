def generate_ir(feature):

    ir = {
        "type": "function",
        "name": feature["name"],
        "parameters": feature["parameters"],
        "operations": feature["operations"],
        "has_loop": feature["has_loop"],
        "has_condition": feature["has_condition"],
        "return": feature["return_value"]
    }

    return ir