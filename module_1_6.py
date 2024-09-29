my_dict = {'Max': 2016, 'Lena': 1985, 'Sonya': 1993}
print(my_dict)
print(my_dict ['Max'])
print(my_dict.get('Den'))
my_dict.update({'Vika': 1998, 'Egor': 2015})
a = my_dict.pop ('Lena')
print(a)
print(my_dict)
my_set = {1, 2, 3, 4, 4, 1, 1, 3, 3, 'Soul', 'Sun', 2, 2, 'Soul'}
print(my_set)
my_set.add (3.15)
my_set.update ([(7, 8, 9)])
my_set.discard('Soul')
print(my_set)