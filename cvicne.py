#a rock-paper-scissors game
from random import randint, choice



#input je takovej ten prompt
comp = ""
hrac = ""

games_g = 0

def computer_choice():
    selection = randint(1,3)
    if selection == 1:
        return "kamen"
    elif selection == 2:
        return "nuzky"
    else:
        return "papir"
def weighted_computer_choice():
    posibru = ["kamen", "nuzky", "papir"]
    selection = posibru + [choice(posibru)]
    current_selection = choice(selection)
    return current_selection
    #for i in selection:
        #print(i)

#weighted_computer_choice()

def players_choice():
    vstup = input("kamen, nuzky nebo papir? ")
    if vstup == "kamen"or vstup == "nuzky" or vstup == "papir":
        return vstup
    else:
        vstup = input("kamen, nuzky nebo papir? ")
    #tady potrebuju nejaky while cyklus na dotazovani dokud hrac nezada spravne zneni volby
#players_choice()

def players_while_choice():
    vstup = input("kamen, nuzky nebo papir? ")
    okay = ["kamen","nuzky","papir"]
    while vstup not in okay:
        print("Neplatna volba! Vyber si poradne!")
        vstup = input("kamen, nuzky nebo papir? ")
    else:
        return vstup
#print(players_while_choice())

def win():
    print(comp)
    print("vyhrals!")

def los():
    print(comp)
    print("prohrals!")

def rem():
    print(comp)
    print("remiza")

def znovu():
    zase = input("chces hrat znovu? ")
    ouk = ["jo", "ne"]
    while zase not in ouk:
        print("Neplatna volba! Vyber si poradne!Napis 'jo' nebo 'ne'.")
        zase = input("chces hrat znovu? ")
    else:
        if zase == "jo":
            print()
            knp()

def game_stats():
    global games
    global comp_wins
    global your_wins
    global comp_win_rate
    global your_win_rate
    comp_win_rate = 100*comp_wins/games
    your_win_rate = 100*your_wins/games

def jmeno_vyteze():
    global comp_wins
    global your_wins
    global winners_name

    if comp_wins > your_wins:
        winners_name = "comp"
    elif your_wins > comp_wins:
        winners_name = "TY!"
    else:
        winners_name = "nikdo, je to remiza"

def retez_vytezstvi():
    global comp_win_streak_max
    global your_win_streak_max
    global comp_win_streak_cur
    global your_win_streak_cur
    if comp_win_streak_cur > comp_win_streak_max:
        comp_win_streak_max = comp_win_streak_cur
    if your_win_streak_cur > your_win_streak_max:
        your_win_streak_max = your_win_streak_cur


games = 0
comp_wins = 0
your_wins = 0
winners_name = ""
comp_win_rate = 0
your_win_rate = 0
comp_win_streak_max = 0
your_win_streak_max = 0
comp_win_streak_cur = 0
your_win_streak_cur = 0

def knp():
    comp = weighted_computer_choice()
    hrac = players_while_choice()

    global games
    global comp_wins
    global your_wins
    global winners_name
    global comp_win_rate
    global your_win_rate
    global comp_win_streak_max
    global your_win_streak_max
    global comp_win_streak_cur
    global your_win_streak_cur

    print("comp vybral: ", comp)
    if comp == "kamen":
        if hrac == "kamen":
            rem()
            comp_win_streak_cur = 0
            your_win_streak_cur = 0
        elif hrac == "nuzky":
            los()
            comp_wins +=1
            your_win_streak_cur = 0
            comp_win_streak_cur += 1
        else:
            win()
            your_wins +=1
            comp_win_streak_cur = 0
            your_win_streak_cur += 1
    elif comp == "nuzky":
        if hrac == "kamen":
            win()
            your_wins +=1
            comp_win_streak_cur = 0
            your_win_streak_cur += 1
        elif hrac == "nuzky":
            rem()
            comp_win_streak_cur = 0
            your_win_streak_cur = 0
        else:
            los()
            comp_wins += 1
            your_win_streak_cur = 0
            comp_win_streak_cur += 1
    else:
        #comp == "papir"
        if hrac == "kamen":
            los()
            comp_wins += 1
            your_win_streak_cur = 0
            comp_win_streak_cur += 1
        elif hrac == "nuzky":
            win()
            your_wins +=1
            comp_win_streak_cur = 0
            your_win_streak_cur += 1
        else:
            rem()
            comp_win_streak_cur = 0
            your_win_streak_cur = 0

    games+=1
    game_stats()
    jmeno_vyteze()
    retez_vytezstvi()
    print("Dosavadni pocet her: ",games)
    print("Comp dosud vyhral tolikrat: ", comp_wins)
    print("Pocet tvych dosavadnich vyher: ", your_wins)
    print("Procentni uspesnost compa: ","{0:.2f}%".format(comp_win_rate))
    print("Tvoje procentualni uspesnost: ","{0:.2f}%".format(your_win_rate))
    print("Vitezem je: ", winners_name)
    print("Nejdelsi vyherni posloupnost compa: ",comp_win_streak_max)
    print("Tvoje nejdelsi vyherni posloupnost: ",your_win_streak_max)
    znovu()

knp()


