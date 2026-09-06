class Solution:
    def helper(self,s,t,i,j,dp):
        if j==len(t):
            return 1
        if i==len(s):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==t[j]:
            take = self.helper(s,t,i+1,j+1,dp)
            skip = self.helper(s,t,i+1,j,dp)
            ans = take + skip
        else:
            ans = self.helper(s,t,i+1,j,dp)
        dp[i][j]  = ans
        return ans
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for _ in range(len(t)+1)]for _ in range(len(s)+1)]
        return self.helper(s,t,0,0,dp)