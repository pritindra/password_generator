import random
import array

# Maximum Length = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol

print("A strong password must be more than 4 characters!!")
Len = input("How long should your password be? ")

if Len <= 4:
     print("You shold use more characters !!")

elif Len > 12:
     print('The password is too lengthy !!')

else:
     for x in range(Len):
         temp_pass = temp_pass + random.choice(COMBINED_LIST)

         temp_pass_list = temp_pass.split(',')
         random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
        password = password + x

print(password)
