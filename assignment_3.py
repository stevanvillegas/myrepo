programmer = {
    "name": "Jon Smith",
    "age": 42,
    "years": 25
}

print("Enter the frist three programming languages you learned")
lang1 = input("first: ")
lang2 = input("second: ")
lang3 = input("third: ")

first_langs = (lang1, lang2, lang3)

print("What are your three favorite programming languages?")
lang1 = input("first: ")
lang2 = input("second: ")
lang3 = input("third: ")

fav_langs = [lang1, lang2, lang3]

still_fav_langs = set(fav_langs).intersection(first_langs)

programmer.update({
    "first_languages": first_langs,
    "favorite_languages": fav_langs,
    "still_favorite": still_fav_langs
})

# print(programmer)

# output = f"Name: {programmer['name']}, Years Coding: {programmer['years']}, Still Favorite Languages: {programmer['still_favorite']}"
# print(output)

template_string = "Name: {}, Years Coding: {} Still Favorite Languages: {}"
print(template_string.format(programmer['name'], programmer['years'], programmer['still_favorite']))