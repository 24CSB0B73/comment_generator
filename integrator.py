def insert_comments_into_code(code, comments):

    lines = code.split("\n")
    new_code = []
    comment_index = 0

    for i, line in enumerate(lines):
        new_code.append(line)

        # Detect function definition
        if line.strip().startswith("def ") and comment_index < len(comments):

            indent = " " * (len(line) - len(line.lstrip()) + 4)

            comment = comments[comment_index]

            # Add docstring after function definition
            new_code.append(f'{indent}"""{comment}"""')

            comment_index += 1

    return "\n".join(new_code)