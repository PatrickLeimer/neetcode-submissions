class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False
        
        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))
        print(sortedS + "  +  " + sortedT)

        if sortedS == sortedT:
            return True

        return False