#Code 1
a=10
#bindings and namespaces

#global amd locar variables
#global priority



def add(a,b):
    a=15
    return a+b



#Code 2
a=input("Enter a number")
type(a)

b=input("Enter a number")
type(b)



#Code 3
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))

print(a+b)



#Code 4
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))

if(a>=b & b>=c):
    print(a)

if(b>=a & b>=c):
    print(b)
if(c>=a & c>=b):
    print(c)
    




#Code 5
num=int(input("number="))
if num%2==0:
    print("even")

else:
    print("odd")




#Code 6
num=int(input("number="))
x=bool
z=2
while(num>z):
    if num%z==0:
      
        x = True

    else: 
       
        x= False

    z=z+1

if x==True:
    print("Not Prime")

else :
    print("prime")




#Code 7
import webbrowser
url="https://www.python.org"
webbrowser.open(url , new=0, autoraise=True)



#Code 8
import webbrowser
webbrowser.open_new("https://www.python.org")
