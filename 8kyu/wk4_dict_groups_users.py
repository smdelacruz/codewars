# def groups_per_user(group_dictionary):
#     """
#     Unfinished Q2
#     The groups_per_user function receives a dictionary, 
#     which contains group names with the list of users. 
#     Users can belong to multiple groups. Fill in the blanks to return a dictionary with 
#     the users as keys and a list of their groups as values.
#     """
#     user_groups = {}
#     job = []
#     # Go through group_dictionary
#     for groups, users in group_dictionary.items():
#     # Now go through the users in the group
#         print(groups)
#         print(users)
#         for user in users:
#             print(groups, user)
#             if user in user_groups:
#                 user_groups[user] = job.append(groups)
#             # user_groups[user] = groups
#                 print(user_groups)
#             # else: print("exist")
#             # user_groups[user] += groups
#             # print(user_groups)
# 			# Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary

# 	# return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)