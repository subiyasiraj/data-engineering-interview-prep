class Solution:
    # LeetCode 1: Two Sum (unsorted array) -> hash map, O(n) time, O(n) space
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index

        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i

    # LeetCode 167: Two Sum II (sorted array) -> two pointers, O(n) time, O(1) space
    def twoSumSorted(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1  # i = smallest value, j = largest value

        while i < j:  # stop when pointers meet, so one element is never used twice
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]  # problem wants 1-indexed
            elif s < target:
                # Sum too small -> need a bigger sum.
                # Array is sorted, so moving i right gives a larger value.
                i += 1
            else:
                # Sum too big -> need a smaller sum.
                # Array is sorted, so moving j left gives a smaller value.
                j -= 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 3], 6))               # [0, 1]
    print(sol.twoSumSorted([-1, 0], -1))       # [1, 2]
    print(sol.twoSumSorted([2, 7, 11, 15], 9)) # [1, 2]
    print(sol.twoSumSorted([2, 3, 4], 6))      # [1, 3]