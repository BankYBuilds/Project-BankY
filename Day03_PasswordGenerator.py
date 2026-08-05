# PASSWORD GENERATOR
import random

charac = (
    "qwertyuiopasdfghjklzxcvbnm"
    "ASQWERTYUIOPDFGHJKLZXCVBNM"
    "0123456789"
    "!@#$%^&*()_+/"
)

password =""

for i in range(8):
    password += random.choice(charac)
print("Generated Password: ", password)