try:
    entry = input("Enter a Non-Zero Integer: ")
    num = int(entry)
    message = "Your number is Even" if num % 2 == 0 else "Your Number is odd"
    print(f'{message}')
    if num == 3: del num
    print(f"10 divided by your number is {10 / num}")
except ValueError:
    print("You did not enter an Integer")
except ZeroDivisionError:
    print("You entered a Zero")
except:
    print("Something went wrong")
else:
    print(f"{num} has been calcualted with out error!")
finally:
    del entry
    print("Entry has been deleted")


print("Code after Try")

class TooYoungException (Exception):
    pass

class TooOldException (Exception):
    pass

try:
    entry = input("Enter your age: ")
    age = int(entry)
    if age < 18:
        raise TooYoungException
    
    if age > 100:
        raise TooOldException  
except ValueError:
    print("You did not enter an age")
except TooYoungException:
    print("You are too young for this")
except TooOldException:
    print("You are too old for this")
else: 
    print("Welcome!")
