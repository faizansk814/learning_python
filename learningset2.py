import math
# pattern printing
for i in range(1, 6):
    bag = ""
    for j in range(1, i + 1):
        bag += str(j) + " "
    print(bag)

# print on condition
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(0,len(numbers)):
    if(numbers[i]>500):
        break
    elif numbers[i]>150:
        continue
    elif numbers[i]%5==0:
        print(numbers[i])

# append in middle
s1 = "Ault"
s2 = "Kelly"
bag3=""
for i in range(0,len(s1)):
    if(i==math.floor(len(s1)/2)):
        bag3+=s2
        bag3+=s1[i]
    else:
        bag3+=s1[i]
print(bag3)

# lower first
str1 = "PyNaTive"
l="abcdefghijklmnopqrstuvwxyz"
bag1=""
bag2=""

for i in range(0,len(str1)):
    if str1[i] in l:
        bag1+=str1[i]
    else:
        
        bag2+=str1[i]
print(bag1+bag2)

# concatenate 
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

for i in range(0,len(list1)):
    list1[i]=list1[i]+list2[i]
print(list1)

# concatenate
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        list3.append(list1[i]+list2[j])
print(list3)

# print
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(0,len(list1)):
    print(list1[i],list2[i])


# choose
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

obj={}
for i in range(0,len(keys)):
    obj[keys[i]]=sample_dict[keys[i]]
print(obj)

# convert 

tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1)
list1[1][0] = 222
modified_tuple = tuple(list1)
print(modified_tuple)

