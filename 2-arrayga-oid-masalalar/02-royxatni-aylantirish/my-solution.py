def rotate(nums: list, k: int) -> list:
    for i in range(k):
        nums.insert(0, nums.pop())

    return nums