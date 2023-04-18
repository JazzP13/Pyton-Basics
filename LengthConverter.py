print('SIMPLE LENGTH CONVERTER')
print()

lUnitFrom = ['a. cm','b. m','c. inch','d. ft']
for units in lUnitFrom:
     print(units)
print()


#for chossing base unit
baseUnit = input('select base unit: ')
unitToConvert = input('select unit: ')


#operation for baseUnit a:
while baseUnit == 'a':
     num_a = int(input('Enter base number: '))
     if unitToConvert == 'b':
          result = num_a*0.01
          print("The ",num_a,"centimeter is",result,"meters.")
          break 
     elif unitToConvert == 'c':
          result = num_a*0.393701
          print("The ",num_a,"inches is ",result,"meters.")
          break
     elif unitToConvert == 'd':
          result = num_a*0.0328
          print("The ",num_a,"feet is ",result,"meters.")
          break


#operation for baseUnit b:
while baseUnit == 'b':
     num_b = int(input("Enter base number: "))
     if unitToConvert == 'a':
          result = num_b*100
          print('The ',num_b,'meters is',result,'meters')
          break
     if unitToConvert == 'c':
          result = num_b*39.3700787402
          print('The ',num_b,'meters is ',result,'inches')
          break
     if unitToConvert == 'd':
          result = num_b*3.28
          print('the ',num_b,'meters is ',result,'feet')
          break
     break


#operation for baseUnit c:
while baseUnit == 'c':
     num_c = int(input('Enter base number: '))
     if unitToConvert == 'a':
          result = num_c* 2.54 
          print('The ',num_c,'inches is',result,'centimeters.')
          break
     if unitToConvert == 'b':
          result = num_c*0.0254
          print('The ',num_c,'inches is ',result,'meters.')
          break
     if unitToConvert == 'd':
          result = num_c*0.083
          print('the ',num_c,'inches is ',result,'feet.')
          break
     break


#operation for baseUnit d:
while baseUnit == 'd':
     num_d = int(input('Enter base number: '))
     if unitToConvert == 'a':
          result = num_d*30.48 
          print('The ',num_d,'feet is ',result,'centimeters.')
          break
     if unitToConvert == 'b':
          result = num_d*0.304
          print('The ',num_d,'feet is ',result,'meters.')
          break
     if unitToConvert == 'c':
          result = num_d*12
          print('the ',num_d,'feet is ',result,'inches.')
          break
     break
