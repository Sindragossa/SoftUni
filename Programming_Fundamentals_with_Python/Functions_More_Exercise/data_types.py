data_type = input()
value = input()


def func_data_type(type, value):
    if type == 'int':
        return int(value) * 2
    elif type == 'real':
        return f'{(float(value) * 1.5):.2f}'
    elif type == 'string':
        return f'${value}$'


print(func_data_type(data_type, value))