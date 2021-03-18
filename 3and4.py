a=int(input("number 1(big num) = "))
X1=a
b=int(input("number 2 = "))
X2=b
while a%b!=0:
    temp=a
    a=b
    b=temp%b

print("b_m_m=",b)
print("k_m_m=",X1*X2/b)