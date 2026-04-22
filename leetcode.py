platform: leetcode
problem no: 1
program:
i=0
        while i<len(nums):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
            i=i+1
Sol=Solution()
result=Sol.twoSum([2,7,11,15],9)
print(result)
