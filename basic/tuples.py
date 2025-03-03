#written in round brackets 
#A tuple is a collection which is ordered and unchangeable.
thistuple=("apple","banana","cherry") # all are 0n indexed
print(thistuple)

#we cannot add or remove items from tuple after declaration
# thistuple[1]="orange" #will throw an error
# thistuple.append("orange") #will throw an error
thistuple2=("a","a") # duplicate values are allowed

tuple1 = ("abc", 34, True, 40, "male")
tuple2=tuple(("abc")) #tuple constructor


#update tuple
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

del x # deletes the x