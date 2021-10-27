def hydrate(drink_string): 
    water = []
    for i in drink_string:
        if i.isdigit():
            water.append(int(i))
    glass = sum(water)

    return "{} glass of water".format(glass) if glass == 1 else "{} glasses of water".format(glass)

print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"))