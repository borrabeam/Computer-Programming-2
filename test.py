list1 = []
result = 4 ** 2
list1.append(result)
ans = list(str(result))
for i in range(ans):
    i += 1
    if i[0] > i[1]:
        i[0] = i[1]

# ans = map(int,str(result))
# for i in list1.split():
#     print(list1)
# print(ans)
print(ans)
print(list1)