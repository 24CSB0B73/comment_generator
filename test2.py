def find_even(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result