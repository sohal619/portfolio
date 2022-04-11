import random

r = '''rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

p = '''Paper
    _______
---'    ____)_____
           _______)
          _________)
         ________)
---.__________)'''

s = '''scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

gh = [r, p, s]
a = int(input("rules-> press 1 for rock\n        press 2 for paper\n        press 3 for scissor\n"))

print(gh[a-1])

b = random.randint(1, 3)

print("\n\ncomputer chose:", gh[b-1])

if a == b:
    print("DRAW")
elif a == 1 and b == 2:
    print("you lose!!")
elif a == 1 and b == 3:
    print("you win!!")
elif a == 2 and b == 1:
    print("you win!!")
elif a == 2 and b == 3:
    print("you lose!!")
elif a == 3 and b == 1:
    print("you lose!!")
elif a == 3 and b == 2:
    print("you win!!")
