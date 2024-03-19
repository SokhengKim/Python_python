dict_word = {
    "A": "Apple",
    "B": "Book",
    "C": "Cook",
    "D": "Drink",
    "V": "V is me",
}

for i in range(1, 10):
    word = input(f"Input letter {i}: ")
    if word.upper() in dict_word:
        print(dict_word[word.upper()])
    else:
        print("The word not found")
