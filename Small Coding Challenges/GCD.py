'''
Per challenge available on https://edabit.com/challenge/55MKEWCYzhxSTdnEr:
Create a function that returns the Greatest Common Denominator of two numbers.
'''

def screen_clear():
    for number in range(0,100):
        print("")

def GCD(num1,num2):
    num1dens = []
    for devisor in range (1,num1):
        if num1 % devisor == 0:
            num1dens.append(devisor)
    num2dens = []
    for devisor in range (1,num2):
        if num2 % devisor == 0:
            num2dens.append(devisor)
    comdens = []
    for testnum in num1dens:
        for num in num2dens:
            if testnum == num:
                comdens.append(testnum)
    return(comdens[-1])

screen_clear()
print("Enter 1st number (Please enter a whole number)")
usernum1 = int(input(""))
screen_clear()
print("Enter 2nd number (Please enter a whole number)")
usernum2 = int(input(""))
screen_clear()
print("The lowest common denominator is")
print(GCD(usernum1,usernum2))