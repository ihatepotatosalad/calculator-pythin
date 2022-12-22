import os

def add(num,num2):
    return num+num2
def subtract(num,num2):
    return num-num2
def multipliy(num,num2):
    return num*num2
def divide(num,num2):
    return num/num2

operations={
    '+':add,
    '-':subtract,
    '*':multipliy,
    '/':divide
    }



def calculator():

    num1=float(input('what is the first number: '))
    go_again = True
    while go_again:


        num2=float(input('what is the second number: '))

        for i in operations:
            print(i)
        operator=input('what operation would you like to use: ')

        answer = operations[operator](num1,num2)

        print(f'{num1} {operator} {num2} = {answer}')
        calc_again=input('wanna add another calc to this one y or n: ')
        if calc_again == 'y':
            num1 = answer
            os.system('cls')
        else:
            go_again = False
            calculator()
            os.system('cls')
calculator()



   



