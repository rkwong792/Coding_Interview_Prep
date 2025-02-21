# A standard binary search will use l <= r which looks like:

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2 # Divison operation rounds down

            if nums[mid] > target:
                # we want to search left side
                r = mid - 1
            elif nums[mid] < target:
                # we want to search right side
                l = mid + 1
            else:
                return mid
        return -1
    
# You can see that the right and left pointers are incrementing/decrementing by one. This is an indication to use l <= r.
    
# Then there are some problems where the pointers are like:

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        # Tips:
        # Use while l < r for problems where you are shrinking a range by adjusting r = mid.
        # Use while l <= r for regular binary search where r = mid - 1.
        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                # The pivot happens on the right somewhere.
                l = mid + 1
            else:
                r = mid
        
        return nums[l]


    # These 