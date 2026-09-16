class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int s=1;
        int e=arr.length-1;
        while(s<=e)
        {
            int mid=(s+e)/2;
            if(arr[mid-1]<arr[mid] && arr[mid]>arr[mid+1])
            {
                return mid;
            }
            else if(arr[mid-1]>arr[mid])
            {
                e=mid-1;
            }
            else
            {
                s=mid+1;
            }
        }
        
     return -1;   
    }
}