a = int(input())
b = int(input())
c = int(input())

ans = 0
if a == 1:
    ans = a + b
    if c == 1:
        ans += c
    else:
        ans *= c
    print(ans)
    quit()
elif c == 1:
    ans = c + b
    if a == 1:
        ans += a
    else:
        ans *= a
    print(ans)
    quit()
else:
    if b != 1:
        ans = a*b*c
        print(ans)
    else:
        if a >= c:
            ans = (b+c)*a
        else:
            ans = (a+b)*c
        print(ans)

