# for random numbers bertween ranger
import random
print(random.randint(0,10))

# CONVERT km into miles
def miles():
    kilo=float(input("Value in Kilometer : "))
    conv=0.6213785
    miles=kilo*conv
    print(f"value in miles id {miles}")
    
miles()    

# check a number is positive or not 
def postiv():
    num=float(input("Entr the Number : "))
    if num >0:
        print(f" It is Positive Number")
    elif num ==0:
        print("Number is equal to zero")
    else:
        print("Number is negative")                        

postiv()


#  check which number is largerst
def larg():
    n1=float(input("Number One : "))
    n2=float(input("Number Two : "))
    n3=float(input("Number Three : "))
    if (n1>=n2) and (n1>=n3):
        largest=n1
    elif (n2>=n1) and (n2>=n3):
        largest=n2
    else:
        largest=n3
    print(f"largest Number is {largest}")    
    
# larg()    

# find factorial of given Number
def factr():
    num=int(input("Entr Number : "))
    factoril=1
    if num<0:
        print("Factorial of Negitive does,t exist")
    elif num==0:
        print("factroial od Zero is 1 ")    
    else:
        for i in range(1,num + 1):
            factoril=factoril*i 
        print(f"Factorial of {num} is {factoril}")                            
        
# factr()        

# Print the Number Between in range 
def ranz():
    nu1=int(input("Number One : "))
    nu2=int(input("Number Two : "))
    print(f"Number Between {nu1} and {nu2} :")
    for num in range(nu1,nu2+1):
        if num>0:
            print(num)

# ranz()            
            

#  Oddes Number in a range
def evz():
    nu1=int(input("Number One : "))
    nu2=int(input("Number Two : "))
    print(f"Odd Number Between {nu1} and {nu2} :")
    for num in range(nu1,nu2+1):
        if (num>0) and (num%2):
            print(num)

evz()

# Only Print even Number in a range
            
def evdd():
    nu1=int(input("Number One : "))
    nu2=int(input("Number Two : "))
    print(f"Odd Number Between {nu1} and {nu2} :")
    for num in range(nu1,nu2+1):
        if (num>0) and (num%2==0):
            print(num)
evdd()            

# simple Python Program to Print Table of Given NUmber
def table():
    num=int(input("Enter Number : "))
    for i in range(1,num):
        print(num, "x", i, "=",num*i)
        
# table()        

# it is obtain by adding first two value s Print out the Fibonichi sequience of a n term
def febonic():
    print("Please enter Positive and Nmber Great than 0")
    num=int(input("Nmber : "))
    n1,n2=0,1
    count=0
    print("Sequence is : ")
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
febonic()        

