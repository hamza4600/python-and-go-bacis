# numpy
import numpy as np
from numpy.core.defchararray import rpartition 

# slice method take  elemnt  from a given index to another index
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:4])
#  copy last elemt from a array
print(arr[4:]) 
# copy from the begaining 
print(arr[:4])
# Data type in Python  support all Data types
# check data type of array dtype
print(arr.dtype)
# we can also set the Data type of array 
adz=np.array([1,2,3,5,6,9,8,71], dtype="S")
print(adz.dtype)
print(adz)

# diffrence between View and copy if we made a copy of arr it copy elemnts from a array  and in view if we do so it will but any chnge in view will make change in the orignal array
d=arr.copy()
print(d)
arr[0]=20
print(d)
print(arr)

# Now we will use View() as we define 
z=arr.view()
z[2]=2150785
print(z)
print(arr)

# we can also change the shape of array and dimension we have defien 
# convert 1-D into 2-D array

aww = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newaw=aww.reshape(4,3)
print(newaw) # create four arrays with 3 items  inside a array

# convert a 1-D into 3-D array
xewaw=aww.reshape(2,3,2)
# creat  two arrays in that  create creat 3 arrays and with 2  elemnts
print(xewaw)
# we can also reshape the two arays intio single aray
qqs=newaw.reshape(-1)
# back to orignal Position and shape
print(qqs)


# itteratyion items from array
# mostaly we use for loop to iterate items from a array
thrD = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in thrD:
    for z in x:
        for i in x:
            print("all itens are below ")
            print(i)
            
            #using nditer function to iterate items from a array
for k in np.nditer(thrD):
    print(k)             
    
    # we can also add two array in single array sing concatenate(1,2)
    # we will add two arrays in same way dimensions
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr3 = np.concatenate((arr1, arr2), axis=1)     
print(arr3)

# split is reverse of join()  we can creat nultilpe arrays from  a single arrays
nex=np.array_split(aww,4)
# creat foure arays from a single array
print(nex)

# find is used to find item from a array
df=np.where(aww%2==0)
# print the odd numbrs
print(df)
# print even numbers
dz=np.where(aww%2==1)
print(dz)
# searchsort is used to find elmt  by index value 
pda=np.searchsorted(aww,6)
print(pda)

# sort is used to arrange items in order sequience 
zrr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(zrr))

# Filtter is  used to get elemnt from a existing array and add to new array

filter_arr=[]
for elemnt in aww:
    if elemnt%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        # newarrr=arr[filter_arr]
            
print(filter_arr)
# print(newarrr)            