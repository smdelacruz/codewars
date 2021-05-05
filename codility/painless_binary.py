def solution(N):
    binary = str(format(N, 'b'))
    print(binary)
    start = ""
    end = ""
    counter = 0
    for i in range(len(binary)):
        if start == "" and binary[i] == '1':
            start = binary[i] 
        elif start != "" and binary[i]  == '1':
            end = binary[i]
            return counter
        else: 
            counter += 1
    return counter if end != "" else 0



print(solution(9))
print(solution(1))
print(solution(6291457))



