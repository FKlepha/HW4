li = []
size = int(input('Введите кол-во элементов в массиве\n'))
print('Введите элементы массива')
for i in range(size):
    a = int(input())
    li.append(a)
li.insert(0, li.pop())
print(li)