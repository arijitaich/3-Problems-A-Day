"""
THREE NUMBER SUM

Write a function that takes in a non-empty array of distinct integers representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input:
-------------
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample Output:
--------------
[[-8,2,6], [-8,3,5], [-6,1,5]]

"""

def fetch_pair(nums, target):
    # nums = [2,7,11,15]

    # target = 9
    npacket = []
    input = list(enumerate(nums))
    lent = len(input)
    for in1, i1 in input:
        packet = []
        for in2, i2  in input:
            total = i1 + i2
            if(lent == 2 and total == target):
                if (i1 not in packet):packet.append(i1)
                if (i2 not in packet):packet.append(i2)
                break       
            elif(total == target and in1!=in2):            
                if (i1 not in packet):packet.append(i1)
                if (i2 not in packet):packet.append(i2)
                break
        packet.sort()
        if(len(packet) == 2 and packet not in npacket):npacket.append(packet)
    return npacket


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
array.sort()
# print(array)

# Sort the array by value descending.
# Start from the negative values
# [-8, -6, 1, 2, 3, 5, 6, 12]
# Fetch the pair that would add up to the first value of the array that is selected here.
# Insert Into New Packet Of 2 Dimensional Array
npacket2 = []
for a in array:
    npacket1: list = []
    npacket1.append(a)
    new_array = [i for i in array if i != a]
    remaining_from_target = targetSum - a
    new_pair = fetch_pair(new_array, remaining_from_target)
    # print(new_pair)
    for np in new_pair: 
        npacket1: list = []
        npacket1.append(a)
        #   print(np)
        if (len(np) == 2):
            for np2 in np:
                # print('Current Value: '+str(a))
                # print('Target Value: '+str(targetSum))
                # print('Remaning Target Value: '+str(remaining_from_target))
                # print('Current Array Set: '+str(np))
                # print('Current Array Set Value: '+str(remaining_from_target))
                npacket1.append(np2)
                # print('Updated Array Set: ')
                # print(npacket1)
                # print('')
            npacket1.sort()
            if(npacket1 not in npacket2):npacket2.append(npacket1)
    # print('')

print(npacket2)

