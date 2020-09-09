class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_len = len(nums1) + len(nums2)
        midpoint = total_len // 2
        result = []
        j = 0
        k = 0
        for i in range(0, midpoint + 1):
            if j == len(nums1):
                result.append(nums2[k])
                k += 1
            elif k == len(nums2):
                result.append(nums1[j])
                j += 1
            elif (nums1[j] < nums2[k]):
                result.append(nums1[j])
                j += 1
            else:
                result.append(nums2[k])
                k += 1
        if (total_len % 2):
            return result[midpoint]
        else:
            return (result[midpoint] + result[midpoint - 1]) / 2
sol = Solution()
print(sol.findMedianSortedArrays([1, 2, 3], [2, 3, 4]))
  

'''
    def findMedianSortedArrays(self, nums1, nums2) -> float:
      flattened = nums1 + nums2
      arr_len = len(flattened)
      flattened.sort()
      mid = arr_len//2
      if arr_len % 2 == 1:
        return flattened[mid]
      else:
        return (flattened[mid] + flattened[mid - 1]) / 2
'''
'''
First attempt at a solution faster than log(m+n)
sol = Solution()
print(sol.findMedianSortedArrays([1, 2, 3], [2, 4, 6 ,7]))

        total_len = len(nums1) + len(nums2)
        midpoint = total_len // 2
        j = 0
        k = 0
        if not nums1:
            if total_len % 2 == 1:
                return nums2[midpoint]
            else: 
                return (nums2[midpoint] + nums2[midpoint - 1])/2
        elif not nums2:
            if total_len % 2 == 1:
                return nums1[midpoint]
            else: 
                return (nums1[midpoint] + nums1[midpoint - 1])/2
            
        for i in range(0, midpoint - 1):
            if nums1[k] > nums2[j]:
                j += 1
            else:
                k += 1
        if total_len % 2 == 1:
            print(nums2[j])
            if len(nums1) < len(nums2):
                return min(nums1[k], nums2[j])
            else:
                return max(nums1[k], nums2[j])
        else:
            return (nums1[k] + nums2[j])/2
  '''