class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        prefix,postfix=1,1
        for i in range(1,len(nums)):
            res.append(nums[i-1]*prefix)
            prefix=res[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res