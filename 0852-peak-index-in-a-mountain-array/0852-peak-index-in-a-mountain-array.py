class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        s=1
        e=len(arr)-2
        while(s<=e):
            mid=(s+e)//2
            if(arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid-1]>arr[mid]):
                e=mid-1
            else:
                s=mid+1
        