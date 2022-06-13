"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

        print('Checking '+str(i1)+'+'+str(i2)+'='+str(total))
"""

# Input: nums = [2,7,11,15], target = 9
nums = [2,7,11,15]

target = 9
packet = []
input = list(enumerate(nums))
lent = len(input)
for in1, i1 in input:
    for in2, i2  in input:
        total = i1 + i2
        if(lent == 2 and total == target):
            if (in1 not in packet):packet.append(in1)
            if (in2 not in packet):packet.append(in2)
            break       
        elif(total == target and in1!=in2):            
            if (in1 not in packet):packet.append(in1)
            if (in2 not in packet):packet.append(in2)
            break
print(packet)