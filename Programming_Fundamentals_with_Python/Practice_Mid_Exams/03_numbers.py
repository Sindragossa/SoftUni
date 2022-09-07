nums = list(map(int, input().split()))
average = sum(nums) / len(nums)

nums = sorted([num for num in nums if num > average])
nums.reverse()

while len(nums) > 5:
    nums.remove(min(nums))

if len(nums) >= 1:
    print(' '.join(list(map(str, nums))))
else:
    print('No')