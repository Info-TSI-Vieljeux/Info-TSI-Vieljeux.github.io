plateau = [str(i) for i in range(1,10)]
nb_plateaux = 0

def affichage(plateau):
    ligne = '-'*7+'\n'
    s = ligne
    for i in range(2,-1,-1):
        for j in range(3*i,3*i+3):
            s += '|'+ plateau[j]
        s += '|'
        s += '\n'
        s += ligne
    print(s)

typeIA = input("\nVoulez-vous jouer contre l'IA parfaite (1)\nou l'IA avec heuristique (2) ?\nChoisir 1 ou 2 : ")
while typeIA not in ("1","2"):
    print(typeIA+" n'est pas un choix proposé")
    typeIA = input("\nVoulez-vous jouer contre l'IA parfaite (1)\nou l'IA avec heuristique (2) ?\nChoisir 1 ou 2 : ")

nb_niv = 1
if typeIA == '2':
    nb_niv = input("\nChoisir le nombre de coups d'avance de l'IA (1,2 ou 3) : ")
    while nb_niv not in ("1","2","3"):
        print(nb_niv+" n'est pas un choix proposé")
        nb_niv = input("\nChoisir le nombre de coups d'avance de l'IA (1,2 ou 3) : ")
    nb_niv = int(nb_niv)

choix = input("\nVoulez-vous jouer en premier ? O ou N : ")
while choix not in ("O","N","o","n"):
    print(choix,"n'est pas un choix proposé") 
    choix = input("\nVoulez-vous jouer en premier ? O ou N : ")

if typeIA == "1" and choix in ("n","N"):
    print("\nLe premier coup de l'IA peut prendre un peu de temps...")

print("\nl'IA a les 'O'\n")
IA = 'O'
humain = 'X'

def cases_restantes(plateau):
    reste = []
    for i in range(9):
        if plateau[i] not in ('X','O'):
            reste.append(plateau[i])
    return reste

def tour_humain(plateau):
    reste = cases_restantes(plateau)
    choix = input("Choisir un numéo sur le plateau : ")
    while choix not in reste:
        print("pas une case disponible")
        choix = input("Choisir un numéo sur le plateau : ")
    plateau[int(choix)-1] = 'X'
    affichage(plateau)

def victoire(plateau,joueur):
    V = False
    for i in range(3):
        V = V or plateau[3*i] == plateau[3*i+1] == plateau[3*i+2] == joueur
    for i in range(3):
        V = V or plateau[i] == plateau[i+3] == plateau[i+6] == joueur
    V = V or plateau[0] == plateau[4] == plateau[8] == joueur or plateau[6] == plateau[4] == plateau[2] == joueur
    return V

def fini(plateau,joueur):
    if victoire(plateau,joueur):
        print("Victoire de {joueur} !")
        return True
    elif (len(cases_restantes(plateau)) == 0):
        print("Match nul !")
        return True
    else:
        return False

def heuristique(arene):
    score = 0
    for i in range(3):
        colonne = [arene[i+3*k] for k in range(3)]
        if 'X' not in colonne:
            score += 1
        if 'O' not in colonne:
            score -= 1
        ligne = [arene[i*3+k] for k in range(3)]
        if 'X' not in ligne:
            score += 1
        if 'O' not in ligne:
            score -= 1
    diagonale1 = [arene[4*i] for i in range(3)]
    diagonale2 = [arene[2+2*i] for i in range(3)]
    if 'X' not in diagonale1:
        score += 1
    if 'O' not in diagonale1:
        score -= 1
    if 'X' not in diagonale2:
        score += 1
    if 'O' not in diagonale2:
        score -= 1
    return score

def minimax(plateau,tourIA,niveau):
    global nb_plateaux
    reste = cases_restantes(plateau)
    if victoire(plateau,'O'):
        return float('inf')
    elif victoire(plateau,'X'):
        return float('-inf')
    elif reste == []:
        return 0
    elif niveau == 0 and typeIA == '2':
        return heuristique(plateau)
    scores = []
    for e in reste:
        nb_plateaux += 1
        if tourIA:
            plateau[int(e)-1] = 'O'
        else:
            plateau[int(e)-1] = 'X'
        scores.append(minimax(plateau,not tourIA,niveau-1))
        plateau[int(e)-1] = e
    if tourIA:
        return max(scores)
    else:
        return min(scores)

def tour_IA(plateau):
    reste = cases_restantes(plateau)
    meilleurscore = float('-inf')
    meilleurcoup = None
    for cp in reste:
        plateau[int(cp)-1] = 'O'
        score = minimax(plateau,False,nb_niv)
        plateau[int(cp)-1] = cp
        if score > meilleurscore:
            meilleurscore = score
            meilleurcoup = cp
    plateau[int(meilleurcoup)-1] = 'O'
    affichage(plateau)

if choix in ("O","o"):
    affichage(plateau)
    tour_humain(plateau)

while True:
    input("Au tour de l'IA (appuyez sur Entrée) ")
    tour_IA(plateau)
    if fini(plateau,IA):
        break
    tour_humain(plateau)
    if fini(plateau,humain):
        break

print(f"\nL'IA a inspecté {nb_plateaux} plateaux pendant cette partie.")