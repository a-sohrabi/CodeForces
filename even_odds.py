n, k = map(int, input().split())
odds = []
evens = []
ceil_ = 0


def myceil(n):
    if n / 1 == n // 1:
        return n
    else:
        return n // 1 + 1



if k <= myceil(n/2):
    print(2*k-1)
else:
    print(int((k-myceil(n/2))*2))








