# todo Здесь нужно написать код
table = str.maketrans('','','1234567890')
with open(r'test_file\task1_data.txt', 'r', encoding='utf-8') as file:
    file = file.read()
res = file.translate(table)
with open(r'test_file\task1_answer.txt', 'w', encoding='utf-8') as file:
    file.write(res)

