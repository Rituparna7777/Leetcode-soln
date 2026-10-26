class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        emp = []
        for ele in nums1 :
            if ele in nums2 :
                emp.append(ele)
                nums2.remove(ele)
        return emp