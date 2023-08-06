# Anagram Check
# Input: "cinema", "iceman"
str1="cinema"
str2="iceman"
str1=''.join(sorted(list(str1)))
str2=''.join(sorted(list(str2)))
if str1==str2:
    print("Its an anagram")
else:
    print("Not an anagram")

# Bubble sort
# Input: [64, 34, 25, 12, 22, 11, 90]
list= [64, 34, 25, 12, 22, 11, 90]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)

# Missing Number
arr=[3,0,1]
arr=sorted(arr)
for i in range(1,len(arr)):
    if arr[i]-arr[i-1]>1:
        print(arr[i]-1)

# Number of ways
def Number(n):
    if n<0:
        return 0
    if(n==0):
        return 1
    else:
        return Number(n-1)+Number(n-2)
print(Number(3))

# Power or not
def Power(n):
    product=2
    while(product<n):
        product*=2
    if(product==n):
        return True
    else:
        return False
print(Power(6))

# Duplicate in array
def Duplicate(arr):
    obj={}
    for num in arr:
        if num not in obj:
            obj[num]=1
        else:
            return False
    return True
    



