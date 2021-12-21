file_name = input('Введите название файла: ')

with open(file_name, 'r') as text_file:
    example_list = []
    for line in text_file:
        example_list.append(int(line))
    average = round(sum(example_list) / len(example_list))
    moves = 0

    for i in example_list:
        moves += abs(i - average)

    print(f'{moves}')
