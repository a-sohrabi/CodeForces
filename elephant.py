x=int(input())

if x<=5:
    print("1")
elif x>5 and x%5==0:
    print(int(x/5))
else:
    print(int(x/5)+1)