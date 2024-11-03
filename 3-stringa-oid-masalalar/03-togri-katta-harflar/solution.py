def inrange(s, start, end):
    start, end = ord(start), ord(end)
    for char in s:
        if not start <= ord(char) <= end:
            return False
    return True

def isupper(s):
    return inrange(s, 'A', 'Z')

def islower(s):
    return inrange(s, 'a', 'z')

def detectCapitalUse(word: str) -> bool:
    if isupper(word) or islower(word):
        return True

    return isupper(word[:1]) and islower(word[1:])