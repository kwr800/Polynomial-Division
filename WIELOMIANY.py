import math
import fractions
stop_wielomianu = int(input("podaj stopień dzielonego wielomianu: "))
a = 0
b = 1
stop_dzielnik1 = int(input("podaj stopień dzielnika wielomianu: "))
dzielnik1 = fractions.Fraction(input("podaj iloraz x^" + str(stop_dzielnik1)+" dzielnika: "))
list1 = []
list2 = [dzielnik1]
answer = []
er = stop_wielomianu
ef = stop_wielomianu + 1
et = stop_dzielnik1
ey = stop_wielomianu
em = stop_wielomianu
eu = stop_dzielnik1
for i in range(-1, stop_wielomianu):

    if ef == 0:
        a = a
    else:
        dzielona_liczba = fractions.Fraction(input("podaj iloraz x^" + str(stop_wielomianu - a) + " dzielonego wielomianu: "))
        list1.append(fractions.Fraction(dzielona_liczba))
        a = a + 1
        ef = ef - 1
    if et == 0:
        b = b
    else:
        dzielnik = fractions.Fraction(input("podaj iloraz x^" + str(stop_dzielnik1 - b) + " dzielnika: "))
        list2.append(fractions.Fraction(dzielnik))
        b = b + 1
        et = et - 1
if stop_dzielnik1 <= stop_wielomianu:
    n = 0
    h = len(list1) - len(list2)
    for u in range(0, h):
        list2.append(0)
    for lol in range(0, len(list1)):
        if ey >= stop_dzielnik1:
            z = fractions.Fraction(list1[n] / dzielnik1)
            multiplied_list = [element * z for element in list2]
            difference = []
            zip_object = zip(list1, multiplied_list)
            for list1_i, multiplied_list_i in zip_object:
                difference.append(list1_i - multiplied_list_i)
            list1 = difference
            er = er - 1
            n = n + 1
            ey = ey - 1
            answer.append(z)
            list2.insert(0, 0)
    q = 1
    for y in range(stop_dzielnik1 - 1, stop_wielomianu):
        list1.pop(0)
    answer2 = []
    for i in answer:
        if i != 0:
            if i > 0:
                answer2.append(" + ")
            else:
                answer2.append(" ")
            if i != 1:
                if i != -1:
                    answer2.append(i)
                else:
                    answer2.append("-")
            if stop_wielomianu - stop_dzielnik1 != 0:
                answer2.append("x")
                if stop_wielomianu - stop_dzielnik1 != 1:
                    answer2.append("^"+str(stop_wielomianu - stop_dzielnik1))
        stop_dzielnik1 = stop_dzielnik1 + 1
    if answer[-1] == 1 or answer[-1] == -1:
        answer2.append(1)
    if not answer2:
        answer2 = answer2
    else:
        answer2.pop(0)
    list8 = []
    for i in list1:
        if i != 0:
            if i > 0:
                list8.append(" + ")
            else:
                list8.append(" ")
            if i != 1:
                if i != -1:
                    list8.append(i)
                else:
                    list8.append("-")
            if eu - 1 != 0:
                list8.append("x")
                if eu - 1 != 1:
                    list8.append("^"+str(eu-1))
        eu = eu - 1
    if list1[-1] == 1 or list1[-1] == -1:
        list8.append(1)
    if not list8:
        list8 = list8
    else:
        list8.pop(0)
    list_5 = [num for num in list8 if isinstance(num, fractions.Fraction)]
    t = len(answer2)
    if all(v == 0 for v in list_5):
        n = n
    else:
        list8 = [str(a) for a in list8]
        str2 = ""
        for elf in list8:
            str2 += elf
        answer2.insert(t, " oraz reszta: " + str2)
    answer2 = [str(a) for a in answer2]
    str1 = ""
    for ele in answer2:
        str1 += ele
    print(str1)
else:
    answer = list1
    answer2 = []
    for i in answer:
        if i != 0:
            if i > 0:
                answer2.append(" + ")
            else:
                answer2.append(" ")
            if i != 1:
                if i != -1:
                    answer2.append(i)
                else:
                    answer2.append("-")
            if em != 0:
                answer2.append("x")
                if em != 1:
                    answer2.append("^"+str(em))
        em = em - 1
    if answer[-1] == 1 or answer[-1] == -1:
        answer2.append(1)
    answer2 = [str(a) for a in answer2]
    if not answer2:
        answer2 = answer2
    else:
        answer2.pop(0)
    str2 = ""
    for elf in answer2:
        str2 += elf
    print("0 oraz reszta: " + str(str2))
input("wciśnij ENTER aby wyjść")
