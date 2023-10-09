# def rotate_array(nums, k):
#     if k == 0:
#         return nums

#     n = len(nums)
#     k = k % n  # Handle cases where k is greater than the array length
#     print(k)
#     for _ in range(k):
#         temp = nums[-1]  # Store the last element
#         for i in range(n - 1, 0, -1):
#             nums[i] = nums[i - 1]  # Shift elements to the right
#         nums[0] = temp  # Place the stored element at the beginning

# # Example usage:
# nums = [1, 2, 3, 4, 5, 6, 7]
# rotate_array(nums, 3)
# print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

def rotate_array(nums, k):
    if k == 0:
        return nums

    n = len(nums)
    k = k % n  
    def reverse(start, end):
      while start<end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end   -= 1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums, 3)
print(nums)
