def analyze_ir(ir):

    analysis = []

    if ir["has_loop"]:
        analysis.append("contains iteration")

    if ir["has_condition"]:
        analysis.append("uses conditional logic")

    if ir["operations"]:
        analysis.append(f"performs {ir['operations'][0]}")

    if not analysis:
        analysis.append("simple computation")

    return analysis