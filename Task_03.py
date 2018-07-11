n = int(input("n="))
lst = []
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            break
    else:
        lst.append(i)
print(lst)


myString = ''.join(str(x) for x in lst)

print(myString)

m = int(input("m=\n"))

list_of_num = list(map(int, input().split()))

for i in list_of_num:
    print(myString[i - 1])
#    '\n'.join(t)
