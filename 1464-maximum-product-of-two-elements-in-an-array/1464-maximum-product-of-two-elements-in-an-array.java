class Solution {
    public int maxProduct(int[] nums) {
        int s=0;
        int e=nums.length-1;
        int m;
        int max=0;
        while(s<e){
            m=(nums[s]-1)*(nums[e]-1);
            if(m>max){
                max=m;
            }
            if(nums[s]<=nums[e]){
                s+=1;
            }
            else if(nums[e]<nums[s]){
                e-=1;
            }
        }
        return max;
        
    }
}