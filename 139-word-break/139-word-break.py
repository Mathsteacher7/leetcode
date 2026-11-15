def wordBreak(s: str, wordDict: list[str]) -> bool:
    ok = [False] * (len(s) + 1)
    ok[0] = True
    word_dict_as_set = set(wordDict)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if ok[j] and s[j:i] in word_dict_as_set:
                ok[i] = True
                break
    return ok[-1]
