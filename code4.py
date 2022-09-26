#data structures-June 6th
# 1. List- ordered, duplicate and mutable
mylist = [3,33,-100,-567,32,137,-331,0x22,-331,0o11,3,-6,87,131,-331,33,5,2022,3,6,-33,33]
'''
print(dir(mylist))
print(type(mylist))
print(mylist)
'''
'''
res = mylist.pop(5)
print(res)
print(mylist)
'''

'''
res1 = mylist.remove(0x22)
print(res1)
print(mylist)
'''

'''
mylist.clear()
print(mylist)
'''

'''
del mylist
print(mylist)
'''

'''
mylist[2]="Vikram"
print(mylist)

mylist.insert(2,-100)
print(mylist)

mylist.append(1987)
print(mylist)
'''

'''
#slicing
print(mylist[:])
print(mylist[2:6])
print(mylist[:7])
print(mylist[3:])
print(mylist[-1])
print(mylist[-2:])
print(mylist[:-3])
print(mylist[-6:-3])
print(mylist[::3])
'''

'''
for k in mylist:
    print(k)
for i in range(len(mylist)):
    print(f"index is {i} and correspodning item is {mylist[i]}")
'''

'''
l1 = mylist.copy()
print(type(l1))
print(l1)

l2 = mylist.reverse()
print(type(l2))
print(l2)
print(mylist)
'''

'''
mylist.sort() #ascending order
print(mylist)

mylist.sort(reverse=True) #descending order
print(mylist)
'''

'''
res1 = mylist.count(-331)
print(res1)

res2 = mylist.index(0x22)
print(res2)
'''

'''
newlist = ["leap year","amy adams","anand tucker","amma","dublin","ireland"]
e_list=[]
for i in newlist:
    if "e" in i:
        e_list.append(i)
print(e_list)

#list comprehension
newlist2 = [k for k in newlist if "m" in k]
print(newlist2)

newlist3 = [j.upper() for j in newlist]
print(newlist3)
'''

'''
lA=["jdwhbhc","oeoiwui","nxcnzvnz",23456781]
lB=[65432111,"vchdsvcdbsvc","bhcvdgvfhdsvg","hjwhbjbhad"]
lC=[]
lC=lA+lB
print(lC)
'''

#tuples
#order, duplicates and immutable
