import smtplib as s
ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()  #to get server of smtp
ob.starttls()   #To start Server
ob.ehlo()  #to get server of smtp
ob.login('###### Your Mail ########', '#### Password ####')
subject = "Testing Mail report"
body = "Trying to Send mail using Python"
message = "subject:{}\n\n{}". format(subject, body)
listadd = '###### Reciever Mail ########'
ob.sendmail('###### Your Mail ########', listadd, message)
print("Done")
ob.close()   # to end server