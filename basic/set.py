#set is unordered , unchangeable and unindexed collection of items
#can remove and add items
thisset={"apple","banana","cherry"} #duplicates are not allowed
print(thisset)

set1={"abc",34,True,40,"male"}

# for x in thisset:
#     print(x)

print("banana" in thisset) #true
thisset.add("orange")
tropical={"pineapple","mango","papaya"}
thisset.update(tropical) #add elements of tropical to thisset
mylist=[1,2,3]
thisset.update(mylist) #add any iterable to the set
thisset.remove("banana") #if the item does not exist it will throw an error
thisset.discard("banana") #if the item does not exist it will not throw an error
thisset.pop() #removes the last item
thisset.clear() #empties the set
del thisset #deletes the set

#union of sets
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2) # or set3=set1|set2
#join mulitple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#intersection of sets use &
