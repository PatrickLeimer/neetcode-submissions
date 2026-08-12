class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        First consider that there are 3 scenarios,
        when the target is the number in the middle
        when the target is less than
        when the target is more than

        '''


        low = 0 
        high = len(nums) - 1 

        while low <= high: 

            mid = (low + high) // 2
            print(mid, nums[mid])

            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else: 
                high = mid - 1
        
        return -1 