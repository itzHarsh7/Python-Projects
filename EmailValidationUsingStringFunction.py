email = input("Enter Your Email: ")
k,j,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if email[-2:]== "in" or email[-3:] == "com":
                if (email[-3] == ".") ^ (email[-4] == "."):   # Why ^(ExOR operater)? because if any one of the condition is true then it will retrurn true
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j =1 
                        elif i.isdigit():
                            continue
                        elif i =="_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k ==1 or j ==1 or d==1:
                        print("Wrong Email. Email Must not contain any SPACE and Should Not contain any Uppercase Letter ")
                    else:
                        print("Correct Email")
                else:
                    print("Wrong Email. Email Must contain .(dot) at position 4 or 3 in reverse")
            else:
                print("Wrong Email. Email Should end with 'in' or 'com'")
        else:
            print("Wrong Email. Email Must contain atleast 1 @ symbol")
    else:
        print("Wrong Email. Your First letter shoud be Alphabet")
else:
    print("Wrong Email. Length of Email Should be greater than 6")
