class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        dic = {"0": "", "1": "", "2":"ABC", "3":"DEF", "4":"GHI", "5":"JKL", "6":"MNO", "7":"PQRS", "8":"TUV", "9":"WXYZ"}
        res = []
        digits = [num for num in digits if num.isdigit()]
        self.dfs(digits, dic, 0, [], res)
        return res

    def dfs(self, digits, dic, index, tempList, res):
        if len(tempList) == len(digits):
            res.append(''.join(tempList))
            return 
        for c in dic[digits[index]]:
                #choose
                tempList.append(c)
                #explore
                self.dfs(digits, dic, index+1, tempList, res)
                #undo
                tempList.pop()

sol = Solution()
print(sol.letterCombinations("35%"))