class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_num = max(candies)

        for candy in candies:
            if candy + extraCandies >= max_num:
                output.append(True)
            else:
                output.append(False)
        
        return output
