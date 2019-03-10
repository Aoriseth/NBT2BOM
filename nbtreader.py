import nbt
from collections import Counter

nbtfile = nbt.nbt.NBTFile("ae2-basic-terminals.nbt","rb")

recipeList = []
blockList = {}

index = 0
for blockType in nbtfile["palette"]:
	blockList[index] = blockType["Name"]
	index+=1

for block in nbtfile["blocks"]:
	if("nbt" in block.keys()):
		recipeList.append(str(block["nbt"]["id"]))

	if("state" in block.keys()):
		blockType = block["state"].value
		recipeList.append(str(blockList[blockType]))

groupedList = Counter(recipeList)
for x in groupedList.items():
	print(str(x[1])+"x "+x[0])

