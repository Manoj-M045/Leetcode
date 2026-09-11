class Solution {
    public int maxArea(int[] height) {
        int l=0;
        int r=height.length-1;
        int ms=0;
        int cs;
        for(int i=0;i<height.length;i++)
        {
            int w=r-l;
            cs=Math.min(height[r],height[l])*w;
            ms=Math.max(cs,ms);

            if(height[l]<height[r])
            {
                l++;
            }
            else
            {
                r--;
            }

        }
        return ms;
        
    }
}