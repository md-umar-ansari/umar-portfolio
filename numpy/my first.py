import numpy as np
a1= np.array([1,2,3])#1 dimension
a2=np.array([[]])#2 dimension
a3=np.array([[[]]])#3 dimension
range=np.arange(1,10,2) #arange is used instad of for loop in numpy start,stop,step
print(range)
print(a1.ndim)
print(a1.shape)
print(a2.ndim)
print(a2.shape)
print(a3.ndim)
print(a3.shape)
# linspace used to create evenly spaced numbers
arr=np.linspace(0,1,5) # here the range between 0 to 1 is divided in 5 eqaul parts (start, stop, no. of values betwwen them)
print(arr)
#logspace -> logarithmic space array
arr1=np.logspace(1,3,5) # range is divided in 5 parts but it is to power of 10
arr2=np.logspace(1,4,4)# 4 equal parts 10^each i.e. 10^1,10^2,10^3,10^4 
print(arr1)
print(arr2)
#array full of zeros
arr0=np.zeros([2,3])# we can write an array in any dimension
print(arr0)
#array of ones
arr1=np.ones([2,3])
print(arr1)
#printing the values of our  own
arrf=np.full(10,9)# 10-> no.of times to repeat 9->what to repeat
print(arrf)
arrf1=np.full([3,4],9)#prints a 3,4 array of 9s ([row,column],default value)
print(arrf1)
#uninitialised array
unin=np.empty([2,3])#prints an empty row
print(unin)