#Write a python program to locate the left insertion point for a specified value in sorted order.
import bisect
n=int(input("enter the number of elements you want to insert"))
a=[]
for i in range(0,n):
    t=int(input("enter the element"))
    a.append(t)
a.sort()
num=int(input ("enter the number to be inserted "))
print ("the sorted array is",a)
s=bisect.bisect_left(a,num)
bisect.insort(a,num)
print(s)
print(a)
