class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # for i in range(len(digits) - 1, -1, -1):
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits
        #     digits[i] = 0
        #
        # digits.insert(0, 1)
        # return digits

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1, *digits]

if __name__ == '__main__':
    digits = [1, 9, 9]
    print(Solution().plusOne(digits))

