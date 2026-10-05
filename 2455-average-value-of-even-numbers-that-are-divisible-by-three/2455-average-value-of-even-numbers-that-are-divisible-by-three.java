class Solution {
    public int averageValue(int[] nums) {
        int c=0;
        int s=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0 && nums[i]%3==0){
                c+=1;
                s=s+nums[i];
            }
        }
        if(c==0){
            return 0;
        }
        else{
            return s/c;
        }
        
    }
}