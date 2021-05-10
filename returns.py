def add_doubles(x = 0, y = 0):
    return (2 * x) + (2 * y)

val = add_doubles(3, 7)
print(val)

def sum_until_zero(*args):
    sum = 0
    
    for num in args:
        if num == 0:
            return sum
        sum += num
    
    return sum

sum = sum_until_zero(1,2,3,4,5,6,7,8,9,1,4,6,0,3,2,1,0)
print(sum)

x = 10
def outer_function():
    x = "Hello World"
    
    def inner_function():
        nonlocal x
        x = "Inner Function"
        print(x)
    
    inner_function()
    print(x)
    

outer_function()
print(x)

# def function_factory(mul):
#     def inner(val):
#         return mul * val 
#     return inner

def function_factory(mul):
    return lambda val: mul * val 

times_three = function_factory(3)
print(type(times_three))
print(times_three(5))

times_four = function_factory(4)
print(times_four(7))