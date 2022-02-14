from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
     b = sorted(items)
     
     if len(items) < 2 :
         return True
         
     elif b == items:
         
        for i in range (0, len(b)-1):
            
            if b[i]==b[i+1]:
                return False
            else:
                return True
     else:
        return False