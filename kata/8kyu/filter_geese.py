geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    """
    My solution
    takes an array of strings as an argument and returns a filtered array containing the same elements
    but with the 'geese' removed.
    The geese are any strings in the following array, which is pre-populated in your solution:
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    """
    goose = []
    for bird in birds:
        if bird not in geese:
            goose.append(bird)
    return goose

def goose_filter(birds):
    """
    Best solution in codewars
    """
    return [bird for bird in birds if bird not in geese]


# goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) #,["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
# goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]) #["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]) #["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]