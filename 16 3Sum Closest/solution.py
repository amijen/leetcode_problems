class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        closest_sum = 0
        for i in range(len(nums)):
            fixed = nums[i]
            right = len(nums) - 1
            left = i + 1
            while left < right: 
                result = fixed + nums[left] + nums[right]
                current_diff = abs(target - result)
                if current_diff < diff : 
                    diff = current_diff
                    closest_sum = result
                
                if result == target: 
                    return closest_sum
                    
                if result > target : 
                    right -= 1
                else:
                    left +=1
                    
        return closest_sum