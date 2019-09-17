print('Welcome to the special recruitment program, please answer the following questions:')
name = input("What's your name? ")
age = int(input('How old are you? '))
exp = int(input("How many years of experience do you have? "))
print()
skills = [ 'Running', 'Dancing', 'Coding', 'Sking', 'Cycling', 'Swimming' ]
cv = {'name':name , 'age':age , 'experience':exp , 'skills':[]}

print('Skills:')
num = 1
for skill in skills:
  print('{}- {}'.format(num,skill))
  num += 1 
print()

sk1 = int(input('Choose a skill from above by entering its number: '))

sk2 = int(input('Choose another skill from above by entering its number: '))

cv['skills'] = [skills[sk1-1], skills[sk2-1] ]


if cv['age'] >= 21 and cv['experience'] >= 1 and (sk1-1 or sk2-1) == 2: 
  print('You have been accepted, {}.'.format(name))
else:
  print('Sorry! {} you have not been accepted.'.format(name))





