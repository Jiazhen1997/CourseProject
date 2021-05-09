

from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        return not (
            rec1[2] <= rec2[0] or  
            rec1[0] >= rec2[2] or  
            rec1[1] >= rec2[3] or  
            rec1[3] <= rec2[1]     
        )


    def isRectangleOverlap_error(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] > rec2[0]:
            return self.isRectangleOverlap(rec2, rec1)

        return (
            rect1[0] < rect2[0] < rec1[2] and
            (
                rec2[1] < rect1[3] < rect2[3] or
                rec2[3] < rect1[3] < rect2[1]
            )
        )
