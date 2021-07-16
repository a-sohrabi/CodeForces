a = input()
letters=[]
c=0

for char in a:
    if char not in letters:
        c+=1
        letters.append(char)

if c%2!= 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")