from random import randint
from time import time

nb_tent = 0
tps_moy = 0
nb_echecs = 0

def Doomsday(jour,mois,annee) :
    doomsday = {i:i for i in range(3,13)}
    if bissextile :
        doomsday[1] = 32
        doomsday[2] = 29
    else :
        doomsday[1] = 31
        doomsday[2] = 28
    for m in doomsday.keys() :
        if m%2 :
            if m in (3,5,7) :
                doomsday[m] += 4
            elif m in (9,11) :
                doomsday[m] -= 4
    
    doomcentury = (7 - ((annee // 100) % 4) * 2) % 7
    an = annee-annee//100*100
    if an % 2 :
        an += 11
    an //= 2
    if an % 2 :
        an += 11
    an %= 7
    doomyear = 7 - an
    ecart = (jour - doomsday[mois])
    signe = ""
    if ecart > 0 :
        signe = "+"
    ecart %= 7
    fin = (ecart + doomcentury + doomyear) % 7
    return signe,fin,ecart,doomcentury,doomyear,doomsday


tps_min = 100
tps_max = 0
liste_jours = ["mardi","mercredi","jeudi","vendredi","samedi","dimanche","lundi"]
while True :
    y = randint(1753,2150)
    m = randint(1,12)
    mois_cts = (4,6,9,11)
    bissextile = False
    if y%4 == 0 and y%400 not in (100,200,300) :
        bissextile = True
    if m == 2 :
        if bissextile :
            d = randint(1,29)
        else :
            d = randint(1,28)
    elif m in mois_cts :
        d = randint(1,30)
    else :
        d = randint(1,31)
    print("date :")
    date = "| {}/{}/{} |".format(d,m,y)
    print("-"*len(date))
    print(date)
    print("-"*len(date))
    start = time()
    int_j = input("Choisir le jour de la semaine (de 1 à 7) : ")
    chiffres = list(map(str,range(1,8)))
    while int_j not in  chiffres :
        int_j = input("saisie non valide, recommencez : ")
    int_j = int(int_j)
    end = time()
    print("temps mis : {:.1f} s\n".format(end-start))
    signe,fin,ecart,doomcentury,doomyear,doomsday = Doomsday(d,m,y)
    nb_tent += 1
    jour = liste_jours[fin].upper()
    if (fin+1)%7+1==int_j:
        print("Bien joué !")
    else :
        print("Echec...")
        nb_echecs += 1
    print("-"*(len(jour)+4))
    print("| {} |".format(jour))
    print("-"*(len(jour)+4))
    print("\nCalculs :")
    print("-"*9)
    print("doomcentury = {}".format(doomcentury))
    print("doomyear = {}".format(doomyear))
    n = (doomyear + doomcentury) % 7
    print("=> Doomsday en {} = {}".format(y,liste_jours[n]))
    print("écart par rapport au doomsday du mois ({}/{})".format(doomsday[m],m))
    if bissextile and m in (1,2) :
      print("(année bissextile)")
    print("{}{} jours".format(signe,ecart))
    tps = end-start
    tps_moy += tps
    if tps < tps_min :
        tps_min = tps
    if tps > tps_max :
        tps_max = tps
    rep = input("\nTaper q pour arreter, Entree pour continuer\n")
    if rep == "q" :
        pourcent = nb_echecs/nb_tent*100
        tps_moy = tps_moy/nb_tent
        print("\nSTATS :")
        print("-"*7)
        print("nombre de tentatives : {}".format(nb_tent))
        print("pourcentage d'erreurs : {:.0f}%".format(pourcent))
        print("temps moyen : {:.1f} s".format(tps_moy))
        print("temps max : {:.1f} s".format(tps_max))
        print("temps min : {:.1f} s".format(tps_min))
        break
