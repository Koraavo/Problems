word = input()
while word:
    for letters in word:
        if letters.isalpha():
            if letters in 'aeiou':
                print("vowel")
            else:
                print("consonant")
        else:
            break
    break
