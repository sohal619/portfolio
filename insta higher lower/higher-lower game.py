import random
from art import logo, vs
from game_data import data


def data_compare():
    b = data[a]['name']
    c = data[a]['description']
    d = data[a]['country']
    f = data[a]['follower_count']
    e['a'] = b+", "+c+", "+d+"."
    e['b'] = f
    return e


def data_against():
    if z != a:
        x = data[z]['name']
        w = data[z]['description']
        v = data[z]['country']
        u = data[z]['follower_count']
        t['a'] = x + ", " + w + ", " + v + "."
        t['b'] = u
        return t
    else:
        data_against()


e = {}
t = {}
g = 0
h = True
z = random.randrange(0, 49)
a = random.randrange(0, 49)
data_compare()
data_against()
A = e['b']
B = t['b']
while h:
    if g != 0:
        print("\n"*30)
    print(logo)
    if g != 0:
        print(f"You're right! Current score: {g}")
        e['a'] = t['a']
        A = B
        z = random.randrange(0, 49)
        data_against()
        B = t['b']
    print(f"Compare A: {e['a']}")
    print(vs)
    print(f"Against B: {t['a']}")
    i = input("who has more followers on instagram? Type 'A' or 'B':").upper()
    if i == "A":
        if A > B:
            g += 1
        else:
            h = False
            print("\n"*30)
            print(f"Sorry, that's wrong. Final score: {g}")

    elif i == "B":
        if B > A:
            g += 1
        else:
            h = False
            print("\n"*30)
            print(f"Sorry, that's wrong. Final score: {g}")
