"""

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
arr = [1,3,5,7,9]

The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24, The function prints 
16, 24

Contraints:
1<=arr[i]<=10**9

Sample Input:
1 2 3 4 5

Sample Output:
10 14


"""

arr: list = [1,3,5,7,9]
arr2 = arr.copy()
start1 = 0
start2 = 0
arr.sort()
arr2.sort(reverse=True)
set1 = [start1:= start1 + i for index, i in enumerate(arr) if index < (len(arr) - 1)]
set2 = [start2:= start2 + i for index, i in enumerate(arr2) if index < (len(arr2) - 1)]
print (str(set1[-1])+' '+str(set2[-1]))
