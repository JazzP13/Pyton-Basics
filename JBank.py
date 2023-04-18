print('=============== JBank ATM ================')
print()

balance = 50000


# this function will ask the user if the user wants to log out or not
def logoutFunction():
     ask_if_L = input('Log Out? [yes] [no] ')
     if ask_if_L == 'yes':
        print('Logged out successfuly!')





#function for transaction 1
def t_Funcion_1():
    t_Amount = int(input('Amount: '))
    if t_Amount <= balance:
        print('Transaction Succesful!')
    elif t_Amount > balance:
        print('Invalid amount')
        ask_if_continue = input('Continue? [yes] [no]: ')
        if ask_if_continue == 'yes':
            Reinput = int(input('Reinput amount: '))
            if Reinput <= balance:
                print('Transaction Successful!')
                logoutFunction()
    else:
        logoutFunction()





#function for transaction number 2
def transac_for_2():
    d_Amount = int(input('Amount: '))
    print('Successfuly added to your balabce!')
    #balance added
    New_balance = balance+d_Amount
    ask_if_check = input('Do you want to check your balance? [yes] [no];: ')
    if ask_if_check == 'yes':
        print(New_balance)
        logoutFunction()
    else:
        logoutFunction()




#function or transaction number 3
def transac_for_3():
    print(balance)
    ask = input('Do you want to withdraw? [yes] [no]: ')
    if ask == 'yes':
        t_Funcion_1()
    else:
        logoutFunction()


    


pin = input('Enter your pin: ')

if pin == '1234':
    print('Log in Successfuly')
    
    trans = ['1. Withdraw','2. Diposit','3. Check Balance','4. Logout']
    for x in trans:
        print(x)
        
    transac = int(input('Choose number of transaction: '))


    

    #transaction foe number 1
    if transac == 1:
        t_Funcion_1()





    #transacion for number 2      
    elif transac == 2:
        transac_for_2()




    #transaction for number 3  
    elif transac == 3:
       transac_for_3()





    #transaction foe number 4          
    elif transac == 4:
        print('Log out Successfuly!')



        
    else:
        print('Invalid')


        
else:
    print('Invalid pin')
