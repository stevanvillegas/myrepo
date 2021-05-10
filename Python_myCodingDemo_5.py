# the assignment was to expand on the 'Python_myCodingDemo_2' program; error handling

employee_id = 1
employees = []

# prompt the user to say how many employees they will add
# using error handling (try/except, else) to repeat the prompt until an integer is entered (while loop)
while True:
    try: 
        num = int(input("Enter the number of employees: "))
    except:
        print("Please enter number of employees")
    else:
        break

# loop (while) for each employee and record their information
while employee_id <= num:
    full_name = input("Enter employee's first and last name: ").split(" ")
 
    first_name = full_name[0].lower().capitalize()
    last_name = full_name[1].lower().capitalize()

# use error handling (try/except(multi-except), else) to repeat the prompt until an integer is entered for age
    while True:
        try:
            age_input = int(input("Enter employee's age: "))
 # raise an error if the employee is under 18
            if age_input < 18:
                raise Exception
        except ValueError:
            print("please enter a number for age")
        except Exception:
            print("Age too low")
        else:
            break
    
    email = f"{first_name.lower()}.{last_name.lower()}{employee_id}@company.com"

    employee = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age_input,
        "email": email
    }
    employees.append(employee)
    employee_id += 1

# print each employee's information in a formatted string
for employee in employees:
    print(f""first name: {employee["first_name"]}
             last name: {employee["last_name"]}
             age: {employee["age"]}
             email: {employee["email"]}"")
                # if buffer.isdigit():
                    # if int(buffer) >= 18:
                        # employee["age"] = int(buffer)
                        # done = True

    finally:
        employee.append(employee)
        print (employeelist)
