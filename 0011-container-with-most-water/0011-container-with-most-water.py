class Solution:
    def maxArea(selfeigh, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ms=0
        while(l<r):
            width=r-l
            heights=min(height[l],height[r])
            area=heights*width
            if(area>=ms):
                ms=area
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return ms
        