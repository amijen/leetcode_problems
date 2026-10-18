class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        max_length = len(nums1) + len(nums2)
        res = []
        if max_length % 2 == 0:
            for i in range(int(max_length/2)+1) :
                if nums1 and nums2 :
                    if nums1[0] < nums2[0]:
                        res.append(nums1[0])
                        del nums1[0]
                    else:
                        res.append(nums2[0])
                        del nums2[0]
                elif nums1 :
                    res.append(nums1[0])
                    del nums1[0]
                elif nums2:
                    res.append(nums2[0])
                    del nums2[0]
            return (res[-1] + res[-2]) / 2 
        else :
            for i in range(max_length // 2 +1):
                if nums1 and nums2 :
                    if nums1[0] < nums2[0]:
                        res.append(nums1[0])
                        del nums1[0]
                    else:
                        res.append(nums2[0])
                        del nums2[0]
                elif nums1 :
                    res.append(nums1[0])
                    del nums1[0]
                elif nums2:
                    res.append(nums2[0])
                    del nums2[0]
            return res[-1]