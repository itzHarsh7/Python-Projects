import datetime
def ageCalculator(year, month, day):
    today = datetime.datetime.now().date()
    dob = datetime.date(year, month, day)
    age = int((today-dob).days / 365.25)
    return age

print('Please Enter your Date of Birth to Calculate your Age') 
date = int(input('Please Enter your Birth Date: '))
month = int(input('Please Enter your Birth Month (in Numbers): '))
year = int(input('Please Enter your Birth Year: '))
age =ageCalculator(year, month, date)
print('\nYour Age is : ', age)