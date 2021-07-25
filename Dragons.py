s, n = map(int, input().split())
dragons_strength = []
bonus = []

# for i in range(n):
#     a = map(int, input().split())
#     dragons_strength.append(a)
#     bonus.append(b)

#
# for i in range(n):
#     if s > dragons_strength[i]:
#         s += bonus[i]
#         dragons_strength[i] = 0
#
# if sum(dragons_strength) == 0:
#     print('YES')
# else:
#     print('NO')

for i in range(n):
    a = list(map(int, input().split()))
    dragons_strength.append(a)
    # bonus.append(b)

dragons_strength = sorted(dragons_strength)

for i in range(n):
    if s > dragons_strength[i][0]:
        s += dragons_strength[i][1]
        dragons_strength[i][0] = 0

sum_ = 0
for i in range(n):
    sum_ += dragons_strength[i][0]

if sum_ == 0:
    print('YES')
else:
    print('NO')



