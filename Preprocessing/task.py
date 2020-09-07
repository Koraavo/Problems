text = input()
new_text = text.replace("!", "").replace(".", "").replace("?", "").replace(",", "")
print(new_text.lower())
