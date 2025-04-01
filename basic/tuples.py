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

#unpacking of the tuples 
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
# green is apple
# yellow is banana

fruits=("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red)=fruits # * is used to assign the rest of the values to the last variable
print(red)

#join in tuples
tuple1=("a","b","c")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)
print(tuple1*2)