
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

max_val = max(a)
min_val = min(a)

max_idx = a.index(max_val)
min_idx = n - 1 - a[::-1].index(min_val)

swaps = max_idx + (n - 1 - min_idx)
if max_idx > min_idx:
    swaps -= 1

print(swaps)
