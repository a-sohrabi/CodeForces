n=int(input())

x=0
for i in range(n):
    c=input()
    if '+' in c:
        x+=1
    elif '-' in c:
        x-=1

print(x)