def longestCommonPrefix(words: list) -> str:
    short = min(words, key=len)
    m = len(short)
    prefiks = ""

    for i in range(m):
        for word in words:
            if short[i] != word[i]:
                return prefiks
        prefiks = short[:i + 1]

    return short
