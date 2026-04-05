
import sys
input = sys.stdin.readline

n = int(input())
db = {}
results = []

for _ in range(n):
    name = input().strip()
    if name not in db:
        db[name] = 0
        results.append("OK")
    else:
        db[name] += 1
        new_name = name + str(db[name])
        db[new_name] = 0
        results.append(new_name)

print('\n'.join(results))
