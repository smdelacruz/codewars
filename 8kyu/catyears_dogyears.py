"""
I have a cat and a dog.
I got them at the same time as kitten/puppy. That was humanYears years ago.
Return their respective ages now as [humanYears,catYears,dogYears]
NOTES:
humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""


def human_years_cat_years_dog_years(human_years):
    """
    my solution
    """
    cat_years = 0
    dog_years = 0
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    elif human_years > 3:
        multiplier = human_years - 2
        cat_years = (15 + 9) + (multiplier * 4)
        dog_years = (15 + 9) + (multiplier * 5)
    return [human_years,cat_years,dog_years]


print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))