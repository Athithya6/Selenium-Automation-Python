'''
ItemsinCart=0

if(ItemsinCart!=2):
    pass
    #raise Exception("Not able to retrieve products")  #One way of raising execption

assert(ItemsinCart==3)
'''

# try-catch exception mechanism

'''
try:
    with open('test1.txt','a') as f:
        f.append("I am Grute")

except Exception as e:
    print("I somehow reached this except block because of an error in the try block")
    print(e)

finally:
    print("Mandatory statement")
'''
'''
try:
    with open('athithya1.txt', 'r') as f1:
        r=f1.readline()
        print(r)

except Exception as e1:
    print("I somehow reached this except block because of an error in the try block")
    print(e1)

finally:
    print("Mandatory statement")
'''

'''
try:
    with open('test1.text','a') as f:
        f.write("I am Grute")

except Exception as e3:
    print("I somehow reached this except block because of an error in the try block")
    print(e3)

finally:
    print("Mandatory statement")
'''