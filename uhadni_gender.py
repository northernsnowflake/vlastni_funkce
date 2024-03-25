"""
Napiš funkci, která jako argument bere příjmení uživatelky/uživatele a zkusí podle něj uhodnout její/jeho pohlaví. To vrátí jako řetězec.

Funkci v programu několikrát zavolej (s různými příjmeními – ty můžeš zadat přímo do kódu při volání funkcí). Výsledky vypiš.

(Pohlaví není možné určit přesně – stačí zvládnout ta nejčastější česká příjmení.)

Program, který tohle dělá, už máš – úkol spočívá v tom, že z něj správný kousek „zabalíš“ do funkce.
"""

def rozhodni(jmeno):
    if jmeno[-1] == 'á':
        #print('žena')
        return 'žena'
    else:
        #print('muž')
        return 'muž'

#jmeno = input("Tvoje příjmení je: ")
print(rozhodni("Janák"))
print(rozhodni("Trnož"))
print(rozhodni("Láskorádová"))
print(rozhodni("Láskorád"))
