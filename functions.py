# Simple python program to find sunm of n number
import calendar
import os 
import sys
import time

def suM():
    num=int(input("Enter Number : "))
    if num<0:
        print("Enter a Positive Number")
    else:
        sum=0
        while (num>0):
            sum+=num
            num-=1
        print(f" THe sum is {sum}") 
            
suM()             
#     #check a number is divisibleble by a list or not
def diviL():
    n1=int(input("NUmber : "))
    n2=int(input("NUmber : "))
    n3=int(input("NUmber : "))
    n4=int(input("NUmber : "))
    lis=[n1,n2,n3,n4]
    result=list(filter(lambda x:(x%2==0),lis))
    print("Numbers Divisible by 2 are",result)
    
diviL()

    #print out the calender of the year and month
def calDa():
    yer=int(input("Enter Year : "))
    mon=int(input("Month : "))
    print(calendar.month(yer,mon))
    
calDa()
        
        # make a simple calculator to amke calculation it take only two inputs
        
def calcu():
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mult(x,y):
        return x*y
    def divd(x,y):
        return x/y    
    print("Please select Operators")
    print("1,Add")        
    print("2,Substract")        
    print("3,Divide")        
    print("4,Multi")   
    while True:
        choice=input("Enter Choice 1,2,3,4")
        if choice in ("1","2","3","4"):
            n1=int(input("Number  One : "))     
            n2=int(input("Number  Two : "))     
            if choice =="1":
                print(n1, "+",n2, "=", add(n1,n2))
            elif choice =="2":
                print(n1, "-", n2, "=",sub(n1,n2))
            elif choice =="3":
                print(n1, "/", n2, "=", divd(n1,n2))
            elif choice =="4":
                print(n1, "*", n2, "=",mult(n1,n2))                                    
            break
         
        
calcu()        

#
print(os.getcwd())  #list path of worlking
print(os.listdir())     #list files in folder
asz=os.listdir()
asa=asz[0]

# function that print out the dimensions of teh photo
def dimesn(file):
    with open(file,"rb") as img_fil:
        img_fil.seek(165)
        a= img_fil.read(2)
        # calculate height
        height=(a[0]<<8)+a[1]
        # next two bytes in bytes
        a=img_fil.read(2)
        # with
        withs=(a[0]<<8)+a[1]
        print(f'Resolution of photo is Height:{height} with:{withs}')
        
dimesn(str(asa))
         

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(5)

         