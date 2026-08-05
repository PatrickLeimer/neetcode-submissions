class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Okay I def understand stacks, i just couldn't visualize how to use here, 
        but now I see is by checking the stack is empty is you can tell they all close 
        
        Reflection: 
        Go through the array, check if the current element is a key, then if the stack is not empty 
        and the last in is equal to the value in dictionary (we close the open bracket) 
        if it can't be closed then return false right away
        then at the end return True only when stack is empty, which means all open brackets have been closed

        OKAY I UNDERSTOOD YES
        '''

        stack = []
        chars = {')':'(', ']':'[', '}':'{' }

        for c in s: 
            if c in chars:
                if stack and stack[-1] == chars[c]: 
                    stack.pop()
                else: 
                    return False 
            else: 
                stack.append(c)
            
        return True if not stack else False
                



