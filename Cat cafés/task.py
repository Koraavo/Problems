list1 = []
cats = input()
while cats.split()[-1].upper() != 'MEOW':
    list1.append(cats)
    cats = input()

first_name = []
numbers = []
for names in list1:
    numbers.append(int(names.split()[-1]))
    first_name.append(names.split()[0])
if max(numbers):
    print(first_name[numbers.index(max(numbers))])
