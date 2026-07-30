class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        AYOOO whats up youtube
        okay condition is set, to find the consecutive sequence the element before has to be exactly 1 lower than next 
        entao
        if TRUE for nums[i] + 1 == nums[i + 1]
        then we can store into count, we also need a temporary count var
        else 
            set count to the current temp, and reset temp

        Reflection: 
        Definetely was able to understand the logic behind it, I was just running into minor issues
        But thats from forgetting python rules that I googled, but im glad because I am learning
        For some reason, I confused the touple data structure with the set, where I thought tuple didnt store repeated values 
        
        '''

        temp = 1
        count = 0
        nums = list(set(nums))
        nums.sort()
        
        if not nums:
            return 0
    
        print(nums)

        for i in range(len(nums) -1):
            if nums[i] + 1 == nums[i+1]: 
                temp += 1
                print('hi ', i, nums[i], temp)

            else:
                count = temp if temp > count else count
                temp = 1
        count = temp if temp > count else count
        
        return count 
                
