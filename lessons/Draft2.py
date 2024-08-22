class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = str(format(num, 'b'))
        new_num = ''
        for i in bin_str:
            if i == '0':
                new_num += '1'
            else:
                new_num += '0'

        return int(new_num, 2)




ex = Solution()
ex.findComplement(5)
assert ex.findComplement(5) == 2
assert ex.findComplement(5) == 2, "Test case 1 failed"
assert ex.findComplement(1) == 0, "Test case 2 failed"
assert ex.findComplement(2) == 1, "Test case 3 failed"
assert ex.findComplement(3) == 0, "Test case 4 failed"
assert ex.findComplement(4) == 3, "Test case 5 failed"
assert ex.findComplement(30) == 1, "Test case 6 failed"  # 30 -> 11110 in binary, complement -> 00001
assert ex.findComplement(15) == 0, "Test case 7 failed"