import datetime
x=datetime.datetime.now()

empl = []
mang = []

class Employee:
  def __init__(self, name, age, salary, employment_date):
    self.name=name
    self.age=age
    self.salary=salary 
    self.employment_date=employment_date
      
  def get_working_years(self):
    return x.year - self.employment_date
    
  def __str__(self):
    return 'Name: %s, Age: %d, Salary: %d, Working Years: %d' % (self.name,self.age,self.salary,self.get_working_years())
       
  
  
class Manager:
  def __init__(self, name, age, salary, employment_date,bonus_percentage):
    self.name=name
    self.age=age
    self.salary=salary 
    self.employment_date=employment_date
    self.bonus_percentage=bonus_percentage
      
  def get_working_years(self):
    return x.year - self.employment_date
    
  def get_bonus(self):
    return self.bonus_percentage * self.salary
    
  def __str__(self):
    return 'Name: %s, Age: %d, Salary: %d, Working Years: %d, Bonus: %f  ' % (self.name,self.age,self.salary,self.get_working_years(), self.get_bonus())


def main():
  print("Options:")

  ops = ['Show Employees', 'Show Managers', 'Add An Employee', 'Add A Manager','Exit']

  num = 1
  for op in ops:
    print('{}. {}'.format(num,op))
    num += 1 
  print()

  i = int(input('What would you like to do? '))

  print('-----------------')



  if i == 1 :
    print('Employees')
    print()
    for n in empl :
      print(n)
    print('-----------------')
    main()
    
  elif i == 2 :
    print('Managers')
    print()
    for n in mang :
      print(n)
    print('-----------------')
    main()
    
  elif i == 3 :
    name = input('Name: ')
    age = int(input('Age: '))
    salary = int(input('Salary: '))
    employment_date = int(input('Employement Year: '))
    E=Employee(name, age, salary, employment_date)
    empl.append(E)
    print()
    print('Employee added succesfully')
    print()
    main()
  
  elif i == 4 :
    name = input('Name: ')
    age = int(input('Age: '))
    salary = int(input('Salary: '))
    employment_date = int(input('Employement Year: '))
    bonus_percentage = float(input('Bonus Percentage:' ))
    M=Manager(name, age, salary, employment_date, bonus_percentage)
    mang.append(M)
    print()
    print('Manager added succesfully')
    print()
    main()
  
  elif i == 5 :
    exit()
    

print('Welcome to HR Pro 2019')
main()    