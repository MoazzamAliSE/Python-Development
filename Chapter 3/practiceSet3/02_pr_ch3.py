letter = '''Dear <|NAME|>
\tYou are selected.Congrats!
\t\t\t<|DATE|>'''
letter = letter.replace("<|NAME|>", input("Enter your name\n"))
letter = letter.replace("<|DATE|>", input("Enter DATE\n"))
print(letter)
