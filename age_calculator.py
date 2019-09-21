import datetime
x=datetime.datetime.now()

def check_birthdate(year,month,day):
  if year > x.year :
    return False
  elif year <= x.year :
    return True
  
def calculate_age(year,month,day):
  if month < x.month :
    age_year=x.year-year
  elif month == x.month and day <= x.day :
    age_year=x.year-year 
  elif month == x.month and day > x.day :
    age_year=x.year-year-1  
  elif month > x.month:
    age_year=x.year-year-1 

  print("You are {} years old.".format(age_year)) 
  
  
year=int(input('Enter year of birth: '))
month=int(input('Enter month of birth: '))
day=int(input('Enter day of birth: '))


if check_birthdate(year,month,day) is True:
  calculate_age(year,month,day) 
else:
  print('birthdate is invalid.')

