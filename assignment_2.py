employee_id = 1
full_name = input("Enter employee's first and last name: ").split(" ")
first_name = full_name[0].lower().capitalize()
last_name = full_name[1].lower().capitalize()

age_input = int(input("Enter employee's age: "))

email = f"{first_name}.{last_name}{employee_id}@company.com"

print(f"""first name: {first_name}
last name: {last_name}
age: {age_input}
email: {email}""")