class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.robLinear(nums[1:]), nums[0] + self.robLinear(nums[2:-1]))

    # this is the algorithm for House Robber I
    def robLinear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        d = {}
        d[len(nums)-1] = nums[-1]
        d[len(nums)-2] = max(d[len(nums)-1], nums[-2])
        for i in xrange(len(nums)-3, -1, -1):
            d[i] = max(d[i+1], nums[i] + d[i+2])
        return d[0]

test = Solution()
print test.rob([2,3,2]) # 3
print test.rob([1,2,3,1]) # 4
print test.rob([0]) # 0
