def warn_the_sheep(queue):
    """
    My solution
    Warn the sheep in front of the wolf that it is about to be eaten.
    Remember that you are standing at the front of the queue which is at the end of the array:
    If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep".
    Otherwise, return "Oi! Sheep number [N]! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
    :param queue: array ['sheep', 'wolf', 'sheep']
    :return:
    # warn_the_sheep(['sheep', 'wolf', 'sheep']) # 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
    # warn_the_sheep(['sheep', 'sheep', 'wolf']) # 'Pls go away and stop eating my sheep'
    """
    reverse_array = queue[::-1]
    if queue[-1] == 'wolf':
        print('Pls go away and stop eating my sheep')
        return 'Pls go away and stop eating my sheep'
    else:
        for x in range(len(reverse_array)):
            if reverse_array[x] == 'wolf':
                print("Oi! Sheep number {}! You are about to be eaten by a wolf!".format(x))
                return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(x)


def warn_the_sheep(queue):
    """
    Best solution form codewars
    """
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


def warn_the_sheep(queue):
    """
    Other solution form codewars
    """
    queue.reverse()
    return 'Pls go away and stop eating my sheep' if queue[0] == 'wolf' else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))


# warn_the_sheep(['sheep', 'wolf', 'sheep']) # 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
# warn_the_sheep(['sheep', 'sheep', 'wolf']) # 'Pls go away and stop eating my sheep'