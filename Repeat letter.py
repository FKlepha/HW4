s = input('Input letters\n')
a = 0
for i in s:
    count = 0
    for j in s:
        if j == i:
            count += 1
            if count > a:
                a = count
                letter = j
print('Letter', letter, 'repeat', a, 'times')