def check_birthdate(year,month,day):
  if year >= 2020:
    return False
  elif year <= 2019:
    return True
  
def calculate_age(year,month,day):
  if month < 9 :
    age_year=2019-year
  elif month == 9 and day <= 4:
    age_year=2019-year 
  elif month == 9 and day > 4:
    age_year=2019-year-1  
  elif month > 9:
    age_year=2019-year-1 
  print("You are {} years old.".format(age_year)) 
  
  
year=int(input('Enter year of birth: '))
month=int(input('Enter month of birth: '))
day=int(input('Enter day of birth: '))


if check_birthdate(year,month,day) is True:
  calculate_age(year,month,day) 
else:
  print('birthdate is invalid.')



