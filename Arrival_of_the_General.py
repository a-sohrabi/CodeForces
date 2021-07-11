n = int(input())
a = list(map(int, input().split()))
max_h = 0
min_h = a[0]
index_min = 0
index_max = 0


for i in range(n):
    if a[i] > max_h:
        max_h = a[i]
        index_max = i
    elif a[i] <= min_h:
        min_h = a[i]
        index_min = i
ans = index_max + (n-1-index_min)
if index_max > index_min:
    print(ans-1)
else:
    print(ans)
