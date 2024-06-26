"""
Fibonacci
=========

The Fibonacci sequence is one of the most famous formulas in
mathematics.
Each number in the sequence is the sum of the two numbers that
precede it.
For example, here is the Fibonacci sequence for 10 numbers,
starting from 0: 0,1,1,2,3,5,8,13,21,34.

Write a program to take N (variable num in code template) positive
numbers as input, and recursively calculate and output the first N
numbers of the Fibonacci sequence (starting from 0).

Sample Input
6

Sample Output
0
1
1
2
3
5

NOTE: If you are making the Fibonacci sequence for n numbers, you
should use n<=1 condition as the base case.
"""


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


n = int(input())
for i in range(n):
    print(fib(i))
