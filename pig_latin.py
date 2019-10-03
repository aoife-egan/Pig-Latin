original = input("Enter a word: ")
if len(original) > 0 and original.isalpha():
    print("You chose: %s to be translated." %(original))
else:
    print("You didn't enter a word.")