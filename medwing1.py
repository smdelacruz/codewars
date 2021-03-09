def StarRating(strParam):
    result = ""
    for i in range(1, 6):
        if strParam >=1:
            result += "full "
        elif strParam > 0.00001:
            result += "half "
        else:
            result += "empty "
        strParam -= 1 if strParam != 0 else 0
    return result

# keep this function call here
print(StarRating(2.36))
print(StarRating(4.5))
print(StarRating(0))