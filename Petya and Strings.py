import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

a = s1.lower()
b = s2.lower()

if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)
