import random


def password():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    c = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '<', '>', '?', '/', '{', '}', '[', ']']

    e = []
    for d in range(7):
        e += (random.choice(a))
    for d in range(4):
        e += (random.choice(b))
    for d in range(4):
        e += (random.choice(c))
    random.shuffle(e)
    f = ""
    for d in e:
        f += d
    return f
