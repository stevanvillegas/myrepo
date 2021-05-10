# each employee is a dictionary like this : 
#       "name" : "john William"
#       "age" : 40

try:
    num = int(input("Number of employees: "))
    if num > 100:           # max number of employees is 100
        raise Exception
    except Exception:
        print("Try Again")
        done = False
        while done is False:
            buffer = input("Number of employees: ")
            if buffer.isdigit():
                num = int(buffer)
                if num <= 100:
                    done = True

employeelist = []

for i in range(num):
    try:
        print(f"Enter employee information: ")
        employee = dict.fromkeys(["name", "age"])
        employee["name"] = input("Employee name: ")
        employee["age"] = int(input("Employee age: "))
        if employee["age"] < 18:
            raise Exception
        except Exception:
            print("Try Again")
            done = False
            while done is False:
                buffer = input("Employee age: ")
                if buffer.isdigit():
                    if int(buffer) >= 18:
                        employee["age"] = int(buffer)
                        done = True

    finally:
        employee.append(employee)
        print (employeelist)