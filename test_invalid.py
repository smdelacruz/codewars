def foo(mylist):
    for i in mylist:
        print("ii", i)
        if i %2==1:
            print(i)
        else: break
    else: print(float('inf'))

print(foo([13,12, 90]))