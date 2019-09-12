first_num=float(input("Enter the first number: "))
second_num=float(input("Enter the second number: "))
op=input("Choose the operation (+, -, /, *): ")

if op == '+' :
  ans=first_num+second_num
elif op == '-' :
  ans=first_num-second_num
elif op == '/' :
  ans=first_num/second_num
elif op == '*' :
  ans=first_num*second_num


print("The answer is {}".format(ans))
