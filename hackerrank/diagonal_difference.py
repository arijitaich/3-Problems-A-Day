"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is 15-17 = 2.

"""

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
dg1 = []
dg2 = []
index = 0
for v in arr:
    dg1.append(v[index])
    index = index + 1
    dg2.append(v[len(v) - index])
total = abs(sum(dg1) - sum(dg2))
print(total)