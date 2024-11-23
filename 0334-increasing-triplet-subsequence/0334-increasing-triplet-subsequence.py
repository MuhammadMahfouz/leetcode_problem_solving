class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = [float('inf'), float('inf'), float('inf')]

        for num in nums:
            if num <= t[0]:
                t[0] = num
            elif num <= t[1]:
                t[1] = num
            else:
                return True
        return False
    
        