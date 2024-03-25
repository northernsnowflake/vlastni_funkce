

"""
Vytvoř funkci pocet_vterin, která bude mít dva argumenty: čas v minutách a čas ve vteřinách.
A bude vracet celkový počet vteřin."""

def pocet_vterin(t_minuty,t_vteriny):
    a = (t_minuty * 60) + t_vteriny
    #print(a)
    return a


print(pocet_vterin(2,30))