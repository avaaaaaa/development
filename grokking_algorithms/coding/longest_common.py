from combinations import find_comb


def lc_substring(s1, s2):
    lcs = []
    longer_str = ""
    shorter_str = ""
    
    if len(s1) > len(s2):
        longer_str = s1
        shorter_str = s2
    else:
        longer_str = s2
        shorter_str = s1
    
    offset = len(shorter_str)
    start = 0
    found = False

    while offset:
        substring = shorter_str[start:start+offset]
        if substring in longer_str:
            lcs.append(substring)
            found = True
        start += 1
        if start + offset > len(shorter_str):
            if found:
                break
            start = 0
            offset -= 1
    
    return lcs


def lc_subsequence(s1, s2):
    lcs = []
    longer_str = ""
    shorter_str = ""
    
    if len(s1) > len(s2):
        longer_str = s1
        shorter_str = s2
    else:
        longer_str = s2
        shorter_str = s1
    
    offset = len(shorter_str)
    found = False

    while offset:
        combs = find_comb(shorter_str, offset, 0)
        universal = find_comb(longer_str, offset, 0)
        for comb in combs:
            if comb in universal:
                string = "".join(comb)
                lcs.append(string)
                found = True
        if found:
            break
        offset -= 1

    return lcs

"""
s1 = ["acbad", "abcwwwbcd"]
s2 = ["abcd", "abcd"]


for i in range(len(s1)):
    print(s1[i], s2[i])
    print("substring:", lc_substring(s1[i], s2[i]))
    print("subsequence:", lc_subsequence(s1[i], s2[i]))
    print()
#"""