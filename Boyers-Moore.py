NO_OF_CHARS = 256

# Bad Character Heuristic
def badCharHeuristic(pattern):
    badchar = [-1] * NO_OF_CHARS
    for i in range(len(pattern)):
        badchar[ord(pattern[i])] = i
    return badchar

# Preprocessing for the strong good suffix rule
def preprocessStrongSuffix(shift, bpos, pattern, m):
    i = m
    j = m + 1
    bpos[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j

# Preprocessing for good suffix rule case 2
def preprocessCase2(shift, bpos, m):
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]

# Boyer-Moore Search Algorithm
def BoyerMooreSearch(text, pattern):
    m = len(pattern)
    n = len(text)
    badchar = badCharHeuristic(pattern)
    bpos = [0] * (m + 1)
    shift = [0] * (m + 1)

    preprocessStrongSuffix(shift, bpos, pattern, m)
    preprocessCase2(shift, bpos, m)

    s = 0  # shift of the pattern with respect to text
    found = False

    while s <= n - m:
        j = m - 1

        # Decrease j while characters match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # Pattern found
        if j < 0:
            print(f"Pattern occurs at shift = {s}")
            found = True
            s += shift[0]
        else:
            badCharShift = j - badchar[ord(text[s + j])]
            goodSuffixShift = shift[j + 1]
            s += max(goodSuffixShift, badCharShift)

    if not found:
        print("Pattern not found")

# Main driver
if __name__ == "__main__":
    text = input("Key in the Text: ")
    pattern = input("Key in the Pattern: ")
    BoyerMooreSearch(text, pattern)
