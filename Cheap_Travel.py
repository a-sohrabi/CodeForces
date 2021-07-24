n, m, a, b = map(int, input().split())

if n % m != 0:
    if n % m * a < b:
        print((n // m) * b + (n % m) * a)
    else:
        print(n // m * b + b)
else:
    print(min(n//m * b, n*a))



#---------------------------------

if n % m * a < b:
    print(min((n // m) * b + (n % m) * a, n*a))
else:
    print(min(n // m * b + b, n*a))
#-----------------------------

print(min(n*a, -n//m*-b, n//m*b+n % m*a))

#-----------------------------------------

n,m,a,b=map(int,input().split())
print(n//m*min(b,m*a)+min((n%m)*a,b))