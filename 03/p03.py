# Define New Functions

def A():
    print("Hello, World!")

def B():
    name = input('Who are you? \n')
    print('Hello,', name, '!')

def C():
    Celsius = input('Temperature in Celsius: ')
    Fahrenheit = float(Celsius) * 1.8 + 32
    print('Temperature in Fahrenheit:', Fahrenheit)

# ------------------------------------------------------------------------------------------------------------------
# Main Program

n = input('Welcome! Please choose one of the following: \nA. Greeting  \nB. Personalized Greeting  \nC. Temperature Convertion \nD. Exit \nInput example: A \n')

while n != 'D' :

    if n == 'A' :
        A()
    else :
        if n == 'B' :
            B()
        else :
            if n == 'C' :
                C()
            else :
                print('Invalid input. Please try again.')

    n = input('\nWhat would you like to try next? \nA. Greeting  \nB. Personalized Greeting  \nC. Temperature Convertion \nD. Exit \n')
    
print('\nThanks for using! \n')

exit()