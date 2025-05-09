 # Common Elements in Two Lists: Find common elements between two lists.
#
list1 = ["Apple", "banana", "shake", "Strawberry", "Mango", "orange"]
List2 = ["Apple", "banana", "shake", "watermelon", "Guava", "banana"]
common_item = []
for i in list1:
    if i in List2:
        common_item.append(i)
print(common_item)