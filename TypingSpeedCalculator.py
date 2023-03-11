from time import *
import random as r

def mistake(paragraph, userinput):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != userinput[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speedtime(timestart, timeend,userinput):
    time_delay= timeend - timestart
    time_R = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)


test =["This will get you the bleeding-edge syntax highlighting for C++. Which means your theme will be able to color your code better. This used to be a fix, but then VS Code starting using it as the official source for C and C++ highlighting.", "Run code snippet or code file for multiple languages: C, C++, Java, JavaScript, PHP, Python, Perl, Perl 6, Ruby, Go, Lua, Groovy, PowerShell, C# Script, C#, VBScript, TypeScript, CoffeeScript, Scala, Swift, Julia, Crystal, OCaml Script, R, AppleScript, Elixir, Visual Basic .NET, Clojure, Haxe, Objective-C, Rust, Racket, Scheme, AutoHotkey, AutoIt, Kotlin, Dart, Free Pascal, Haskell, Nim, D, Lisp, Kit, V, SCSS, Sass, CUDA, Less, Fortran, Ring, and custom command"]

while True:
    newTest = input("\nWanna test your Speed?? Press n for No and Y for Yes: ")
    if newTest =='y':
        test1 = r.choice(test)
        print("\n\t\t***** Typing Speed ******\n")
        print(test1)
        print("\n")

        time1= time()
        testinput= input("Enter: \n")
        time2= time()

        print("Speed : ", speedtime(time1, time2,testinput), "w/sec")
        print("Error : ", mistake(test1, testinput))
    else: 
        print("Thanks For Testing Your Speed")
        break