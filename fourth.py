n, m, a, b = map(int, input().split())

min_cost = float('inf')


for i in range(n // m + 2):
    rides_covered = i * m
    if rides_covered >= n:
        
        cost = i * b
    else:
        
        remaining = n - rides_covered
        cost = i * b + remaining * a
    min_cost = min(min_cost, cost)

print(min_cost)
