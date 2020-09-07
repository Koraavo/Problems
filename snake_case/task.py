word = input()
snake_case = ""
for x in word:
    if x.isupper():
        snake_case += ('_' + x.lower())
    else:
        snake_case += x
print(snake_case)
