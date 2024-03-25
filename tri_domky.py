"""
Napiš proceduru, která vykreslí domeček dané velikosti. Velikost se zadá jako argument, např:

vykresli_domecek(30)
vykresli_domecek(40)
vykresli_domecek(80)
Proceduru v programu několikrát zavolej (s různými velikostmi).
"""

from turtle import forward, left, right, exitonclick, penup, pendown, shape
from math import sqrt


def odjed_mimo(velikost_strany):
     #odjede mimo
    left(90)
    forward(4*velikost_strany)


def vypocti_sikmou(velikost_strany):
    return forward(sqrt(2)*velikost_strany/2)
      

def vykresli_domecek(velikost_strany):
    #for a in range(1):

        left(180)
        forward(velikost_strany)
        #forward(sqrt(2)*100)
        right(135)
        forward(sqrt(2)*velikost_strany)

        left(90)
        vypocti_sikmou(velikost_strany)

        left(90)
        vypocti_sikmou(velikost_strany)

        left(135)
        forward(velikost_strany)

        right(90)
        forward(velikost_strany)

        right(135)
        forward(sqrt(2)*velikost_strany)

        left(135)
        forward(velikost_strany)

        odjed_mimo(velikost_strany)
        #exitonclick()

vykresli_domecek(30)
vykresli_domecek(40)
vykresli_domecek(80)

exitonclick()