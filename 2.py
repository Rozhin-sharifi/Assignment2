from random import randint

print("Tas berizid:(y/n)")
char=input()
flag=True
if char=="y":
    while flag:
        Tas = randint(1, 6)
        print(Tas)
        if Tas==6:
            print("You Have Prize!\n one more time")
            Tas = randint(1, 6)
            print(Tas)
            flag=False
else:
    exit