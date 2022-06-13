"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10**-4 are acceptable.


Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line 6 with  digits after the decimal. The function should not return a value.

Input Format:

The first line contains an integer, n , the size of the array.
The second line contains n space-separated integers that describe arr[n].

Constraints:
0<n<=100
-100<=arr[i]<=100



Output Format:

Print the following 3 lines, each to 6 decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667

Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive:3/6 = 0.500000 , negative: 2/6 = 0.333333  and zeros:1/6 = 0.166667.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#



def plusMinus(arr):
    # Write your code here
    # For each, count how many times its present in the array
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for a in arr:
        if(a != 0 and a > 0):positive_count=positive_count+1
        elif(a < 0):negative_count=negative_count+1
        elif(a == 0):zero_count=zero_count+1
   
    positive_ratio = ((positive_count/len(arr)))
    positive_ratio="{0:.6f}".format(positive_ratio)
    negative_ratio=((negative_count/len(arr)))
    negative_ratio="{0:.6f}".format(negative_ratio)
    zero_ratio=((zero_count/len(arr)))
    zero_ratio="{0:.6f}".format(zero_ratio)
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)
    # print('There are '+str(positive_count)+' positive numbers, '+str(negative_count)+' negative numbers, and '+str(zero_count)+' zero in the array. \n The proportions of occurrence are positive:'+str(positive_count)+'/'+str(len(arr))+' = '+str(positive_ratio)+' , negative: '+str(negative_count)+'/'+str(len(arr))+' = '+str(negative_ratio)+'  and zeros:'+str(zero_count)+'/'+str(len(arr))+' = '+str(negative_ratio)+'.')



if __name__ == '__main__':
    

    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
