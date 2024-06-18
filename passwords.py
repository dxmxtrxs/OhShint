import random
import string
import os

def generate_passwords(first_name: str = "", last_name: str = "", bday: str = "",file_name: str = "", prnt = bool, save = bool) -> list:
    # Convert all inputs to lowercase for consistency
    first_name = first_name.lower()
    last_name = last_name.lower()
    # Extract birthday components
    day = bday[:2]
    month = bday[2:4]
    b_year = bday[4:]
    short_year = b_year[-2:]

    # Create a list to store the potential passwords
    passwords = []

    # Existing combinations with full year
    base_passwords = [
        first_name + last_name + b_year,
        last_name + first_name + b_year,
        first_name + "." + last_name + b_year,
        last_name + "." + first_name + b_year,
        first_name + "_" + last_name + b_year,
        last_name + "_" + first_name + b_year,
        first_name[0] + last_name + b_year,
        first_name + last_name[0] + b_year,
        first_name[0] + "." + last_name + b_year,
        first_name + "." + last_name[0] + b_year,
        first_name[0] + "_" + last_name + b_year,
        first_name + "_" + last_name[0] + b_year,
        first_name[:2] + last_name + b_year,
        first_name + last_name[:2] + b_year
    ]
    
    # Existing combinations with short year
    base_passwords += [
        first_name + last_name + short_year,
        last_name + first_name + short_year,
        first_name + "." + last_name + short_year,
        last_name + "." + first_name + short_year,
        first_name + "_" + last_name + short_year,
        last_name + "_" + first_name + short_year,
        first_name[0] + last_name + short_year,
        first_name + last_name[0] + short_year,
        first_name[0] + "." + last_name + short_year,
        first_name + "." + last_name[0] + short_year,
        first_name[0] + "_" + last_name + short_year,
        first_name + "_" + last_name[0] + short_year,
        first_name[:2] + last_name + short_year,
        first_name + last_name[:2] + short_year
    ]
    
    passwords.extend(base_passwords)

    # Adding special characters and more complexity
    special_chars = "!@#$%^&*"
    for char in special_chars:
        for base in base_passwords:
            passwords.append(base + char)
            passwords.append(char + base)
            passwords.append(base[:len(base)//2] + char + base[len(base)//2:])
    
    # Adding numeric and mixed case variations
    for num in range(10):
        for base in base_passwords:
            passwords.append(base + str(num))
            passwords.append(str(num) + base)
            passwords.append(base[:len(base)//2] + str(num) + base[len(base)//2:])
            passwords.append(base.capitalize() + str(num))
            passwords.append(str(num) + base.capitalize())
            passwords.append(base.capitalize())

    # Adding randomized characters
    for _ in range(10):
        random_char = random.choice(string.ascii_letters + string.digits + special_chars)
        for base in base_passwords:
            passwords.append(base + random_char)
            passwords.append(random_char + base)
            passwords.append(base[:len(base)//2] + random_char + base[len(base)//2:])

    if file_name == "":
        file_name = str(first_name + last_name + "Passwords.txt")
    else:
        file_name = file_name+".txt"
    if save:
        f = open(file_name, "w")

    for i in range(len(passwords)):
        if prnt:
            print(str(i)+". "+ passwords[i])
        if save:
            f.write(str(i)+". "+ passwords[i] + "\n")
    if save:
        file_path = os.path.abspath(file_name)
        print("File was saved to: " + file_path)
        f.close()


    return passwords
