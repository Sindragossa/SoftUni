def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


person = {
    'name': 'George',
    'town': 'Sofia',
    'age': 20
}

print(get_info(**person))
print(get_info(age=17, name='Gosho', town='Plovdiv'))