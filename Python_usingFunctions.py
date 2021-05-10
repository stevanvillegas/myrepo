x = 10
t = "10:00"
def say_hello():
    global t
    t = "12:30"
    x = "Hello World"
    y = 20
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"t = {t}")

# while x < 11:
#     z = x * 2
#     x += 1

# say_hello()
# print(f"x = {x}")
# # print(f"y = {y}")
# print(f"z = {z}")
# print(f"t = {t}")

def say_greeting(name, greeting="Hello"):
    print(f"{greeting} {name}")

# say_greeting()
say_greeting("World")
say_greeting("Planet", "Greetings")
say_greeting(greeting="Good Morning", name="Earth")

def print_csv(*args, seperator=","):
    output = ""
    for arg in args:
        output += f"{arg}{seperator}"
    print(output[0:-1])
print_csv(1,2,3,4,5,6,7,8,9,0)
print_csv(1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,seperator="-")

def print_keys(cb=print, **kwargs):
    for key in kwargs:
        cb(f"{key}, {kwargs[key]}")

def formatted_print(arg):
    print(f"The string recieved is: {arg}")

print_keys(a = "10", b = 20, c = "Hello")
print_keys(a = "10", b = 20, cb=formatted_print)

print("Hello ", 42, [" World"], sep=" - ", end="\n\n")
