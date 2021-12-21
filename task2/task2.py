import math

file_name1 = input('Введите путь к 1ому файлу: ')
file_name2 = input('Введите путь к 2ому файлу: ')

with open(file_name1, 'r') as file1:
    for line in file1:
        if ' ' in line:
            x1 = float(line.split()[0])
            y1 = float(line.split()[1])
        else:
            rad = float(line)
with open(file_name2, 'r') as file2:
    for line in file2:
        i_x = float(line.split()[0])
        i_y = float(line.split()[1])
        dist = math.sqrt((x1-i_x)**2+(y1-i_y)**2)
        if round(dist, 2) == round(rad, 2):
            print(0)
        elif dist < rad:
            print(1)
        else:
            print(2)
