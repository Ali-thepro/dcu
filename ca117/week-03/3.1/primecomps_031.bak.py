# #!/usr/bin/env python3

# import sys

# for line in sys.stdin:
#     print('Primes:', [n for n in range(2, int(line) + 1) if all(n % k != 0 for k in range(2, n))])




#!/usr/bin/env python3

import sys


def is_prime(number):
    # if number is equal to or less than 1, return False
    if number <= 1:
        return False

    for x in range(2, number):
        #  if number is divisble by x, return False
        if number % x == 0:
            return False
    return True


for line in sys.stdin:
    nums = [int(n) for n in range(2, (int(line) + 1))]
    primes = [n for n in nums if is_prime(n)]
    # primes = [n for n in range(2, (int(line) + 1)) if is_prime(n)]
    print(f"Primes: {primes}")