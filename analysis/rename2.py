import os
# for fname in os.listdir("."):
	# os.rename(fname, fname.replace("?", ""))
# 	if ".wav" in fname:
# 		split_fname = fname.split("_")
# 		new_fname = "stressTurk_" + "" + split_fname[0] + "_" + split_fname[1] + "_" + "_".join( split_fname[2:] )
# 		os.rename( fname, new_fname )
# 	if ".TextGrid" in fname:
# 		split_fname = fname.split("_")
# 		new_fname = "stressTurk_" + "" + split_fname[0] + "_" + split_fname[1] + "_" + "_".join( split_fname[2:] )
# 		os.rename( fname, new_fname)

path = os.getcwd()
filenames = os.listdir(path)

# for filename in filenames:
#     os.rename(filename, filename.replace(" ", ""))

# for filename in filenames:
#     os.rename(filename, filename.replace("?", ""))

# for filename in filenames:
#     os.rename(filename, filename.replace("Item_Sandy", "ItemSandy"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Item_Bonnie", "ItemBonnie"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Item_Billy", "ItemBilly"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Item_Dory", "ItemDory"))


# for filename in filenames:
# 	# print filename
# 	# print filename.replace("Sandy", "ItemSandy_Sandy")
# 	os.rename(filename, filename.replace("ItemItemSandy_Sandy_ItemItemSandy_Sandy_Andy", "ItemSandy_Andy"))



# for filename in filenames:
# 	os.rename(filename, filename.replace("VersionC.wav_1", "VersionC_1.wav"))


# for filename in filenames:
# 	os.rename(filename, filename.replace("VersionC.wav_2", "VersionC_2.wav"))

# for filename in filenames:
# 	os.rename(filename, filename.replace("VersionC.wav_3", "VersionC_3.wav"))
# for filename in filenames:
# 	# print filename
# 	# print filename.replace("Sandy", "ItemSandy_Sandy")
# 	os.rename(filename, filename.replace("Sandy", "ItemSandy_Sandy"))





# for filename in filenames:
#     os.rename(filename, filename.replace("Andy", "ItemSandy_Andy"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Pull_IS", "ItemSandy_Pull"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Bonnie", "ItemBonnie_Bonnie"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Donny", "ItemBonnie_Donny"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Kick_IS", "ItemBonnie_Kick"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Billy", "ItemBilly_Billy"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Jilly", "ItemBilly_Jilly"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Kiss_IS", "ItemBilly_Kiss"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Dory", "ItemDory_Dory"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Laurie", "ItemDory_Laurie"))

# for filename in filenames:
#     os.rename(filename, filename.replace("Poke_IS", "ItemDory_Poke"))






# for filename in filenames:
#     os.rename(filename, filename.replace("NA", "Filler_NA"))


# for filename in filenames:
#     os.rename(filename, filename.replace("stressTurk__", "stressTurk_"))

for filename in filenames:
    os.rename(filename, filename.replace("TextGrid\r","TextGrid"))