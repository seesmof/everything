"""
Find such x, so that x^2+sqrt(x)=C with an accuracy of at least 6 decimal points.

Input: One real number C

Output: Print the desired root x with at least 6 digits after the decimal point.

solve in python in as little code as possible
"""

from math import sqrt


c = float(input())
for x in range(int(c)):
    if x**2 + sqrt(x) == c:
        print(float(x))
