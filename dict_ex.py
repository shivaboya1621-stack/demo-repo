#dictionary
#key and value parts
# {}
# keys are "immutable" but values are "mutable"

# d1 = {
#     "name" :"samba",
#     "age" : 40
# }
# print(d1)

# d2 = dict(name="samba",age=40)
# print(d2)

# print(d1["name"])
# print(d2.get("name")) #Both lines are used to access values from a dictionary in Python, but they behave differently when the key does not exist.

# d1 = {}
# d1["name"] = "Shiva"
# d1["age"] = 40
# print(d1)
 
# d1["age"]= 35
# print(d1)

# d1.pop("age")
# print(d1)

# d1.popitem()
# print(d1)

# # del d1["age"]
# # print(d1)

# d1.clear()
# print(d1)

# d1 = {
#     "name" : "shiva",
#     "age" : 28  
# }
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# for key in d1:
#     print(key)
# for value in d1.values():
#     print(value)
# for key,value in d1.items():
#     print(key,value)



#print({x:x*x for x in range(1,6)})

# d1 = {
#     (10,20) : "Hello"
# }
# print(d1)



# d1 = {
#     "name" : "`shiva"
# }
# print("name" in d1)
# print("age" in d1)
# print("name" not in d1)
# print("age" not in d1)


