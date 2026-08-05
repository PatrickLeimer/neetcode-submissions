class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Right away I think of a dictionary, let me jump into that

        Reflection:
        For some reason I was making this more complicated than it had to be, create dictionary, sort it by key value using lambda function,
        item : item[1] means it sorts by integers, if it was item[0] it would do alphabetically, items() accesses both items in dicitonary, and then we append a key for each iteration
        then we cap by [:k] which means keep values until k amount remember start:stop:skip

        '''

        count = {}
        result = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else: 
                count[num] += 1
        
        result = [key for key, val in sorted(count.items(), key=lambda item: item[1], reverse=True)][:k]

        return result

            