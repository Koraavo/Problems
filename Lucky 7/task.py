number = int(input())
list1 = []
for _i in range(number):
    to_check = int(input())
    list1.append(to_check)
for _k, j in enumerate(list1):
    if j % 7 == 0:
        squares = j ** 2
        print(squares)
