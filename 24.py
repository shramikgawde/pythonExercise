from pprint import pprint
 
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
for items,value in d.items():
  print(items, "has value", value)
