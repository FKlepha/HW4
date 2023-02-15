li = []
li2 = []
size = int(input('Введите кол-во элементов в массиве\n'))
print('Введите элементы массива')
for i in range(size):
    li.append(int(input()))
for j in range(len(li)-1):
    x = li[j]
    j += 1
    y = li[j]
    if y > x:
        x = y
        li2.append(x)
print(li2)