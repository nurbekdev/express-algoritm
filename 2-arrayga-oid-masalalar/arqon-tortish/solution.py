def sign(num):
    if num < 0:
        return 1
    elif num > 0:
        return -1
    return 0

def leftRightDifference(nums: list) -> list:
    left, right = 0, sum(nums)
    result = []

    for num in nums:
        left += num
        result.append(sign(left-right))
        right -= num

    return result