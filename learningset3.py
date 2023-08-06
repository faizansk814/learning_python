# tuple unpacking
arr=[("John", 25), ("Jane", 30)]
arr1=[]
for i in range(0,len(arr)):
    a=list(arr[i])
    arr1.append(a[0]+ " "+"is"+" " +str(a[1])+ " "+"years old")
print(arr1)
print('.'.join(arr1))

# dictionary manipulation
#  Add "John": 25, Update "John": 26, Delete "John"
def Obj():
    obj={}
    obj["name"]=25
    print(obj)
    obj["name"]=26
    print(obj)
    del obj["name"]
    print(obj)
Obj()

# Two Sum Problem
# Input: [2, 7, 11, 15], target = 9

arr=[2, 7, 11, 15]
k=9
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==k):
            print(i,j)
            break

# Palindrome Check
str="madam"
bag=""
for i in range(len(str)-1,-1,-1):
    bag+=str[i]
if bag==str:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")

# Selection Sort
arr=[2,4,9,7,8]

for i in range(0,len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[min]):
            min=j
    temp=arr[i]
    arr[i]=arr[min]
    arr[min]=temp
print(arr)