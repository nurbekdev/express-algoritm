# Ro'yxat kvadrati
# Sizga berilgan sonlar ro'yxati o'sish tartibida saralangan.
# Har bir elementning kvadratini hisoblab, natijani saralangan holda qaytaring.
def sortedSquares(nums: list) -> list:
    i, j = 0, len(nums)-1
    result = []

    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            result.append(nums[j]**2)
            j -= 1
        else:
            result.append(nums[i]**2)
            i += 1
    result.reverse()
    return result


