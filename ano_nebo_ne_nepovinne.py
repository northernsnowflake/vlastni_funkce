"""
Změň funkci ano_nebo_ne tak, aby se místo ano se dalo použít i a, místo ne i n a aby se nebral ohled na velikost písmen a mezery před/za odpovědí.

Odpovědím jako možná nebo no tak určitě by počítač dál neměl rozumět.

"""
souhlas = ['ano','a','Ano','A',' ano',' a',' Ano',' A','ano ','a ','Ano ','A ','     ano     ','aNo','aNO','anO','ANO']
nesouhlas = ['ne','Ne','N','n','ne',' Ne',' N',' n','ne ','Ne ','N ','n ','nE','NE','     ne     ','nE']

def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    odpoved = input(otazka)
    for prvek_s in souhlas:
        if odpoved == prvek_s:
            return True
    for prvek_n in nesouhlas:
        if odpoved == prvek_n:
            return False

navratova_hodnota = ano_nebo_ne('Chceš si zahrát hru? ')

if navratova_hodnota == True: 
    print('OK! Ale napřed si ji musíš naprogramovat.')
elif navratova_hodnota == False:
    print('Škoda.')
else:
    print('Nerozumím! Odpověz "ano" nebo "ne".')

