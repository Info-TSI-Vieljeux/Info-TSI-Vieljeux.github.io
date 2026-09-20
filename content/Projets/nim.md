---
title: "Nim"
date: 2021-03-06T14:23:56+01:00
weight : 6
draft: false
---

# Jeu de Nim

Présentation du jeu et de l'algorithme de Bouton :

{{<youtube 2jahbr5wMHk>}}

<br>

### Mission : 

Coder une IA qui joue un coup gagnant lorsqu'elle est est en position gagnante (en suivant l'algorithme de Bouton) et qui joue aléatoirement si elle est sur une position perdante.

[**Jouer contre une telle IA**.](https://presentationssite.github.io/info/nim/#/)

<br><br>

---


### Un code solution possible :

```python
# exemple de plateau : [1,3,5,7]
from random import randint

def tourIA(plateau):
  nimSomme = 0
  for nb in plateau:
    nimSomme ^= nb
  if nimSomme == 0: # position perdante
    ligne = randint(0,len(plateau)-1)
    while plateau[ligne] == 0:
      ligne = randint(0,len(plateau)-1)
    nbjetons = randint(1,plateau[ligne])
    plateau[ligne] -= nbjetons
    print(f"l'IA en prend {nbjetons} sur la ligne {ligne+1}")
    print(plateau)
  else:
    compteur = 0
    for i in range(len(plateau)):
      if plateau[i] != 0:
        ligne = i
        compteur += 1
    if compteur == 1: # s'il ne reste qu'une seule ligne non vide, c'est fini
      print(f"l'IA en prend {plateau[ligne]} sur la ligne {ligne+1}.\nLe plateau est vide, vous avez perdu...")
      plateau[i] = 0
      print(plateau)
    else:
      i = 0
      while (plateau[i]^nimSomme) > plateau[i]: # on cherche une ligne permettant d'obtenir à nouveau nimSomme=0
        i += 1
      vieux = plateau[i]
      plateau[i] = nimSomme^plateau[i]
      print(f"l'IA en prend {vieux-plateau[i]} sur la ligne {i+1}")
      print(plateau)
```

<br>



