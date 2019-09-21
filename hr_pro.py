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
    
      #def __str__ (self, name, age, salary, employment_date):
    #  return 'Name: '+self.name+', Age: '+self.age+', Salary: '+self.salary+', Working Years: '+get_working_years()
      
  
  
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
    
    # def __str__ (self, name, age, salary, employment_date,bonus_percentage):
     # return 'Name: '+self.name+', Age: '+self.age+', Salary: '+self.salary+', Working Years: '+get_working_years()+', Bonus: '+get_bonus()


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
    E=Employee(empl[0],empl[1],empl[2],empl[3])
    employment_date=empl[3]
    Ye=E.get_working_years()
    print('Employees')
    print()
    #print(E.__str__())
    print('Name: {}, Age: {}, Salary: {}, Working Years: {}'.format(empl[0],empl[1],empl[2],Ye))
    print('-----------------')
    main()
    
  elif i == 2 :
    M=Manager(mang[0],mang[1],mang[2],mang[3],mang[4])
    employment_date=mang[3]
    bonus_percentage=mang[4]
    salary=mang[2]
    Ym=M.get_working_years()
    Bm=M.get_bonus()
    print('Managers')
    print()
    #print(M.__str__())
    print('Name: {}, Age: {}, Salary: {}, Working Years: {}'.format(mang[0],mang[1],mang[2],Ym,Bm))
    print('-----------------')
    main()
    
  elif i == 3 :
    name = input('Name: ')
    empl.append(name)
    age = int(input('Age: '))
    empl.append(age)
    salary = int(input('Salary: '))
    empl.append(salary)
    employment_date = int(input('Employement Year: '))
    empl.append(employment_date)
    print('Employee added succesfully')
    print()
    main()
  
  elif i == 4 :
    name = input('Name: ')
    mang.append(name)
    age = int(input('Age: '))
    mang.append(age)
    salary = int(input('Salary: '))
    mang.append(salary)
    employment_date = int(input('Employement Year: '))
    mang.append(employment_date)
    bonus_percentage = float(input('Bonus Percentage:' ))
    mang.append(bonus_percentage)
    print('Manager added succesfully')
    print()
    main()
  
  elif i == 5 :
    exit()
    
    


print('Welcome to HR Pro 2019')
main()    