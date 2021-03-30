def maxTickets(tickets):
    sorted_tickets = sorted(tickets)
    p1 = []
    p2 = []
    # counter = sorted_tickets[0]
    dictt = {}
    x = 0
    # print("len(tickets)", len(tickets)+1)
    # while x != len(tickets)+1:
    #     print("x", x)
    #     print("sorted_tickets[x+1]", sorted_tickets[x+1])
    #     print("sorted_tickets[x]", sorted_tickets[x])
    #     if sorted_tickets[x+1] - sorted_tickets[x] == 1:
    #         print("sorted")
    #     elif sorted_tickets[x+1] == sorted_tickets[x]:
    #         print("sorted")
    #     else: print("not sorted")
    #     x += 1

    for k, v in enumerate(sorted(tickets)):
        if v == tickets[k+1]:
            print("seq")
        elif v + 1 == v:
            print("Sql")
        else: print("not sq")
    # print(counter)
    # counter = 1
    # for i in range(len(tickets)):
    #     print("so", sorted_tickets[i])
    #     # print("co", counter)
    #     if sorted_tickets[i] == counter:
    #         p1.append({"if{}".format(i): sorted_tickets[i]})
    #     elif sorted_tickets[i+1] - sorted_tickets[i] == 1:
    #         p1.append({"p{}".format(i): sorted_tickets[i]})
    #     else:
    #         p1.append({"pppp{}".format(i): sorted_tickets[i]})
    #     counter += 1
    # # return max(len(p1), len(p2))


# print(maxTickets([4,2,3,15]))
# print(maxTickets([8,5,4,8,4]))
print(maxTickets([12,10,10,4,5,1]))