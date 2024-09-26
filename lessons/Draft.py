from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        temp_res = 0
        prev_sym = s[0]
        for curr_sym in s:
            if roman_numerals[prev_sym] < roman_numerals[curr_sym]:
                if curr_sym == 'V':
                    result += 4
                elif curr_sym == 'X':
                    result += 9
                elif curr_sym == 'L':
                    result += 40
                elif curr_sym == 'C':
                    result += 90
                elif curr_sym == 'D':
                    result += 400
                elif curr_sym == 'M':
                    result += 900

            else:
                temp_res += roman_numerals[curr_sym]

        return result



ex = Solution()
assert ex.romanToInt("III") == 3
assert ex.romanToInt('LVIII') == 58
assert ex.romanToInt('MCMXCIV') == True

