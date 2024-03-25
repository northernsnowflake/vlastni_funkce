"""
Napiš funkci, která bude mít jako parametr jedno číslo (n) a vypíše n řádek. Na prvním řádku bude "Bum", na druhém "Bác", na třetím "Bum", atd. Využij funkci z předchozího úkolu.

Např.

>>> vypis_bum_bac(5) 
Bum
Bác
Bum
Bác
Bum
"""

def sude_liche(cislo):
    if cislo % 2 == 0:
        #print('Sudé')
        print('Bác')
    else:
        #print('Liché')
        print('Bum')

def vypis_bum_bac(n):
    for i in range(1,n+1):
        sude_liche(i)
        """
        if i % 2 == 0:
            print('Bác') #sudé
            #return 'Bum'
        else:
            print('Bum') #liché
            #return 'Bác'
        """ 

vypis_bum_bac(5)