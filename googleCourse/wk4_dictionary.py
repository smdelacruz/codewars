file_counts = {"jpg":10, "txt":14, "csv":2,"py":23}

for extension in file_counts:
    print(extension) #jpg, txt, csv,

for extension, amount in file_counts.items():
    print("There are {} files with .{} extension".format(amount, extension)) #There are 10 files with .jpg extension


print(file_counts.keys()) #dict_keys(['jpg', 'txt', 'csv', 'py'])
print(file_counts.values()) # dict_values([10, 14, 2, 23])