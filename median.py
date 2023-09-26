"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


def get_median(nums):
    nums.sort()

    if len(nums) == 1:
        return nums[0]

    if len(nums) % 2 == 0:
        return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2

    return nums[(len(nums))//2]


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(get_median(numbers))

