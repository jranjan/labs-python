class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dc = len(digits)
        carry = 1 if digits[dc - 1] == 9 else 0
        for i in range(dc):
            if digits[dc - i - 1] + carry > 9:
                digits[dc - i - 1] = 0
                carry = 1
            else:
                digits[dc - i - 1] = digits[dc - i - 1] + 1
                carry = 0
                break

        print digits
        if carry == 1:
            digits.insert(0, 1)

        return digits

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([8, 9,9,9]))