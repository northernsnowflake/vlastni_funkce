"""
Napiš funkci, která bude mít jako parametr jedno 
číslo a vrátí "Bum", je-li toto číslo liché,
a "Bác", je-li toto číslo sudé.
"""

def sude_liche(cislo):
    if cislo % 2 == 0:
        #print('Sudé')
        return 'Bác'
    else:
        #print('Liché')
        return 'Bum'


print(sude_liche(11))
