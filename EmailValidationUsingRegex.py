import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" 
    #When we need to search any character in strings using regids, we need slash 

'''

No space should be there
[a-z] will  check whether our email starts from  lower case characters or not
[\._] it will search for _ or . in our email or not
? 
[a-z 0-9] will check whether email contains alphabets or numbers between these or not
[@] this checks @ is in our email or not
[.]\w{2,3} will check position of our . in pur email 
{2,3} is no. of characters 
position of . is prior to those no. of caracters

'''
user_email = input("Enter Your Email: ")
if re.search(email_condition, user_email):    #re.search() function will compare our (condition1 with , input)
    print("Correct Email")
else:
    print("Wrong Email")