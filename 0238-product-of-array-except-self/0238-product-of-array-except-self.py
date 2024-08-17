class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        left_prod_list = [1]
        right_prod_list = [1]

        final_left_prod = 1
        final_right_prod = 1
        for i in range(1, n):
        #print("i", i)
            final_left_prod *= nums[i-1]
            #print("final left prod", final_left_prod)
            left_prod_list.append(final_left_prod)
            #print("left prod", left_prod_list)
            final_right_prod *= nums[n-i]
            right_prod_list.append(final_right_prod)
            #print("right prod", right_prod_list)
            #print("=============================================")
        right_prod_list.reverse()
        for i in range(n):
            ans.append(left_prod_list[i] * right_prod_list[i])
        return ans