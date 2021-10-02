# https://leetcode.com/contest/biweekly-contest-62/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def count_c(c):
            i, j, count = 0, 0, k
            ans = 0
            for j in range(len(answerKey)):
                if answerKey[j] == c: count -= 1
                if count >= 0: ans = max(ans, j-i+1)
                while count < 0:
                    if answerKey[i] == c: count += 1
                    i += 1
            return ans
        return max(count_c('T'), count_c('F'))