def result_type(nums):
    if 0 in nums:
        return 'zero'
    negative = 0

    for n in nums:
        if n < 0:
            negative += 1

    if negative % 2 == 0:
        return 'positive'
    return 'negative'


numbers = [int(input()) for n in range(3)]
print(result_type(numbers))