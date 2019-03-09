import nbt
from collections import Counter

nbtfile = nbt.nbt.NBTFile("ae2-basic-terminals.nbt","rb") 
# print(nbtfile.keys())
# print(nbtfile["blocks"])
# print(type(nbtfile["blocks"]))
# print(nbtfile.pretty_tree())

recipeList = []

for x in nbtfile["blocks"]:
	# print(x["nbt"])
	# print(x["nbt"]["id"])
	recipeList.append(str(x["nbt"]["id"]))
	# for y in x["nbt"]:
	# 	print(y)
	# 	pass
	pass


# print(recipeList)

groupedList = Counter(recipeList)
for x in groupedList.items():
	print(str(x[1])+"x "+x[0])

