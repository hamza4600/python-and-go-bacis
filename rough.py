# writtenig differnts patterns in terminal
from termcolor import colored
import time
import threading
def patter():
    rows=int(input("Enter NUmber of rows : "))
    k=0
    for i in range(1, rows+1):
        for space in range (1,(rows-i)+1):
            print(end="  ")

        while k!=(2*i-1):
            print("*",end="")
            k+=1
        k=0
        print()                
        
patter()        

print(colored("Hamza","yellow"))


# measuring the timr of a code
def timx():
    start=time.time()
    for a in range(100000):
        print("Hamza")
    end=time.time()
    print(end-start)
    
timx()        
