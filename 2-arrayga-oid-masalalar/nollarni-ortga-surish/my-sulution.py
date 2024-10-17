def moveZeroes(nums: list) -> list:
    new_nums = []
    a = 0
    for i in nums:
        if i>0:
            new_nums.append(i)
        if i==0:
            a+=1
    for j in range(a):
        new_nums.append(0)
    return new_nums

