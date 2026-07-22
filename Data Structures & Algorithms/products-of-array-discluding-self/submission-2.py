class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        Okay I know for sure how to solve it using an O(n^2) approach,
        the thing is I need to figure out a O(n) approach
        would division work for every, not how you would think about it

        This kinda sounds like DP, where there are repeated steps mmmmm idk
        I'll do the O(n^2) and then figure out a more optimal way

        Reflection:
        I started out with an O(n^2) which was not even fully working, then I came to this back and forward O(n), I got here with a little help tbh
        My mind was not comprehending the backwards part, so I needed some help with the loop, but I realized its a python thing, if it was c like i just i--
        I can't say this was easy, but I understand it which is what matters now

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
