def get_drink_by_profession(param):
    """
    My Solution
    Complete the function that receives as input a string, and produces outputs according to the following table:
    Input	                Output
    "Jabroni"	            "Patron Tequila"
    "School Counselor"	    "Anything with Alcohol"
    "Programmer"	        "Hipster Craft Beer"
    "Bike Gang Member"	    "Moonshine"
    "Politician"	        "Your tax dollars"
    "Rapper"	            "Cristal"
    anything else	        "Beer"
    """
    dict = {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }
    try:
        return dict.pop(param.title())
    except KeyError:
        return "Beer"
"""
Best answer from other code warriors
"""
d = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}

def get_drink_by_profession(s):
    return d.get(s.lower(), "Beer")

"""
Clever answer
"""
def get_drink_by_profession(param):
    return {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }.get(param.title(), "Beer")


get_drink_by_profession("jabrOni")# "Patron Tequila"
get_drink_by_profession("scHOOl counselor")# "Anything with Alcohol"
get_drink_by_profession("rapper")# "Cristal"
get_drink_by_profession("Pug")# "Beer"