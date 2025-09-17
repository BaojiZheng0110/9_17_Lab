from typing import List


def MaxCrossingSum(nums: List[int], left: int, mid: int, right: int) -> int:
    #Calaulate the sum of the left half
    LeftSum = float('-inf') #-infinity, initial number to search for max
    total = 0
    for i in range(mid, left - 1, -1):   #from mid to left
        total += nums[i]
        if total > LeftSum:
            LeftSum = total

    #Calculate the sum of the right half
    RightSum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):     #from mid+1 to right
        total += nums[i]
        if total > RightSum:
            RightSum = total

    return LeftSum + RightSum # Return sum of elements on left and right of mid

#Using divide and conquer to find the maximum subarray sum
def MaxSubarraySum(nums: List[int], left:int, right:int) -> int:
    # if there is only one element, return that element
    if left == right:
        return nums[left]
    mid = (left + right) // 2           #Find the midpoint of the array
    LeftMax = MaxSubarraySum(nums, left, mid)           #Maximum subarray sum in left half
    RightMax = MaxSubarraySum(nums, mid + 1, right)     #Maximum subarray sum in right half
    CrossMax = MaxCrossingSum(nums, left, mid, right)   #Maximum subarray sum crossing the midpoint

    return max(LeftMax, RightMax, CrossMax)# Return the maximum of the three


# Public function to find the maximum subarray sum
def FindMaxSubarraySum(nums: List[int]) -> int:
    if not nums:
        raise ValueError("Input array must not be empty.")
    return MaxSubarraySum(nums, 0, len(nums) - 1)
    
if __name__ == "__main__":
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Example 1:", FindMaxSubarraySum(nums1))

    nums2 = [1]
    print("Example 2:", FindMaxSubarraySum(nums2))

    nums3 = [1, 2, 3, -2, 5]
    print("Example 3:", FindMaxSubarraySum(nums3))