uInput = input("Enter your name: ")
uinput = uInput.lower()
list = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
numList = []

count2 = 0

for count in uInput:

    if list.index(count) <= 9:
        numList.append(list.index(count))

    elif list.index(count) > 9 and list.index(count) <= 18:
        numList.append(list.index(count)-9)

    elif list.index(count) > 18:
        numList.append(list.index(count)-17)

print(numList)    