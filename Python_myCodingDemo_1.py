# The assignment was to write a program to capture user input for an employee.

# Record employee's name
employee_id = 1
# Splitting the name into first and last
full_name = input("Enter employee's first and last name: ").split(" ")
# Ensuring the first letter of both first and last names are capitalized, and the rest of the letters are lowercase 
first_name = full_name[0].lower().capitalize()
last_name = full_name[1].lower().capitalize()

# recording the employee's age by parsing the age information to an int
age_input = int(input("Enter employee's age: "))

# generating the employee's email
# linking the first and last names with a "."
# adding the employee's id number to the last name as well
# the addition of @company.com to the end of the email
email = f"{first_name}.{last_name}{employee_id}@company.com"

# printing all results to the screen
print(f"""first name: {first_name}
last name: {last_name}
age: {age_input}
email: {email}""")
