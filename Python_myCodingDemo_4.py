# the assignment was to create a program that accepts a user's integer input

num = int(input("Enter an integer: "))
num_list = [0]

# range(start, stop) 
for i in range(1, num +1):
# if the number is divisible by both 3 and 5, add "Fizzbuzz"
    if (i % 15 ==0 ):
        num_list.append("Fizzbuzz")
# if the number is divisible by 3, add "Fizz"
    elif i % 3 == 0:
        num_list.append("Fizz")
# if the number is divisible by 5, add "Buzz"
    elif i % 5 == 0:
        num_list.append("Buzz")
# if the number is divisible by neither, add the number itself
    else:
        num_list.append(i)

print(num_list)
sum = 0
for i in num_list:
    if isinstance(i,int):
        sum += i

print(f"Integer Sum: {sum}")
print(f"Fizz Count: {num_list.count('Fizz')}")
print(f"Buzz Count: {num_list.count('Buzz')}")
print(f"Fizzbuzz Count: {num_list.count('Fizzbuzz')}")
