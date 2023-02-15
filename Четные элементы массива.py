li = []
size = int(input('Введите кол-во элементов в массиве\n'))
print('Введите элементы массива')
for i in range(size):
    i = int(input())
    if i % 2 == 0:
        li.append(i)
print(li)