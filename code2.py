'''
a=100
b=1120

if a>b:
    print("a greater than b")
elif a<b:
    print("a lesser than b")
else:
    print("a equal to b")
'''

'''
name = "Athithya"
print("my name is",name,end="\n")
print("my name is",name,end="///////",sep="--")
'''

'''
mylist=[3,4,5,4,3,5,4,33,678]
print(mylist)
for i in mylist:
    print(i)

for i in range(len(mylist)):
    print(mylist[i])
'''

'''
for i in range(10):
    print(i)

t1=[]
t2=[]
for k in range(4,15):
    t1.append(k)
    t2.append(k*8)
print(t1)
print(t2)
'''

'''
for m in range(1,100,12):
    print(m)
'''

'''
i=2
while(i<=20):
    print(i-1)
    i+=1
'''

'''
list=[5,89,-7,43,-66,12,1,8]
for i in list:
    if(i==-66):
        break
    print(i)
'''

'''
list=[5,89,-7,43,-66,12,1,8]
for i in list:
    if(i==-66):
        continue
    print(i)
'''

list=[5,89,-7,43,-66,12,1,8]
for i in list:
    pass