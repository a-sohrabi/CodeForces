string = set(input().strip("{}").split(', '))
# print(string)
counter = 0
for char in string:
    if char.isalpha():
        counter += 1

print(counter)

a = input()
print(len(set(a[1:-1:3])))
