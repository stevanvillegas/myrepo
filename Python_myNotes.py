# This is documentation of my Cognixia Python learning experience:

# This is a list:
    fruits = ["apple", "mango", "banana", "kiwi", "peach"]
    print(fruits)

    mixed_list = ["Hello", 30, [1,2,3], None]
    print(mixed_list)

    print(fruits[0])
    print(fruits[-2])
    print(fruits[0:3])
    print(fruits[1:-1])

    fruits_copy = fruits.copy()
    print(fruits_copy)
    fruits.append("orange")
    fruits.append("mango")
    fruits[2] = "bananas"
    print(fruits)
    print(fruits_copy)

    mixed_list.clear()
    print(bool(mixed_list))
    print(fruits.count("mango"))

    nums_1 = [1,2,3,4]
    nums_2 = [10,11,12]
    nums_1.extend("Hello")
    print(nums_1)
    nums_1.insert(3,"Hello")
    print(nums_1)



#This is a set:
    fruit_set = {"apple", "mango", "kiwi", "banana", "mango"}
    print(fruit_set)

    fruit_set.add("avocado")
    print(fruit_set)

    fruit_set.discard("apple")
    print(fruit_set)

    fruit_set.update(("apple", "banana", "kiwi"))
    print(fruit_set)

    random_fruit = fruit_set.pop()
    print(random_fruit)

    season_fruits = {"avacado","cherry", "peach", "grapefruit", "kiwi", "lemon"}
    fav_fruits = {"strawberry", "pear", "avacado", "lemon"}

    print(season_fruits.intersection(fav_fruits))
    print(season_fruits.difference(fav_fruits))



#This is a tuple:
    fruits = ("apple","mango","banana","kiwi","mango")
    print(fruits)
    print(fruits[0])
    print(fruits[1:-2])

        # fruits[3] = "duiran"

    more_fruits = fruits + ("durian",)
    print(more_fruits)
    print(fruits)

    print(fruits.count("mango"))
    print(fruits.index("mango"))

    empty_tuple = ()
    print(empty_tuple)
    print(type(empty_tuple))



#This is a dictionary:
    user = {
        "username": "Hello World",
        "password": "helloWorld1",
        "id": 567,
        1: 100,
        "friend_ids": [123,456],
        "status": {
            "banned": False,
            "active": True
        }
    }

    print(f"The username is {user['username']}")
    print(f"Is the user active? {user['status']['active']}")

    user['status']['active'] = False
    user['friend_ids'].append(789)

        # user['premium_account'] = False
    user.update({"premium_account": False})

    print(user)

    user_id = user.get('id')
    print(user_id)

    user_keys = user.keys()
    user_values = user.values()
    user_items = user.items()
    print(user_keys)
    print(user_values)
    print(user_items)

    val = user.pop("premium_account")
    print(val)
    print(user)

    new_dictionary = dict.fromkeys(["Hello", "World"],0)
    print(new_dictionary)
      
      
      
#Working with Variables:
    x = "Hello World"
    print(x)
    x = 42
    print(x)

    x, y, z = "Car", "Bicycle", "Unicycle"
    print(x + y + z)

    my_programming_language = "Python"

    my_boolean = True
    other_boolean = False

    print(bool(None))

    my_int = 10

    my_float = 20.7

    my_complex = 3j

    print(my_complex * my_complex)
    print(my_int + my_float)
    print(my_int + my_complex)

    print(int(my_float))
    print(float(my_int))
    print(int(float("42.3")))
    print(float("50"))

    print("The number is " + str(42))

    print(len("Hello World"))

    message = "Hello {}, you are {} years old"
    new_string = message.format("Python", 31)
    print(new_string)

    new_string = message.format("Java", 29)
    print(new_string)

    print(message)
    num = 12
    print(f"The number is {num}, double the number is {num * 2}")

    print(None)
    var = "Hello"
    print(type(var))

    print(isinstance(var, str))

    y = 12
    print(y)
    del y
    print(y)



#Working with Conditionals:
    num = int(input("Enter a Number: "))

    if num > 10:
        print("Your number is greater than 10")
        if num % 2 == 0: print("Your number is also even")
        else: print("Your number is also odd")
    elif num > 5: print("Your number is between 5 and 10")
    else: print("Your number is less than 5")

    message = "Your number is 42" if num == 42 else "Your number is not 42"
    print(message)

      
      
#This is a for loop:
    fruits = ["apple", "kiwi", "mango", "banana", "avocado"]
    drinks = ["coffee", "tea","milkshake","Capri Sun","smoothie"]

    for fruit in fruits:
        print(fruit)
    else:
        print("loop finished")
    print(f"last fruit: {fruit}")


    for i in range(5):
        print(f"{i}: {fruits[i]}, {drinks[i]}")

    my_range = range(10)
    short_range = range(3,10)
    fast_range = range(1,10,2)

    for i in fast_range:
        pass
    print("empty loop")
      

      
#This is a while loop:
    i = 1
    while i < 10:
        j = i * 2
        if i % 4 == 0: break
        print(f"i = {i}")
        i += 1 
    else:
        print(f"{i} is greater than 10, loop exiting.")

    print(f"End of loop. i = {i}, j = {j}")

    fruits = {"apple","kiwi","mango","banana"}

    while fruits:
        fruit = fruits.pop()
        if fruit == "apple": continue
        print(fruit)
    else: 
        print("Fruit Loop finished")

    nums = [1,2,3,4,5]
    search = 7
    i = 0
    while i < len(nums):
        if nums[i] == search:
            print(f"Value found at index {i}")
            break
        i += 1 
    else :
        print("Value not found")
      
      
      
#using built in modules
    import sys
    import math
    import random
    import time
    import datetime
    import timeit

    print(sys.argv)

    print(math.sqrt(25))

    print(random.randint(10,20))
    print(random.sample(k=3,population=[1,1,2,3,45,"Hello"]))

    # print(time.sleep(2))
    print(time.time())

    print(datetime.datetime.now().minute)
    print(datetime.datetime(2019,2,21,12,30))

    func = "print('Hello World')"
    print(timeit.timeit(stmt=func,number=3))
      
      
      
#using filter and map
    letters = ['a','b','c','d','e','f','g','h','i','j','k']

    def vowel_filter(letter):
        if letter in ['a','e','i','o','u']:
            return False
        return True

    consonants = filter(vowel_filter, letters)
    print(list(consonants))

    vowels = filter(lambda letter: True if letter in ['a','e','i','o','u'] else False, letters)
    print(list(vowels))

    upper_letters = map(lambda letter: letter.upper(), letters)
    print(list(upper_letters))

    list_comp = [letter.upper() for letter in letters if letter not in ['a','e','i','o','u']]
    print(list_comp)

    gen_ex = (letter.upper() for letter in letters if letter not in ['a','e','i','o','u'])
    print(gen_ex)

      
      
#using generators
    def my_gen():
        yield "Hello"
        yield "World"
        yield 42

    for val in my_gen():
        print(val)

    print(val)

    gen1 = my_gen()
    print(next(gen1))
    print(next(gen1))
    print(next(gen1))

      
      
#import module example
    import my_module 
    from my_module import say_hello as hello
    from my_module import *

    my_module.say_hello()
    greeting = my_module.custom_greeting("Good Morning", "Module")
    print(greeting)

    print(my_module.x)

    hello()
    print(get_x())

    print(f"You are running {__name__}")


      
#module example continued
    def say_hello():
        print("Hello World")

    def custom_greeting(greeting = "Hello", name = "World"):
        return f"{greeting}, {name}!"

    x = 42

    def get_x():
        return x

    if __name__ == "__main__":
        print(f"You are running {__name__}")
    else: 
        print(f"You have imported {__name__}")
