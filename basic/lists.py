# #created using square brackets
# thislist = ["apple", "banana", "cherry",3] #can be of different data types
# print(thislist[1]) #print(len(thislist[1])) length of the list
# print(thislist)

# #can be created using list() constructor
# thislist = list(("apple", "banana", "cherry")) 
# print(thislist[-1]) #print last element [-2] is second last and so on

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5]) #print 3 4 5 th items

# thislist[1]="harsad"
# print(thislist)
# thislist.append("fruit")
# print(thislist)   #.remove("harsad") removes specified element

# del thislist[1] #removes specified index
# print(thislist)
# del thislist #deletes the list
# print(thislist) #will throw an error
# thislist.sort() #sorts the list  thislist.reverse() will sort in reverse order


#loops in list
thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)
#----
# for i in range(len(thislist)):
#     print(thislist[i])
#----
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

#copy a list
#list1=list2 will not workl as it will copy the reference
#list1=list2.copy() or list1=list(list2) or list1=list(thislist) will work

#join two lists
#list3=list1+list2