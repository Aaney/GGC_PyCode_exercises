#unfinished tic-tac-toe game
sloupce = [1,2,3]
radky = ['A','B','C']
male_pole = {radek: {sloupec: '.' for sloupec in sloupce} for radek in radky}
#s = 'B'
#print(male_pole[s][2])
def vytiskni_male_pole(pole):
    #tady je asi potreba nejaky vypis cisel sloupcu
    print("   1   2   3")#lame!!!
    for radek, sloupec in pole.items():
        print(radek, end='  ')
        for sloupec, bunka in sloupec.items():
            if sloupec == 3:
                print(bunka, end='')
            else:
                print(bunka, end=' | ')
        print()
#vytiskni_male_pole(male_pole)

def ziskej_policko(pismeno_s_cislem):
    pismeno = pismeno_s_cislem[0]
    cislo = int(pismeno_s_cislem[1])
    return pismeno, cislo

def validace_obsazenosti_policka(pouzivane_pole, pism, cisl):
    if pouzivane_pole[pism][cisl] == '.':
        return True
    else:
        return False

def validace_zpisovaneho_znaku():
    #TODO
    pass

def zapis_do_pole(nejake_pole,znacka):
    policko = zadej_policko_prompt()
    pis, cis = ziskej_policko(policko)
    #znacka = "X"
    if validace_obsazenosti_policka(nejake_pole,pis,cis):
        nejake_pole[pis][cis] = znacka
        vytiskni_male_pole(nejake_pole)
    else:
        print('Pole je obsazene')
        zapis_do_pole(nejake_pole, znacka)

def zadej_policko_prompt():
    policko = input("Zadej policko v rozmezi A1-C3: ")
    return policko

def vyhodnot_vyhru(takove_pole, hrac):
    diaga1 = takove_pole['A'][1] == takove_pole['B'][2] == takove_pole['C'][3] != '.'
    diaga3 = takove_pole['A'][3] == takove_pole['B'][2] == takove_pole['C'][1] != '.'
    radeka = takove_pole['A'][1] == takove_pole['A'][2] == takove_pole['A'][3] != '.'
    radekb = takove_pole['B'][1] == takove_pole['B'][2] == takove_pole['B'][3] != '.'
    radekc = takove_pole['C'][1] == takove_pole['C'][2] == takove_pole['C'][3] != '.'
    sloup1 = takove_pole['A'][1] == takove_pole['B'][1] == takove_pole['C'][1] != '.'
    sloup2 = takove_pole['A'][2] == takove_pole['B'][2] == takove_pole['C'][2] != '.'
    sloup3 = takove_pole['A'][3] == takove_pole['B'][3] == takove_pole['C'][3] != '.'
    neniva = '.' in male_pole['A'].values()
    nenivb = '.' in male_pole['B'].values()
    nenivc = '.' in male_pole['C'].values()
    misto = neniva == nenivb == nenivc
    if diaga1:
        print('Vyhrava hrac: ', hrac)
    elif diaga3:
        print('Vyhrava hrac: ', hrac)
    elif radekb:
        print('Vyhrava hrac: ', hrac)
    elif radekc:
        print('Vyhrava hrac: ', hrac)
    elif sloup1:
        print('Vyhrava hrac: ', hrac)
    elif sloup2:
        print('Vyhrava hrac: ', hrac)
    elif sloup3:
        print('Vyhrava hrac: ', hrac)
    elif misto == False:
        print('Je to remiza')
        return 0
    else:
        print('zatim nikdo')
        return 1

def jmena_hracu_prompt():
    jmeno1 = input('Jmeno prvnho hrace X : ')
    jmeno2 = input('Jmeno druheho hrace O : ')
    return jmeno1, jmeno2

def hrej(herni_pole, hrac):
    pass

def hrat_piskvorky(takove_pole):
    vytiskni_male_pole(takove_pole)
    konec = 0
    hrac = 1

    while konec == 0:
        if hrac % 2 == 1:
            zapis_do_pole(takove_pole, 'X')
        else:
            zapis_do_pole(takove_pole, 'O')

        diaga1 = takove_pole['A'][1] == takove_pole['B'][2] == takove_pole['C'][3] != '.'
        diaga3 = takove_pole['A'][3] == takove_pole['B'][2] == takove_pole['C'][1] != '.'
        radeka = takove_pole['A'][1] == takove_pole['A'][2] == takove_pole['A'][3] != '.'
        radekb = takove_pole['B'][1] == takove_pole['B'][2] == takove_pole['B'][3] != '.'
        radekc = takove_pole['C'][1] == takove_pole['C'][2] == takove_pole['C'][3] != '.'
        sloup1 = takove_pole['A'][1] == takove_pole['B'][1] == takove_pole['C'][1] != '.'
        sloup2 = takove_pole['A'][2] == takove_pole['B'][2] == takove_pole['C'][2] != '.'
        sloup3 = takove_pole['A'][3] == takove_pole['B'][3] == takove_pole['C'][3] != '.'
        neniva = '.' in male_pole['A'].values()
        nenivb = '.' in male_pole['B'].values()
        nenivc = '.' in male_pole['C'].values()
        misto = neniva == nenivb == nenivc
        if diaga1:
            print('Vyhrava hrac: ', hrac)
        elif diaga3:
            print('Vyhrava hrac: ', hrac)
        elif radekb:
            print('Vyhrava hrac: ', hrac)
        elif radekc:
            print('Vyhrava hrac: ', hrac)
        elif sloup1:
            print('Vyhrava hrac: ', hrac)
        elif sloup2:
            print('Vyhrava hrac: ', hrac)
        elif sloup3:
            print('Vyhrava hrac: ', hrac)
        elif misto == False:
            print('Je to remiza')
            konec = 1
        else:
            print('zatim nikdo')
            konec = 0
            hrac += 1
hrat_piskvorky(male_pole)
#hrat_piskvorky(male_pole)

#male_pole['A'][1] = '.'
#male_pole['B'][2] = '.'
#male_pole['C'][1] = 'x'
#diaga1 = male_pole['A'][1] == male_pole['B'][2] == male_pole['C'][3] != '.'
#print(diaga1)
#vytiskni_male_pole(male_pole)



