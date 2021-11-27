import threading
import time

onx=time.time()

def one():
    for i in range(1000000):
        print("Hamza")
        
def two():
    for j in range(1000000):
        print("C+++")
        
t1=threading.Thread(target=one)                
t2=threading.Thread(target=two)                

def start():
    star=time.time()
    t1.start()
    t2.start()
    end=time.time()
    print(end-star)
    
# start()  
one()
two()  
twx=time.time()
print(twx-onx)     
# it take 40 second to complete this two loops