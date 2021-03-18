from random import randint


value = randint(0, 10)
inputN=-1
counter=0
while inputN!=value:
    inputN=int(input("Adad ra hads bezanid:\n"))
    counter+=1
    if inputN==value:
        print("you did it!")
        print(counter)
        break

    if inputN>value:
        print ("go down")
    else:
        print("go up")