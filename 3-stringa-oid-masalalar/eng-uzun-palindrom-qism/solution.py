def expend(s, i, j):
    n = len(s)

    while i >= 0 and j < n and s[i] == s[j]:
        i -= 1
        j += 1

    return s[i + 1:j]


def longestPalindrome(s: str) -> str:
    n = len(s)
    answer = ""

    for i in range(n):
        pal_odd = expend(s, i, i)
        pal_even = expend(s, i, i + 1)

        answer = max([answer, pal_odd, pal_even], key=len)

        return answer