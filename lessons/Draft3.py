def longestCommonPrefix(strs):
    res = ''
    min_len = len(min(strs, key=len))
    for i in range(min_len):
        for s in strs:
            x = strs[0][i]
            if s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))




















# res = ''
# for i in range(len(strs[0])):
#     for s in strs:
#         if i == len(s) or s[i] != strs[0][i]:
#             return res
#     res += strs[0][i]
#
# return res