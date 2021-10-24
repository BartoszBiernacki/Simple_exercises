
names = ["Karol", "Dawid", "Bartek", "Tom", "Zbigniew", "Zbyszek", "Denis"]
dictionary = {}

first_letters = []
for name in names:
    first_letter = name[0]
    if first_letter not in first_letters:
        first_letters.append(first_letter)
        dictionary[first_letter] = [name]
    else:
        dictionary[first_letter].append(name)

for key in dictionary.keys():
    print(dictionary[key])

print(dictionary)
