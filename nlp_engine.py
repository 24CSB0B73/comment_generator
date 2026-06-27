import random

operation_templates = {

    "addition": [
        "adds the given numbers",
        "computes the sum of the inputs"
    ],

    "subtraction": [
        "subtracts one number from another"
    ],

    "multiplication": [
        "multiplies the given numbers"
    ],

    "division": [
        "divides one number by another"
    ],

    "modulus": [
        "computes the remainder of division"
    ],

    "exponentiation": [
        "raises a number to a power"
    ],

    "floor division": [
        "performs floor division"
    ],

    "function call": [
        "calls another function"
    ]
}

loop_templates = [
    "iterates through the input values"
]

condition_templates = [
    "applies conditional checks"
]


def generate_nlp_comment(ir, analysis):

    comment_parts = []

    # 🔥 HANDLE IMPORTS + NORMAL OPS
    for op in ir["operations"]:

        if "uses" in op:
            comment_parts.append(op)

        else:
            comment_parts.append(
                random.choice(operation_templates.get(op, ["performs some operation"]))
            )

    # 🔹 Loop
    if ir["has_loop"]:
        comment_parts.append(random.choice(loop_templates))

    # 🔹 Condition
    if ir["has_condition"]:
        comment_parts.append(random.choice(condition_templates))

    # 🔹 Build sentence
    if comment_parts:
        sentence = "This function " + ", ".join(comment_parts)
    else:
        sentence = "This function processes input"

    # 🔹 Return
    if ir["return"]:
        sentence += f" and returns {ir['return']}"
    else:
        sentence += " and does not return any value"

    sentence += "."

    return sentence