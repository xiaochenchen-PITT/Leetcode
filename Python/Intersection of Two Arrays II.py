class Solution(object):
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
            
        ret = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    move = 0
                    while move + i < len(nums1) and j + move < len(nums2):
                        if nums1[i + move] == nums2[j + move]:
                            move += 1
                        else:
                            break
                    ret += nums1[i : i + move]
        return ret