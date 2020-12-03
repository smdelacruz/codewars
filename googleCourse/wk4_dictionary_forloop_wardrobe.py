wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes_type,colors in wardrobe.items():
    for color in colors:
        print("{} {}".format(color, clothes_type))


print("big" > "small")