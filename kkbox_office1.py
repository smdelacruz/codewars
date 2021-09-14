def solution(arr):

    holder = []
    total_counter = 0
    char_counter = 1
    for i in range(len(arr)):
        print("-----------------")
        char = arr[i]
        print("current char", char)
        if i != 0:
            print("not first")
            if arr[i-1] != char:
                char_counter = 1
                total_counter +=1
                holder.append(char)

            if arr[i-1] == char:
                holder.append(char)
                char_counter += 1
                total_counter += 1
                if char_counter > 2:
                    print("more than 2", i)
                    holder = []
                    holder = arr[i-1:]
                    print(holder)
                    # total_counter -= 1
        elif i == 0:
            total_counter += 1
            holder.append(char)
        else: print("else")
        print("holder", holder)
        print("total_counter", total_counter)
        print("char_counter", char_counter)



# print(solution('baaabbabbb')) #7
print(solution('baaab')) #3