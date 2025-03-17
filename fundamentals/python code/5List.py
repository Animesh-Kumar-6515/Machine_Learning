lst=[1,2,3,4,5,3]

print(lst)
print(len(lst))

lst2=[1,"aniwsh",True]
print(lst2)

print(type(lst))

print(lst[2:4])

lst[1:4]=[9]
print(lst)

lst.insert(2,23)
print(lst)
lst.append(24)
lst.extend(lst2)

lst.remove("aniwsh")
print(lst)
lst.pop(1) # remove the second element
lst.pop() # pop the last element

del lst[0] # delete the first element
# del lst # del the entire list 


for i in lst:
    print(i)

for i in range(len(lst)):
    print(lst[i])

while i<len(lst):
    print(lst[i])
    i+=1

lst.sort() # will sort the array
lst.sort(reverse=True)

lst.reverse()

newlst=lst.copy()
print(newlst)
