#practicegreatestnum4
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
d = int(input("enter the fourth number:"))
if(a>=b and a>=c and a>=d):
    print("first is greatest" , a)
elif(b>=c and b>=d):
    print("second is greatest" , b)
elif(c>=d):
    print("third is greatest" , c)
else:
    print("fourth is greatest" , d)