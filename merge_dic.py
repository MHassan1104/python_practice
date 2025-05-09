# Merge Two Dictionaries: Merge two dictionaries into a single dictionary.

dic1={
    1:"hassan",
    2:"Hannan",
    3:"Hannan",
    4:"Hannan",
}
dic2={
    5:"hassan",
    6:"Hannan",
    7:"Hannan",
}
dic3={}
# dic3= dic1.copy()
dic3.update(dic1)
dic3.update(dic2)
print(dic3)
print(type(dic3))