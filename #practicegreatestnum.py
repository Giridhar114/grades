#practicegreatestnum
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if(a>=b and a>=c):
    print("first is greatest" , a)
elif(b>=c):
    print("second is greatest" , b)
else:
    print("third is greatest" , c)