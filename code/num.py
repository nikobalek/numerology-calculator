uInput = input("Enter your name: ")
uinput = uInput.lower()
list = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numList = []

for count in uInput:

    if count == ' ':
        continue

    elif list.index(count) <= 9:
        numList.append(list.index(count))

    elif list.index(count) > 9 and list.index(count) <= 18:
        numList.append(list.index(count)-9)

    elif list.index(count) > 18:
        numList.append(list.index(count)-18)

for count in numList:
    print(count,end=' ')

print()