def combine_lists(list1, list2):
    return list2 + list1[::-1]

	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))



['Mike', 'Carol', 'Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Alice']


