print('SIMPLE PYTNHON CALCULATOR')

print('+' , '-' , 'x' , '/')
userOperand = input('chosse operand: ')
fnum = int(input("Enter first number: "))
snum = int(input('Entersecond number: '))

if userOperand == '+':
     result = fnum+snum
     print(result)
elif userOperand == '-':
     result = fnum-snum
     print(result)
elif userOperand == 'x':
     result = fnum*snum
     print(result)
elif userOperand == '/':
     result = fnum/snum
     print(result)
