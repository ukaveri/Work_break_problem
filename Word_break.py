#word break:
"""

"""

def wordBreak(s, wordDict):
    word_set = set(wordDict)
    word_lengths = {len(word) for word in word_set}
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for l in word_lengths:
            if i - l >= 0 and dp[i - l] and s[i-l:i] in word_set:
                dp[i] = True
                break
        
    return dp[n]
s = "penballbook"
wordDict = {"pen","ball","book"}
print(wordBreak(s,wordDict))
