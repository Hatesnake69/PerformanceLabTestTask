n = int(input('Введите число n: '))
m = int(input('Введите число m: '))

circ_array = [i for i in range(1, n+1)]
_path = str(circ_array[0])
loop = m
while True:
    if circ_array[(loop) % len(circ_array)-1] == int(_path[0]):
        break
    _path += str(circ_array[(loop) % len(circ_array)-1])
    loop += m-1

print(f'{_path}')
