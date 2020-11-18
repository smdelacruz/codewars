def past(h, m, s):
    """
    Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
    Your task is to make 'Past' function which returns time converted to milliseconds.
    """
    clock = (h * 3600000 + m * 60000 + s * 1000)
    return clock

past(0, 1, 1) #61000