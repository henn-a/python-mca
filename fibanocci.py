list1=[]
a=0
b=1
size=int(input("enter the length of fibonacci serise:"))
for i in range(size):
    list1.append(a)
    a,b=b,a+b
print(list1)
