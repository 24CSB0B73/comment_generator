def complex(a, b):
    result = (a + b) * (a % b)
    if result > 10:
        return result ** 2
    return result