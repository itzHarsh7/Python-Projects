Height=float(input("Enter your Height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("Your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=18.5):
		print("You are underweight")
	elif(BMI>18.5 and BMI<=25):
		print("You are Healthy")
	elif(BMI>25 and BMI<=30):
		print("You are overweight")
	elif(BMI>30 and BMI<=40):
		print('You are Obese')