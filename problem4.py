#!/usr/bin/python3
"""
finding the median of two sorted arrays
"""
def findMedianSortedArrays(nums1, nums2):
	# ensure that nums1 is the smaller array
	if len(nums1) > len(nums2):
		nums1, nums2 = nums2, nums1
	
	# get length of both arrays
	m, n = len(nums1), len(nums2)

	# caluclate the total length and half length (for median calcualtion)
	total_length = m + n
	half_lenth = (total_length + 1) // 2

	# initialize binary search range for nums1
	left, right = 0, m

	# perform binary search on nums1
	while (left <= right):
		# partition nums1
		partition_nums1 = (left + right) // 2
		# calculate partition for nums2 based on partition of nums1
		partition_nums2 = half_length - partition_nums1

		# get elements around partitions
		max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partion_nums1 - 1]
		min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]

		max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
		min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partion_nums2]
		# check if the partions are correct
		if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
		# calculate median based on even or odd total length
			if total_length % 2 == 0:
				return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) // 2
			else:
				return max(max_left_nums, max_left_nums2)
		# adjust binary search engine
		elif max_left_nums1 > min_right_nums2:
			right = partitions_nums1 - 1
		else:
			left = partion_nums1 + 1
	raise ValueError("Input arrays are not sorted.")
