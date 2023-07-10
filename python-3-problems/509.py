"""
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
0 <= n <= 30
"""
def fib(n):
    fiblist = [0,1]
    for index in range(2, n+1):
        try: 
            fiblist.append(fiblist[index-1]+ fiblist[index-2])
        except:
            pass
    print(fiblist)
    return fiblist[n]

n = 2
output = 1
#print(fib(n)==output)
n = 3
output = 2
print(fib(n)==output)
n = 4
output = 3
print(fib(n)==output)

