import random
def create_random_array(n):
    array = []
    for i in range(n):
        array.append(random.randint(0,2**19))
    return array

def create_ascending(n):
    array = []
    value = 0
    for i in range(n):
        value += i+random.randint(0,10000)
        array.append(value)
    return array


def create_descending(n):
    array = []
    for i in range(n):
        array.append(random.randint(0,2**19))
    array.sort(reverse = True)
    return array


def create_123(n):
    array = []
    for i in range(n):
        array.append(random.randint(1,3))
    return array