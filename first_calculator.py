x = float(input('enter first number '))
if x==int or float:
 print(':)')
else:
 print('dude its a calculator why are u writing letters ')
y = float(input('enter second number '))
if y==int or float:
 print(':)')
else:
 print('dude its a calculator why are u writing letters')
operation =str(input('''               enter (+) for addition 
               enter (-) for subtraction
               enter (/) for division 
               enter (*) for multiplication'''))
if operation == '+':
    result = x + y
elif operation == '-':
     result = x - y
elif operation == '*':
     result = x * y
elif operation == '/':
     result = x/y
else :
    print('u might have brain damage')
print(result)