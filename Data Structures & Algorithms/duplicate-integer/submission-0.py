class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numHash = dict()        
        for num in nums:
        # print(numHash.get(num))
            if numHash.get(num):
                return True 
            else:
                numHash[num] = True
        return False 