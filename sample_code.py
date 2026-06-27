def add(a, b):
    return a + b


def process_numbers(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total