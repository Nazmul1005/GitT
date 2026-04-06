recipe = input()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
r = int(input())

rb = recipe.count('B')
rs = recipe.count('S')
rc = recipe.count('C')


lo, hi = 0, 10**15

while lo < hi:
    mid = (lo + hi + 1) // 2

  
    need_b = max(0, rb * mid - nb)
    need_s = max(0, rs * mid - ns)
    need_c = max(0, rc * mid - nc)

    cost = need_b * pb + need_s * ps + need_c * pc

    if cost <= r:
        lo = mid
    else:
        hi = mid - 1

print(lo)
