import random
import string
pwd_len = int(input("Enter the length of the password: "))
use_upper = input("Should the password contain uppercase letters? (yes/no): ")
use_lower = input("Should the password contain lowercase letters? (yes/no): ")
use_digits = input("Should the password contain digits? (yes/no): ")
use_special = input("Should the password contain special characters? (yes/no): ")
pool = ""
if use_upper == "yes":
    pool += string.ascii_uppercase
if use_lower == "yes":
    pool += string.ascii_lowercase
if use_digits == "yes":
    pool += string.digits
if use_special == "yes":
    pool += string.punctuation
if pool == "":
    print("No valid character type selected.")
else:
    pwd = "".join(random.choice(pool) for _ in range(pwd_len))
    print("Generated password:", pwd)
