def productExceptSelf(nums: list) -> list:
    prefix = [1]
    suffix = [1]

    product = 1
    for num in nums:
        product *= num
        prefix.append(product)

    product = 1
    for num in reversed(nums):
        product *= num
        suffix.append(product)
    suffix.reverse()

    result = []
    for i in range(len(nums)):
        left, right = 1, 1
        left = prefix[i]
        right = suffix[i+1]
        prod = left * right
        result.append(prod)
    return result