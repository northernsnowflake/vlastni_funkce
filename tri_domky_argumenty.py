"""
Máš-li ráda geometrii, můžeš zkusit dávat domečkové proceduře dva argumenty: 
šířku a výšku. Je potřeba si vzpomenout na Pythagorovu větu a na goniometrické funkce. 
Konkrétně funkci arkus tangens* from math import atan.

Pozor, funkce atan vrací výsledek v radiánech; je potřeba ho převést na stupně
 (from math import degrees).


"""
from turtle import forward, left, right, exitonclick, penup, pendown, shape
from math import sqrt, atan, degrees


def vykresli_domecek(sirka,vyska):
    #for a in range(1):
        uhlopricka = sqrt(sirka**2 + vyska**2)
        uhel_uhlopricka = degrees(atan(vyska/sirka))
        uhel_uhlopricka_maly = 90 - uhel_uhlopricka
        uhel_strecha_zakladna = degrees(atan((vyska/2)/(sirka/2)))
        uhel_strecha_spicka = 2*(180-90-uhel_strecha_zakladna)
        strecha = 180-(uhel_uhlopricka+uhel_strecha_zakladna)
        uhel_strechy_horni = (180-2*strecha)

        left(180)
        forward(sirka)
        #forward(sqrt(2)*100)

        left(uhel_uhlopricka+180)
        forward(uhlopricka)

        left(180-uhel_strecha_zakladna-uhel_uhlopricka)
        forward(uhlopricka/2)


        left(180-uhel_strecha_spicka)
        forward(uhlopricka/2)

        left(180-uhel_strecha_zakladna)
        forward(sirka)

        right(90)
        forward(vyska)

        right(180-uhel_uhlopricka_maly)
        forward(uhlopricka)

        left(180-uhel_uhlopricka_maly)
        forward(vyska)

        #odjede mimo
        left(90)
        forward(6*sirka)
        #exitonclick()


vykresli_domecek(20,20)
vykresli_domecek(20,60)
vykresli_domecek(60,20)

exitonclick()
