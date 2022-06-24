"""

Given an array of integers, where all elements but one occur twice, find the unique element.

Example
a = [1,2,3,4,3,2,1]
The unique element is 4.

Example 2:
a = [1,1]

"""

a = [1,1]
a2 = list(set(a))
if(len(a2) != 1):
    b = [i for i in a if a.count(i) > 1]
    c = [i for i in a if i not in b]
    print(c[0])
else:
    print(a2[0])