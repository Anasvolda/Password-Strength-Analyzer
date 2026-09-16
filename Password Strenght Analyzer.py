Password = input("Enter your password: ")

## Checking for uppercase
has_uppercase = False
for character in Password: ## LOOP - goes through each character
    if character.isupper(): ## Conditional - checks each condition
        has_uppercase = True # Do this if true
        break

## Checking for Number
has_numbers = False
for character in Password:
   if character.isdigit():
    has_numbers = True
    break

## Verifying System
if len(Password) >= 8 and has_uppercase and has_numbers:
 print("Password is Strong")
else:
 print("Password is not strong enough please enter atleast 1 captial letter and 1 numerical character and must be atleast 9 characters long")