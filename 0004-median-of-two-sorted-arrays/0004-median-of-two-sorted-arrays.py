class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr=nums1+nums2
        n=len(arr)
        arr.sort()
        mid=len(arr)//2
        if len(arr)%2!=0:
            
            return arr[mid]
        else:
            # mid=len(arr)/2
            return (arr[mid]+arr[mid-1])/2.0