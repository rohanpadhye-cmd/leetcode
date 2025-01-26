class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        if len(text) % 2 != 0:
            
            mid_index = len(text) // 2
            a = text[:mid_index]  
            middle = text[mid_index]  
            b = text[mid_index+1:]

            if (a == b[::-1]):
                return True
            return False  

        else:
            
            a = text[:len(text)//2]
            b = text[len(text)//2:]
            if (a == b[::-1]):
                return True
            return False  
