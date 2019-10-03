original = input("Enter a word: ")

pyg = "ay"
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]

if len(original) > 0 and original.isalpha():
    print("You chose: %s to be translated." %(original))
    print("Translation: %s" %(new_word))
else:
    print("You didn't enter a word.")