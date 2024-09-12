from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        for word in words:
            for sym in word:
                if sym not in allowed:
                    break
            else:
                result += 1

        return result


ex = Solution()
assert ex.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]) == 2
assert ex.countConsistentStrings("abc",["a","b","c","ab","ac","bc","abc"]) == 7
assert ex.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"] ) == 4
