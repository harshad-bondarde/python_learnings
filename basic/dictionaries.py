# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# #ordered changeable and indexed
# print(thisdict['brand'])

dict1=dict(name='john',age=36,city='new york')
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())

if('name' in dict1):
    print("yes")    
else:
    print("no") 
dict1.pop('city') # or del dict1['city']
#dict1.popitem() #removes the last item

for x in dict1:
    print(x) #prints the keys
for x in dict1:   
    print(dict1[x]) #prints the values
for key in dict1.keys():
    print(key)
for value in dict1.values():    
    print(value)    
for x,y in dict1.items():
    print(x,y)

#nested dictionaries
myfamily={
    "child1":{
        "name":"emma",
        "year":2004
    },
    "child2":{
        "name":"john",
        "year":2007
    },
    "child3":{
        "name":"mike",
        "year":2011
    }
}
print(myfamily["child1"]["name"])