import os, time
print('Insert equation, Spaces between characters')
equa = str(input(': '))
equa.split(" ")
# print(equa)
run = 0
for slot in equa:
    str(slot)
    try:
        if slot == "+":
            ans1 = float(equa[run-2])
            ans2 = float(equa[run+2])
            print(ans1+ans2)
        if slot == "-":
            ans1 = float(equa[run-2])
            ans2 = float(equa[run+2])
            print(ans1-ans2)
        if slot == "*":
            ans1 = float(equa[run-2])
            ans2 = float(equa[run+2])
            print(ans1*ans2)
        if slot == "/":
            ans1 = float(equa[run-2])
            ans2 = float(equa[run+2])
            print(ans1/ans2)
    except IndexError:
        print('Invaild Syntax')

        
    run += 1
