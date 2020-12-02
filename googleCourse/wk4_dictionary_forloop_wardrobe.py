wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for k,v in wardrobe.items():
    for pp in v:
        print("{} {}".format(pp, k))