class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        """
    Every word has to go into one group
    every time we iterate in the array, we can add to one subarray or create a new one
    
    Sort the string so that it always matches 
    we can always just grab the first item in the groups to compare because they are anagrams 
    
    Reflection:
        KILL ME, for some reason i forgot to add the [0] to access the first item on the sublist I was iterating through and that was killing my entire logic
        therefore, this easy problem took me so long to debug. Buut, slowly getting the hang of python, practice makes perfect
        """
    
        result = []
        result.append([strs[0]])

        for i in range (1, len(strs)):
            matched = False
            temp = "".join(sorted(strs[i]))
            
            for j in range(len(result)):

                if temp == "".join(sorted(result[j][0])):
                    result[j].append(strs[i])
                    matched = True 

            if not matched: 
                result.append([strs[i]])
                    
        
        return result