class Solution:
    """
    target : 9
    [-1, 0, 3, 5, 9, 12]
     |         |      |
    left      mid    right

    1. 9 > mid => 變成看右邊的 [9, 12]，也就是 left 指向當前 mid 右邊
    [-1, 0, 3, 5, 9, 12]
                  |   |
                mid   right
                left


    """

    def search(self, nums: List[int], target: int) -> int:
        left_ptr, right_ptr = 0, len(nums) - 1

        while left_ptr <= right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2

            if nums[mid_ptr] == target:
                return mid_ptr
            elif target > nums[mid_ptr]:
                left_ptr = mid_ptr + 1
            else:
                right_ptr = mid_ptr - 1
        return -1
