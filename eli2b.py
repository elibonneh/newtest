import array as arr

a = arr.array("i", [3, 6, 9])
print(a)
a[0] = 5
print(a)
a.append(111)
print(a)
print(a[0])
a.pop(0)
print(a)
a.insert(1, 7)
print(a)
print(len(a))
for temp_num in a:
    print(temp_num)
for i in range(len(a)):
    print(a[i])

my_list = [a.insert(1, 7), a.append(222)]
print(a)
seasons = ('f', 'w', 's', 's')
print(seasons)
x = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
print(x)

my_dictionary = {'A': 1, 'B': 2}
print(my_dictionary.keys())
print(my_dictionary.values())
my_dictionary['A'] = 5
print(my_dictionary.values())

