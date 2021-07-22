# a = input()
# flag = 0
# for i in range(len(a)):
#     if a[i] == 'h' and flag == 0:
#         flag += 1
#     if a[i] == 'e' and flag == 1:
#         flag += 1
#     if a[i] == 'l' and flag == 2:
#         flag += 1
#         continue
#     if a[i] == 'l' and flag == 3:
#         flag += 1
#     if a[i] == 'o' and flag == 4:
#         flag += 1
# if flag == 5:
#     print('YES')
# else:
#     print('NO')
#--------------------
s = list(input())
mean = ['h', 'e', 'l', 'l', 'o']

no = True
index = 0
for letter in s:
    if letter == mean[index]:
        index += 1
    if index == 5:
        print("YES")
        no = False
        break
if no:
    print("NO")




