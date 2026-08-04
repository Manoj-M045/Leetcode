class Solution:
    def maxArea(selfeigh, height: List[int]) -> int:
        ms=0
        l=0
        r=len(height)-1
        while(l<r):
            w=r-l
            cs=min(height[l],height[r])*w
            ms=max(cs,ms)
            if(height[l]<height[r]):
               l=l+1
            else:
               r=r-1
        return ms
        