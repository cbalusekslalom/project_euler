"""
https://projecteuler.net/problem=206

This process should take a number and find the unique integer where the Z^2 is of the form 1_2_3_4_5_6_7_8_9_0
This means the iteger should be of base ten (to end in zero)
ANd additionally must be somewhere in the billions.
1x10^9 * 1x10^9 = 1x10^18 = 1 000 000 000 000 000 000 (or 19 positions)
Additionally, the transition to a number that does not start with 1 would be ~ sqrt(2)*10^9

This gives the upper and lower limit for searching as [1E9, sqrt(2)E9] in increments of 10.

Possible functions:
sqr(n)
split(num)
"""

import numpy as np

base = 1234567890

def sqr(n):
    return n*n

def split(num):
    intlist = [str(x) for x in str(num)]
    newstring = ''
    for i in range(0,len(intlist)):
        if i%2 == 0:
            newstring += intlist[i]
    return int(newstring)

def main():
    output = 0
    for i in range(int(1E9), int(np.sqrt(2)*1E9), 10):
        test_val = split(sqr(i))
        if test_val - base == 0:
            output = i
            break
    print(f"The integer is: {output}")

if __name__ == '__main__':
    main()
