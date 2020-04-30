import tkinter as tk
import random
import array


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

global COMBINED_LIST
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

global temp_pass
temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol
def _pass_():

    Len = length.get()

    if Len <= 4:
         print("You shold use more characters !!")
         # l=Label(m, text='You should use more characters')
         # l.pack()

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
    # L=Label(m, text=password)
    # L.pack()


m = tk.Tk()

length = tk.IntVar()

m.title('Password_Generator')

w = tk.Label(m, text='Length of the password?').grid(row=0)
e1 = tk.Entry(m, textvariable=length)
e1.grid(row=0, column=1)

button = tk.Button(m, text = 'Enter', width = 10,
    command = _pass_)
button.grid(row = 1, column = 1)

m.mainloop()
