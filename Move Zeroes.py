'''class Solution:
    def moveZeroes(self, nums: int) -> None:
        self.nums = nums

        for i in range(len(self.nums)):
            if self.nums[i] == 0:
                self.nums.append(self.nums[i])
                self.nums.remove(0)
        
        return self.nums'''
    




x = [[0]]
x = x + x * 2
#x[0].append(1)
print(x)
