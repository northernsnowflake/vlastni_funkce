"""
Další vylepšení hry sibenice:

Použij funkci zamen (místo toho, aby byl příslušný kód přímo v hlavním programu).
Po vypsání počtu neúspěšných pokusů vypiš obrázek. Funkci, která vrátí obrázek podle počtu pokusů, si můžeš zkopírovat z Gistu
Zabal hru do funkce a po skončení dej hráči možnost hru opakovat

"""
import random
slovo = random.choice(['čokoláda','okolo'])
stav = '_'*len(slovo)
neuspesne = 0
hadane_pozice = []


def obrazek(level):
    if level == 0:
        return """
        ~~~~~~~
        """
    elif level == 1:
        return """
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 2:
        return """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 3:
        return """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 4:
        return """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        """
    elif level == 5:
        return """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        """
    elif level == 6:
        return """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        """
    elif level == 7:
        return """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        """
    elif level == 8:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        """
    else:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~
        """


def hra(stav,slovo,neuspesne):
    s = '[@_!#$%^&*()<>?/\|}{~:"]§'
    while True:
        pismeno = input("Zadej písmeno:")
        if pismeno in s:
            print('Neakceptovatelný znak')
            continue
        if len(pismeno) != 1 or len(pismeno) == 0 or pismeno == ' ' or pismeno == '':
            print('Nezadal jsi buď žádný znak nebo víc než jeden znak')
            continue
        if pismeno in slovo:
            pozice = slovo.find(pismeno) #když nebude výskyt, find vrátí -1
            while pozice != -1: # znamení že je tady alespoň jeden výskyt písmena ve slově
            # tj. dokud je tam hodnota (i když by vícekrát)
                if pozice not in hadane_pozice: #jestli ještě není v seznamu
                    hadane_pozice.append(pozice) #print(hadane_pozice)
                    stav = zamen(pismeno,stav,pozice)
                pozice = slovo.find(pismeno, pozice + 1) # té první už si nevšímej - hustýýý řádek
            if '_' not in stav:
                print('Gratuluji')
                break
        elif pismeno not in slovo:
            neuspesne = neuspesne + 1
            print(f'neuspesne {neuspesne}')
            print(obrazek(neuspesne))
            continue
        elif pismeno == '':
            neuspesne = neuspesne + 1
            print(f'neuspesne {neuspesne}')
            print(obrazek(neuspesne))
            continue
        elif neuspesne > 9:
            print('Hráč bohužel prohrál')
            break
        #print(hadane_pozice)
        print(f'neuspesne {neuspesne}')
        print(obrazek(neuspesne))
        print(stav)
    return obrazek(neuspesne), stav



def zamen(pismeno,stav,pozice):
    stav = stav[:pozice] + pismeno + stav[pozice + 1:]
    return stav


while True:
    #slovo = random.choice(['trávník','stromek','stavení'])
    hra(stav,slovo,neuspesne)
    opakovani = input('Chceš hru opakovat?:a/n')
    if opakovani != 'a':
        break