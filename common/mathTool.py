
from math import sqrt
"""
判断是否为质数
"""
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
