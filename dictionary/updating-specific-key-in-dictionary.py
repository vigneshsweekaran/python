vars = [
    {
        "name": "vignesh",
        "skill": "python",
        "age": 26

    },
    {
        "name": "yeshwanth",
        "skill": "python",
        "age": 25
    },
    {
        "name": "yeshwanth",
        "skill": "python",
        "age": 25
    }
]

#Option1:  If we use For loop it will change the specific data in all dictionary
for value2 in vars:
    print(type(value2))
    print(value2)
    value2["name"]="Ram"

print(vars)

# option2 : If we want to update only one dictionary we should not use for loop
vars[0]["name"]="Alachal"
print(vars)

# option3 : Updating specific value in one dictionary using for loop
for value2 in vars:
    print(type(value2))
    print(value2)
    if value2["name"]=="Alachal":
        value2["name"]="Bhaskar"

print(vars)
