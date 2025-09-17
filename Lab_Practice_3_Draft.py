# Lab Practice #3
# Maximum Subarray Sum using Divide and Conquer
#
# This implementation finds the subarray with the largest sum in a given integer array.
# The algorithm uses the divide-and-conquer approach, which has a time complexity of O(n log n).
#
# Time Complexity Explanation:
# - The array is recursively divided into two halves (log n levels of recursion).
# - At each level, we compute the maximum crossing sum in O(n) time.
# - Thus, the total time complexity is O(n log n).

from typing import List

def max_crossing_sum(nums: List[int], left: int, mid: int, right: int) -> int:
	"""
	Helper function to find the maximum sum of a subarray crossing the midpoint.
	"""
	# Include elements on left of mid
	left_sum = float('-inf')
	total = 0
	for i in range(mid, left - 1, -1):
		total += nums[i]
		if total > left_sum:
			left_sum = total

	# Include elements on right of mid
	right_sum = float('-inf')
	total = 0
	for i in range(mid + 1, right + 1):
		total += nums[i]
		if total > right_sum:
			right_sum = total

	# Return sum of elements on left and right of mid
	return left_sum + right_sum

def max_subarray_sum(nums: List[int], left: int, right: int) -> int:
	"""
	Recursive function to find the maximum subarray sum using divide and conquer.
	"""
	# Base case: only one element
	if left == right:
		return nums[left]

	mid = (left + right) // 2

	# Maximum subarray sum in left half
	left_max = max_subarray_sum(nums, left, mid)
	# Maximum subarray sum in right half
	right_max = max_subarray_sum(nums, mid + 1, right)
	# Maximum subarray sum crossing the midpoint
	cross_max = max_crossing_sum(nums, left, mid, right)

	# Return the maximum of the three
	return max(left_max, right_max, cross_max)

def find_max_subarray_sum(nums: List[int]) -> int:
	"""
	Public function to find the maximum subarray sum.
	"""
	if not nums:
		raise ValueError("Input array must not be empty.")
	return max_subarray_sum(nums, 0, len(nums) - 1)

# Example usage and test cases
if __name__ == "__main__":
	# Example 1
	nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	print("Example 1:", find_max_subarray_sum(nums1))  # Output: 6

	# Example 2
	nums2 = [1]
	print("Example 2:", find_max_subarray_sum(nums2))  # Output: 1

	# Example 3
	nums3 = [5, 4, -1, 7, 8]
	print("Example 3:", find_max_subarray_sum(nums3))  # Output: 23

#
# Time Complexity:
# The divide-and-conquer approach splits the array into two halves recursively (log n levels).
# At each level, the crossing sum is computed in O(n) time.
# Therefore, the total time complexity is O(n log n).
	left_sum = total

	# Include elements on right of mid
	right_sum = float('-inf')
	total = 0
	for i in range(mid + 1, right + 1):
		total += nums[i]
		if total > right_sum:
			right_sum = total

	# Return sum of elements on left and right of mid
	return left_sum + right_sum					