class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        Okay I know for sure how to solve it using an O(n^2) approach,
        the thing is I need to figure out a O(n) approach
        would division work for every, not how you would think about it

        This kinda sounds like DP, where there are repeated steps mmmmm idk
        I'll do the O(n^2) and then figure out a more optimal way


        '''
        pre = 1
        result = []
        n = len(nums)

        for i in range(n):
            result.append(pre)
            pre *= nums[i]

        pre = 1
        
        for i in range(-1, -n - 1, -1 ):
            result[i] *= pre
            pre *= nums[i]

        return result
