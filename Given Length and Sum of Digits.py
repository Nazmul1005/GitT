m, s = map(int, input().split())

if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
elif s > 9 * m:
    print("-1 -1")
else:
    
    smallest = []
    remaining = s
    for i in range(m):
        for d in range(0 if i > 0 else 1, 10):
           
            left = m - i - 1
            if remaining - d <= 9 * left:
                smallest.append(d)
                remaining -= d
                break

   
    largest = []
    remaining = s
    for i in range(m):
        d = min(9, remaining)
        largest.append(d)
        remaining -= d

    print(''.join(map(str, smallest)), ''.join(map(str, largest)))
