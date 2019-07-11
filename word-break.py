

# def wordBreak(s, wordDict):
#     n = len(s)
#     string = list(s)
#     dp = [[0]*n]*n

#     new_s = ''

#     for i in range(n):
#         new_s += string[i]
#         if new_s in wordDict:
#             dp[0][i] = 1
        

#     for i in range(1, n):
#         new_s = '' 
#         for j in range(i, n):
#             new_s += string[j]
#             if new_s in wordDict:
#                 if dp[i-1][i-1]:
                
#                     dp[i][j] = 1

#     print(dp)

#     print(dp[n-1][n-1])

# wordBreak("catsandog" ,["cats", "dog", "sand", "an", "cat"])


# arr = []
# def wordBreak(s, wordDict, now='', string=''):
#     if not s:
#         import ipdb;ipdb.set_trace()
#         if string:
#             arr.append(string)
#         return True

#     for i in s:
#         now += i
#         if now in wordDict:
#             string += now if not string else " {}".format(now) 
#             wordBreak(s.replace(now, "", 1), wordDict, string=string)
                
#     return arr


arr = []
import re
def wordBreak(os, s, wordDict, now='', string=''):
    if not s:
        
        if string:
            arr.append(string)
        return True

    for i in range(len(s)+1):
        if s[:i] in wordDict:
            import ipdb;ipdb.set_trace()
            if len(string) - len(re.findall(string, " ")) + len(s[:i]) >= i :
                string  = os[:i]

            string += s[:i] if not string else " {}".format(s[:i]) 

            x= 1
            y=2
            wordBreak(os, s[i:], wordDict, string=string)
                
    return arr

# "catsanddog"
# ["cat","cats","and","sand","dog"]
# "pineapplepenapple"
# ["apple","pen","applepen","pine","pineapple"]
# print(wordBreak("pineapplepenapple" , ["apple","pen","applepen","pine","pineapple"]))
print(wordBreak("catsanddog","catsanddog" , ["cat","cats","and","sand","dog"]))
            



