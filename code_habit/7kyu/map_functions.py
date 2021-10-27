

def some_but_not_all(seq, pred): 
    """not my solution"""
    return any(map(pred, seq)) and not all(map(pred, seq))