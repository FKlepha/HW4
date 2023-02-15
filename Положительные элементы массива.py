li = []
size = int(input('Введите кол-во элементов в массиве\n'))
print('Введите элементы массива')
count = 0
for i in range(size):
    i = int(input())
    if i > 0:
        count += 1
print(count)