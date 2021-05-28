# The assignment was to create a dictionary with "name", "age", and "years" keys
programmer = {
    "name": "Jon Smith",
    "age": 42,
    "years": 25
}

# Prompt the user to enter their first three programming languages
print("Enter the frist three programming languages you learned")
lang1 = input("first: ")
lang2 = input("second: ")
lang3 = input("third: ")

# storing as a tuple
first_langs = (lang1, lang2, lang3)

# prompt the user to enter their three favorite programming languages
print("What are your three favorite programming languages?")
lang1 = input("first: ")
lang2 = input("second: ")
lang3 = input("third: ")

# storing as a list
fav_langs = [lang1, lang2, lang3]

# created a set that is a intersection of their first programming languages and their favorite programming languages
still_fav_langs = set(fav_langs).intersection(first_langs)

programmer.update({
    "first_languages": first_langs,
    "favorite_languages": fav_langs,
    "still_favorite": still_fav_langs
})

        # print(programmer)
    
        # adding all of these collections as keys to the dictionary 
        # output = f"Name: {programmer['name']}, Years Coding: {programmer['years']}, Still Favorite Languages: {programmer['still_favorite']}"
        # print(output)
        
# adding all of these collections as keys to the dictionary     
template_string = "Name: {}, Years Coding: {} Still Favorite Languages: {}"
print(template_string.format(programmer['name'], programmer['years'], programmer['still_favorite']))
