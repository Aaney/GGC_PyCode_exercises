#callendar creator - input is month and day of the week
nazev_delka = {"Leden": 31,
               "Unor": 28,
               "Brezen": 31,
               "Duben": 30,
               "Kveten": 31,
               "Cerven": 30,
               "Cervenec": 31,
               "Srpen": 31,
               "Zari": 30,
               "Rijen": 31,
               "Listopad": 30,
               "Prosinec": 31}
poradi_delka = {1: 31,
               2: 28,
               3: 31,
               4: 30,
               5: 31,
               6: 30,
               7: 31,
               8: 31,
               9: 30,
               10: 31,
               11: 30,
               12: 31}
poradi_nazev = {1: "Leden",
               2: "Unor",
               3: "Brezen",
               4: "Duben",
               5: "Kveten",
               6: "Cerven",
               7: "Cervenec",
               8: "Srpen",
               9: "Zari",
               10: "Rijen",
               11: "Listopad",
               12: "Prosinec"}

def obdelnik():
    radky = 5
    sloupce = 7
    for i in range(radky):
        print ()
        for j in range(1, sloupce+1):
            print((j+i*sloupce), end=" ")
#obdelnik()

def jeden_mesic_osklivy_jednocifrovy(delka):
    radky = 5
    sloupce = 7
    for i in range(radky):
        print()
        for j in range(1, sloupce + 1):
            den = j + i * sloupce
            if den <= delka:
                print((den), end=" ")

def jeden_mesic_osklivy_dvoucifrovy(delka):
    radky = 5
    sloupce = 7
    for i in range(radky):
        print()
        for j in range(1, sloupce + 1):
            den = j + i * sloupce
            if den <= delka:
                print("{0:02d}".format(den), end=" ")

def jeden_mesic_osklivy_dvoucifrovy_tyden(delka):
    radky = 5
    sloupce = 7
    tolikaty_den = 1
    print("PO UT ST CT PA SO NE",end="")
    #for i in range(radky):
    #    print()
        #print(tolikaty_den*"   ", end="")

    #for i in range(radky):
    print()
    # print(tolikaty_den*"   ", end="")
    print((tolikaty_den-1) * "   ", end="")
    for k in range(1, sloupce + 2 - tolikaty_den):


        if k <= delka:
            print("{0:02d}".format(k), end=" ")

    for i in range(radky):
        print()
        # print(tolikaty_den*"   ", end="")
        for j in range(1, sloupce + 1):

            den = j + i * sloupce + 8 - tolikaty_den
            if den <= delka:
                print("{0:02d}".format(den), end=" ")

def jeden_mesic_hezky_dvoucifrovy_tyden(delka, nty_den_v_tydnu):
    radky = 5
    sloupce = 7

    print("PO UT ST CT PA SO NE",end="")
    #for i in range(radky):
    #    print()
        #print(tolikaty_den*"   ", end="")

    #for i in range(radky):
    print()
    # print(tolikaty_den*"   ", end="")
    print((nty_den_v_tydnu-1) * "   ", end="")
    for k in range(1, sloupce + 2 - nty_den_v_tydnu):


        if k <= delka:
            print("{0:02d}".format(k), end=" ")

    for i in range(radky):
        print()
        # print(tolikaty_den*"   ", end="")
        for j in range(1, sloupce + 1):

            den = j + i * sloupce + 8 - nty_den_v_tydnu
            if den <= delka:
                print("{0:02d}".format(den), end=" ")

def vytiskni_kalendar():
    global nazev_delka
    for key, value in nazev_delka.items():
        print(key)
        jeden_mesic_hezky_dvoucifrovy_tyden(value,4)
        print()
        print("__ __ __ __ __ __ __")
        print()

#vytiskni_kalendar()

def pocitadlo_posunuti(old_day, old_month_value):
    new_day = (old_day+(old_month_value%7))
    if new_day>7:
        new_day = new_day%7
    return new_day
#print(pocitadlo_posunuti(4, 31))

def vytiskni_kalendar_dle_dne_a_mesice(mesic, nty_den_v_tydnu):
    global poradi_delka
    global poradi_nazev
    posunuti = nty_den_v_tydnu
    for key, value in poradi_delka.items():

        if key+mesic-1<=12:
            print(poradi_nazev[(key+mesic-1)])
            jeden_mesic_hezky_dvoucifrovy_tyden(poradi_delka[(key+mesic-1)],posunuti)
            posunuti = pocitadlo_posunuti(posunuti,poradi_delka[(key+mesic-1)])
            print()
            print("__ __ __ __ __ __ __")
            print()
vytiskni_kalendar_dle_dne_a_mesice(4,6)

def vytiskni_kalendar_s_prestupnymi_roky(mesic, nty_den_v_tydnu, rok):
    #todo celou funkci.. zatim to je jen kopie te vytiskni_kalendar_dle_dne_a_mesice(mesic, nty_den_v_tydnu)
    global poradi_delka
    global poradi_nazev
    posunuti = nty_den_v_tydnu
    for key, value in poradi_delka.items():

        if key+mesic-1<=12:
            print(poradi_nazev[(key+mesic-1)])
            jeden_mesic_hezky_dvoucifrovy_tyden(poradi_delka[(key+mesic-1)],posunuti)
            posunuti = pocitadlo_posunuti(posunuti,poradi_delka[(key+mesic-1)])
            print()
            print("__ __ __ __ __ __ __")
            print()