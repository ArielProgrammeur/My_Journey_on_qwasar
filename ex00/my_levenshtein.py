def my_levenshtein (s1,s2):
    if len(s1) != len(s2):
        return -1
    diff = 0
    for i in range (len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    return diff

