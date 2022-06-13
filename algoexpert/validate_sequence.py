"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array
  but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4]
  form a sequence of the array [1, 2, 3, 4], and so do the numbers [2, 4].
  Note that a single number in an array and the array itself are both valid subsequences of the array.

  Sample Input
  ------------
  array  = [5, 1, 22, 25, 6, -1, 8, 10]
  sequence  = [1, 6, -1, 10]

  Sample Output
  -------------
  true

"""


array  = [1, 1, 1, 1, 1]
sequence  = [1, 1, 1]
def isValidSubsequence(array, sequence):
    # Write your code here.
    new_array = array.copy()
    [new_array.remove(a) for a in array if a not in sequence]
    if(new_array == sequence):return True
    elif(new_array[:len(sequence)] == sequence):return True
    else:return False

isValidSubsequence(array, sequence)