#replace second elemet b=1
b = [0,0,0]
b[1] = 1
print(b)


#itereate over a list using 'for element in...'
c_list = ['item0','item1','item2']
for element in c_list:
    print(element)

#itereate over a list using 'for element in range...'
d_list = ['item0','item1','item2']
for element in range(len(d_list)):
    print(d_list[element])


#find the sum of e_list
e_list = [32,55,710, 1]
total = 0
for i in e_list:
    total += i
print(total)