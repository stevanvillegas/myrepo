# simple phone numbers program

phone = input("Enter a phone number to see if it is valid: ")
phone_digits = phone.replace("(","").replace(")","").replace("-","").replace(" ","")


if ((len(phone_digits) != 10) or ("911" in phone_digits)):
    print(f"Phone Number {phone} is invalid")
else: print(f"Phone Number {phone} is valid")
