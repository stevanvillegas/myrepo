num = int(input("Enter an integer: "))
num_list = [0]

for i in range(1, num +1):
    if (i % 15 ==0 ):
        num_list.append("Fizzbuzz")
    elif i % 3 == 0:
        num_list.append("Fizz")
    elif i % 5 == 0:
        num_list.append("Buzz")
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