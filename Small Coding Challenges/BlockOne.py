'''
Per challenge available on https://edabit.com/challenge/u4rHyBDs5RM2PfNxy:
Create a function that counts the number of blocks of two or more adjacent 1s in a list.
'''

def screen_clear():
    for number in range(0,100):
        print("")

def one_block(mylist):
    countlist = []
    onecounter = 0
    blockcounter = 0
    for number in mylist:
        countlist.append(number)
    print(countlist)
    for number in countlist:
        print(number)
        if number == 1:
            onecounter +=1
            print("Onecounter is at {}".format(onecounter))
        else:
            onecounter = 0
            print("Onecounter set to 0")
        if onecounter == 2:
            blockcounter +=1
            print("Blockcounter at {}".format(blockcounter))
    print(onecounter)
    print(blockcounter)

screen_clear()
numbers = [0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1]
print(numbers)
one_block(numbers)