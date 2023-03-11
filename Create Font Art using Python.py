# pip install pyfiglet

import pyfiglet
name = input("Enter your Name: ")
font = pyfiglet.figlet_format(name)
print(font)