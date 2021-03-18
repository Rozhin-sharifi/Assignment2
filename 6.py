sec=int(input("Enter Seconds:\n"))
H=sec//3600
min=(sec%3600)//60
s=min%60
print('time is: ',H,':',min,':',s)