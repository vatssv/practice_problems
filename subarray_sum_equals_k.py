class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {}
        current_sum, count = 0, 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum - k in sums:
                count += sums[current_sum-k]
            if current_sum == k:
                count += 1
            if current_sum in sums:
                sums[current_sum] += 1
            else:
                sums[current_sum] = 1
            # print('Sums: ', sums)
        return count