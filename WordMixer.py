import random

def rearrange(list):
    listamount = len(list)
    newlist = []
    for i in range(amountofwords):
        randomword = random.randint(0, listamount-1)
        newlist.append(list[randomword])

    for i in newlist:
        print(i)


amountofwords = int(input("Give the max words in numbers: "))

inputlist = []

for i in range(amountofwords):
    userinput = input("Input words: ")
    inputlist.append(userinput)

rearrange(inputlist)
