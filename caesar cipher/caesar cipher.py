import time


def caesar(t, s, direct):
    d = ""
    if direct == "encode":
        for a in t:
            b = alphabets.index(a)
            d += alphabets[b + s]
            if a not in alphabets:
                d += a
        print(f"the encoded message:{d}")
    if direct == "decode":
        for a in t:
            b = alphabets.index(a)
            d += alphabets[b - s]
            if a not in alphabets:
                d += a
        print(f"the decoded message:{d}")


logo = ('''
                                                                  
                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
                                                                  
                                                                  
                                                            
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             

''')


alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
             "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a", "b", "c", "d", "e", "f", "g", "h",
             "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
             "z", " "]

rules = "\n\n\n\n\nRules-\n1. Don't use any kind of symbols while encode." \
        "\n2. only those messages can be decode that is encode by this programme." \
        "\n3. Shift number must be less than 10." \
        "\n4. You have to remember shift code while encoding and use the same shift code while decoding.\n\n"


print(logo)
time.sleep(3)

que = True
while que:
    print(rules)
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt->\n")
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number->\n"))
    while shift > 10:
        shift -= 1
    caesar(t=text, s=shift, direct=direction)
    o = input("Type 'yes' if you want to run caesar cipher again, otherwise Type 'no'->\n")
    if o == "yes":
        que = True
    else:
        print("\nGood bye!!")
        que = False
