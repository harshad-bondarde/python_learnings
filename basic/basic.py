# print("HI")
# variables can be changed 
x=3
x="harshad"
print(x)

# casting 
a=str(3) # a will be '3'
print(type(a)) #will print <class 'str'>

z=float(3) # z will be 3.0 


# many values to multiple variables in single line
a,b,c=1,2,3  # or this could be a=b=c=4
print(a,b,c)

#unpack a collection
fruits=['apple','banana','cherry']
[a1,b1,c2]=fruits
print(a1,b1,c2)


#data types
u=5+1j #complex j is a imagianry part
u1=["apple","banana","cherry"] #list
u2=("apple","banana","cherry") #tuple  
u3=range(6) #range
u4={"name":"John","age":36} #dictionary
u5={"apple","banana","cherry"} #set 
u5=frozenset({"apple","banana","cherry"}) #frozenset 


#strings 
a="Hello, World!"
print(a.upper()) #upper case
print(a.lower()) #lower case

a='hsdfsdf,sdfsd,ddd'
print(a.split(",")) #split by comma

age=36
# txt="My name is John , I am "+age will throw an error
txt=f"My name is John , I am {age}" #string formatting
print(txt)

#python booleans
a=200
b=33
if(b>a):
    print("b is greater than a")
else:
    print("b is not greater than a")
#any string is true except empty string
#any number is true except 0
#Any list, tuple, set, and dictionary are True, except empty ones.