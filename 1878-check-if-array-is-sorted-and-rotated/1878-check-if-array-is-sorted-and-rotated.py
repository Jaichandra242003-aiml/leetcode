class Solution(object):
    def check(self, nums):
        count = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
            if count>1:
                return False
        if nums[-1]>nums[0]:
            count+=1
        if count>1:
            return False
        return True
        