#Dictionary key, value pair

LIST = ["a","b","c"]
print(LIST[2])


person = {
    "name": "Mary",
    "occupation":"Developer",
    "age": 24
}

#Print age
print(person["age"])
print("\n+1 = ")
person["age"] = 25
print(person["age"])

#retrieve the values from above
print(person["name"])

#We want to know all of the different keys that are in the list
print("\nPrint all different keys in list:")
for x in person:
    print(x)

print("\nPrint all different values in list:")
for x in person.values():
    print(x)

#find if a person has an age assigned
if "age" in person:
    print("Person has age")
if not "taco" in person:
    print("Person has taco")

#Evaluate the lenght of person
print("\nThe lenght of person is: ")
print(len(person))

#new key name that does NOT exist in dictionary/list
print("\nThe shirt size of person is: ")
person["shirtSz"] = "M"
print(person)

#remove the key name:
print("\nDELETE the person age: ")
del person["age"]
print(person)

#additionally you can give the "age" value an empty string:
print("\nEMPTY value for person age: ")
person["age"] = ""
print(person)
