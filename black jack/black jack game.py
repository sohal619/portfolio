import random
from logo import logo
result = {}


def bj():
    number = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = []
    card1 = []

    def user_card():
        for z in range(2):
            y = random.choice(number)
            card.append(y)
            if sum(card) == 22:
                card[z] -= 10
            elif sum(card) == 21:
                return f"   your final hand: {card}, final score: {sum(card)}"
        return f"   your cards: {card}, current score: {sum(card)}"

    def m_card():
        j = True
        while j:
            x = random.choice(number)
            card1.append(x)
            if x == 11:
                if sum(card1) == 22:
                    card1[len(card1) - 1] -= 10
            if sum(card1) >= 17:
                j = False
        return f"   computer's first card: {card1[0]}"

    b = user_card()
    c = m_card()
    if sum(card) == 21 and sum(card1) == 21:
        result[1] = b
        result[2] = f"   computer's final hand: {card1}, final score: {sum(card1)}"
        if len(card1) == 2:
            result[3] = "   Draw🙃!!"
            return result
        else:
            result[3] = "   you win😎!!"
            return result

    if sum(card) == 21:
        result[1] = b
        result[2] = f"   computer's final hand: {card1}, final score: {sum(card1)}"
        result[3] = "   you win😎!!!"
        return result

    print(b)
    print(c)
    s = True
    while s:
        d = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if d == "y":
            w = random.choice(number)
            card.append(w)
            if w == 11:
                if sum(card) > 21:
                    card[len(card) - 1] -= 10
            if sum(card) == 21:
                result[1] = f"   your final hand: {card}, final score: {sum(card)}"
                result[2] = f"   computer's final hand: {card1}, final score: {sum(card1)}"
                if sum(card1) == 21:
                    if len(card) == len(card1):
                        result[3] = "Draw🙃!!"
                        return result
                    if len(card) < len(card1):
                        result[3] = "you win😎!!"
                        return result
                    if len(card) > len(card1):
                        result[3] = "you lose😤!!"
                        return result
                else:
                    result[3] = "   you win😎!!"
                return result
            if sum(card) > 21:
                if sum(card1) > 21:
                    result[1] = f"   your final hand: {card}, final score: {sum(card)}"
                    result[2] = f"   computer's final hand: {card1}, final score: {sum(card1)}"
                    result[3] = "   Draw🙃!!"
                    return result
            if sum(card) > 21:
                result[1] = f"   your final hand: {card}, final score: {sum(card)}"
                result[2] = f"   computer's final hand: {card1}, final score: {sum(card1)}"
                result[3] = "   you lose😤!!"
                return result
            else:
                print(f"   your cards: {card}, current score: {sum(card)}")
                print(c)
        else:
            result[1] = f"   your final hand: {card}, final score: {sum(card)}"
            result[2] = f"   computer's final hand: {card1}, final score: {sum(card1)}"
            if sum(card) > 21:
                if sum(card1) > 21:
                    result[3] = "   Draw🙃!!"
                    return result
            if sum(card1) > 21:
                result[3] = "   you win😎!!"
                return result
            if sum(card) < sum(card1):
                result[3] = "   you lose😤!!"
                return result
            if sum(card) == sum(card1):
                result[3] = "   Draw🙃!!"
                return result
            else:
                result[3] = "   you win😎!!"
                return result


p = True
while p:
    a = input("Do you want to play a game of blackjack? Type 'y' or ''n':").lower()
    if a == "y":
        print("\n" * 50)
        print(logo)
        bj()
        for m in result:
            print(result[m])
    else:
        print("   Good bye🤔!!")
        p = False
