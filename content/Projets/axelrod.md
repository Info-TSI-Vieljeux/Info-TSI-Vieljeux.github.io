---
title: "Tournoi d'Axelrod"
date: 2021-03-06T14:23:56+01:00
weight : 8
draft: false
---

# Le tournoi d'Axelrod


La mission est d'implémenter le tournoi d'Axelrod première version présenté dans la vidéo ci-dessous.

Vous ferez concourir les stratégies suivantes en écrivant une fonction par stratégie :

- `AllC` : coopère toujours.
- `AllD` : trahit toujours.
- `Rando` : joue au hasard.
- `Alt` : alterne un coup sur deux.
- `TitforTat` : coopère au premier coup puis joue le coup précédent de l'adversaire.
- `Grudger` : commence par coopérer mais dès que l'autre trahit, trahit toujours.
- `Joss` : commence par coopérer puis joue le coup précédent de l'adversaire sauf 10% du temps où il trahit.
- `TitforTwoTats` : trahit si l'autre trahit deux fois de suite, coopère sinon.
- `TwoTitsforTat` : coopère tant que l'autre coopère, mais à chaque trahison de l'adversaire, trahit deux fois consécutives.
- `Tester` : commence par trahir. Si l'autre a coopéré au premier coup, `Tester` se repent et joue `TitforTat` pour la suite, sinon il joue `Alt`.
- `Eatherly` : commence par trahir puis trahit en proportion du taux de trahison de l'autre jusqu'à ce coup.
- `Gofman` : commence par coopérer. Si les deux joueurs ont joué différemment au coup précédent, trahit avec une probabilité de 5/7, et coopère s'ils ont joué la même chose.
- `Tullock` : coopère les 10 premiers coups puis coopère à chaque coup 10% de moins que l'autre a coopéré sur les 10 coups qui précèdent.
- `Pavlov` : commence par coopérer. Si l'autre a coopéré au dernier tour, on garde le même coup, sinon on change.

Donnez le palmarès du tournoi après 200 parties.

{{<youtube mScpHTIi-kM>}}
<br>

---

# Une solution :


```python
from random import random
import seaborn as sns
import matplotlib.pyplot as plt
```

Les différentes stratégies :

```python
def TitforTat(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) == 0:
        return 1
    elif liste_coups_adverses[-1]:
        return 1
    else:
        return 0

def Grudger(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) == 0:
        return 1
    else:
        if liste_coups_joueur[-1] == 0:
            return 0
        elif liste_coups_adverses[-1] == 0:
            return 0
        else:
            return 1

def Joss(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) == 0:
        return 1
    else:
        if random()<0.1:
            return 0
        else:
            return liste_coups_adverses[-1]

def Rando(liste_coups_joueur,liste_coups_adverses):
    return int(random()*2)

def AllD(liste_coups_joueur,liste_coups_adverses):
    return 0

def AllC(liste_coups_joueur,liste_coups_adverses):
    return 1

def TitforTwoTats(liste_coups_joueur,liste_coups_adverses): # tit for 2 tats
    if len(liste_coups_adverses) < 2:
        return 1
    elif liste_coups_adverses[-1]+liste_coups_adverses[-2] == 0:
        return 0
    else:
        return 1
        
def TwoTitsforTat(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) < 1:
        return 1
    elif liste_coups_adverses[-1] == 0 or (len(liste_coups_adverses) > 1 and liste_coups_adverses[-2] == 0):
        return 0
    else:
        return 1

def Tester(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) == 0:
        return 0
    elif len(liste_coups_adverses) == 1:
        return liste_coups_adverses[-1]
    else:
        if liste_coups_adverses[1]: # tit for tat
            return liste_coups_adverses[-1]
        else: # alternance
            return (len(liste_coups_adverses)+1)%2

def Eatherly(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) == 0:
        return 0
    else:
        if random() < (len(liste_coups_adverses)-sum(liste_coups_adverses))/len(liste_coups_adverses):
            return 0
        else:
            return 1

def Alt(liste_coups_joueur,liste_coups_adverses):
    return (len(liste_coups_adverses)+1)%2

def Gofman(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) == 0:
        return 1
    else:
        if liste_coups_adverses[-1] != liste_coups_joueur[-1]:
            if random() < 2/7:
                return 1
            else:
                return 0
        else:
            return 1

def Tullock(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) < 11:
        return 1
    else:
        if random() < sum(liste_coups_adverses)/len(liste_coups_adverses)-0.1:
            return 1
        else:
            return 0
            
def Pavlov(liste_coups_joueur,liste_coups_adverses):
    if len(liste_coups_adverses) == 0:
        return 1
    else:
        if not liste_coups_adverses[-1]:
            return 1-liste_coups_joueur[-1]
        else:
            return liste_coups_joueur[-1]
```

Match entre deux joueurs :

```python
def partie(joueurA,joueurB):
    nbre_parties = 200
    score_joueurA = 0
    score_joueurB = 0
    liste_coups_joueurA = []
    liste_coups_joueurB = []
    for i in range(nbre_parties):
        JA = dico_strategies[joueurA](liste_coups_joueurA,liste_coups_joueurB)
        JB = dico_strategies[joueurB](liste_coups_joueurB,liste_coups_joueurA)
        liste_coups_joueurA.append(JA)
        liste_coups_joueurB.append(JB)
        if JA:
            if JB:
                score_joueurA += 3
                score_joueurB += 3
            else:
                score_joueurA += 0
                score_joueurB += 5
        else:
            if JB:
                score_joueurA += 5
                score_joueurB += 0
            else:
                score_joueurA += 1
                score_joueurB += 1
    if joueurA == joueurB:
        dico_scores[joueurA] += score_joueurA
        matrice_tournoi[liste_joueurs.index(joueurA)][liste_joueurs.index(joueurA)] += score_joueurA
    else:
        dico_scores[joueurA] += score_joueurA
        dico_scores[joueurB] += score_joueurB
        matrice_tournoi[liste_joueurs.index(joueurB)][liste_joueurs.index(joueurA)] += score_joueurB
        matrice_tournoi[liste_joueurs.index(joueurA)][liste_joueurs.index(joueurB)] += score_joueurA
```

Le tournoi (on fait s'affronter tous les joueurs y compris eux-mêmes et on recommence 50 fois) :

```python
def tournoi():
    global partie
    nb_tournois = 100
    for i in range(nb_tournois):
        for j,JA in enumerate(liste_joueurs):
            for JB in liste_joueurs[j:]:
                partie(JA,JB)
    for i in range(len(matrice_tournoi)):
        for j in range(len(matrice_tournoi[0])):
            matrice_tournoi[i][j] = int(matrice_tournoi[i][j]/nb_tournois)
    for key in dico_scores:
        dico_scores[key] = int(dico_scores[key]/nb_tournois) 
```

Pour réinitialiser les scores entre deux tournois :

```python
def raz():
    global liste_joueurs,liste_strategies,dico_strategies,dico_scores,matrice_tournoi
    liste_joueurs = ["TitforTat","Grudger","Joss","AllD","AllC","TitforTwoTats","Tester","Eatherly","Alt","Gofman","Tullock","Rando","TwoTitsforTat"]
    liste_strategies = [TitforTat,Grudger,Joss,AllD,AllC,TitforTwoTats,Tester,Eatherly,Alt,Gofman,Tullock,Rando,TwoTitsforTat]
    dico_strategies = {J:S for (J,S) in zip(liste_joueurs,liste_strategies)}
    dico_scores = {J:0 for J in liste_joueurs}
    matrice_tournoi = [[0 for _ in range(len(liste_joueurs))] for _ in range(len(liste_joueurs))]
```

```python
raz()
tournoi()
liste_scores = [dico_scores[k] for k in dico_scores]
combo = list(zip(liste_scores,liste_joueurs))
combo.sort(reverse=True)
for s,j in combo:
    print(f"{j:17} : {s}")
```

{{<rawhtml>}}
<div style="font-family:monospace">
TitforTwoTats&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 7333<br>
Gofman&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 7132<br>
TitforTat&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 7113<br>
AllC&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 7076<br>
TwoTitsforTat&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 7048<br>
Grudger&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 6990<br>
Pavlov&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 6957<br>
Tullock&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 6467<br>
Rando &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 5991<br>
Alt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 5962<br>
Eatherly&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 5792<br>
Joss&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 5775<br>
AllD&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 5732<br>
Tester&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 5664<br>
</div>
{{</rawhtml>}}


```python
plt.figure(figsize=(15,15),dpi=150)
s = sns.heatmap(matrice_tournoi, annot=True, fmt="d", cmap='YlGnBu', xticklabels=liste_joueurs, yticklabels=liste_joueurs)
plt.tick_params(axis='both', which='both', length=5)
s.xaxis.tick_top()
s.xaxis.set_label_position('top')
plt.xticks(rotation=90)
```

![](/restournoi.png)


<script>
// Helper function to simulate random number for strategies that require randomness
function random() {
    return Math.random();
}

function TitforTat(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length === 0) {
        return 1;
    } else {
        return liste_coups_adverses[liste_coups_adverses.length - 1];
    }
}

function Grudger(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length === 0) {
        return 1;
    }
    else {
        if (liste_coups_joueur[liste_coups_joueur.length - 1] == 0){
            return 0;
            }
        else if (liste_coups_adverses[liste_coups_adverses.length - 1] === 0) {
            return 0;
            }
        else {
            return 1;
        }
    }
}

function Joss(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length === 0) {
        return 1;
    } else {
        if (random() < 0.1) {
            return 0;
        } else {
            return liste_coups_adverses[liste_coups_adverses.length - 1];
        }
    }
}

function Rando(liste_coups_joueur, liste_coups_adverses) {
    return Math.round(random());
}

function AllD(liste_coups_joueur, liste_coups_adverses) {
    return 0;
}

function AllC(liste_coups_joueur, liste_coups_adverses) {
    return 1;
}

function TitforTwoTats(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length < 2) {
        return 1;
    } else if (liste_coups_adverses.slice(-2).reduce((a, b) => a + b, 0) === 0) {
        return 0;
    } else {
        return 1;
    }
}

function TwoTitsforTat(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length < 1) {
        return 1;
    } else if (liste_coups_adverses[liste_coups_adverses.length - 1] === 0 || (liste_coups_adverses.length > 1 && liste_coups_adverses[liste_coups_adverses.length - 2] === 0)) {
        return 0;
    } else {
        return 1;
    }
}

function Tester(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length === 0) {
        return 0;
    } else if (liste_coups_adverses.length === 1) {
        return liste_coups_adverses[0];
    } else {
        if (liste_coups_adverses[1]) { // Tit for Tat
            return liste_coups_adverses[liste_coups_adverses.length - 1];
        } else { // Alternance
            return (liste_coups_adverses.length + 1) % 2;
        }
    }
}

function Eatherly(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length === 0) {
        return 0;
    } else {
        let cooperationRatio = (liste_coups_adverses.length - liste_coups_adverses.reduce((a, b) => a + b, 0)) / liste_coups_adverses.length;
        if (random() < cooperationRatio) {
            return 0;
        } else {
            return 1;
        }
    }
}

function Alt(liste_coups_joueur, liste_coups_adverses) {
    return (liste_coups_adverses.length + 1) % 2;
}

function Gofman(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length === 0) {
        return 1;
    } else {
        if (liste_coups_adverses[liste_coups_adverses.length - 1] !== liste_coups_joueur[liste_coups_joueur.length - 1]) {
            if (random() < 2 / 7) {
                return 1;
            } else {
                return 0;
            }
        } else {
            return 1;
        }
    }
}

function Tullock(liste_coups_joueur, liste_coups_adverses) {
    if (liste_coups_adverses.length < 11) {
        return 1;
    } else {
        let cooperationRatio = liste_coups_adverses.reduce((a, b) => a + b, 0) / liste_coups_adverses.length;
        if (random() < cooperationRatio - 0.1) {
            return 1;
        } else {
            return 0;
        }
    }
}

function Pavlov(liste_coups_joueur, liste_coups_adverses) {
    // Commence par coopérer
    if (liste_coups_joueur.length === 0) {
        return 1;
    }
    let dernier_coup_joueur = liste_coups_joueur[liste_coups_joueur.length - 1];
    let dernier_coup_adverse = liste_coups_adverses[liste_coups_adverses.length - 1];
    // Gagnant si les deux coopèrent ou si le joueur seul trahit
    if ((dernier_coup_joueur === 1 && dernier_coup_adverse === 1) || 
        (dernier_coup_joueur === 0 && dernier_coup_adverse === 1)) {
        return dernier_coup_joueur; // répète le dernier coup
    } else {
        return 1 - dernier_coup_joueur; // change le dernier coup
    }
}

function partie(joueurA, joueurB) {
    let nbre_parties = 200;
    let score_joueurA = 0;
    let score_joueurB = 0;
    let liste_coups_joueurA = [];
    let liste_coups_joueurB = [];

    for (let i = 0; i < nbre_parties; i++) {
        let JA = joueurA(liste_coups_joueurA, liste_coups_joueurB);
        let JB = joueurB(liste_coups_joueurB, liste_coups_joueurA);
        liste_coups_joueurA.push(JA);
        liste_coups_joueurB.push(JB);
        if (JA) {
            if (JB) {
                score_joueurA += 3;
                score_joueurB += 3;
            } else {
                score_joueurA += 0;
                score_joueurB += 5;
            }
        } else {
            if (JB) {
                score_joueurA += 5;
                score_joueurB += 0;
            } else {
                score_joueurA += 1;
                score_joueurB += 1;
            }
        }
    }

    return {score_joueurA, score_joueurB};
}

const strategies = {
    "TitforTat": TitforTat,
    "Grudger": Grudger,
    "Joss": Joss,
    "Rando": Rando,
    "AllD": AllD,
    "AllC": AllC,
    "TitforTwoTats": TitforTwoTats,
    "TwoTitsforTat": TwoTitsforTat,
    "Tester": Tester,
    "Eatherly": Eatherly,
    "Alt": Alt,
    "Gofman": Gofman,
    "Tullock": Tullock,
    "Pavlov": Pavlov
};

function playMatch() {
    let playerAStrategyName = document.getElementById("playerAStrategy").value;
    let playerBStrategyName = document.getElementById("playerBStrategy").value;

    let playerAStrategy = strategies[playerAStrategyName];
    let playerBStrategy = strategies[playerBStrategyName];

    let {score_joueurA, score_joueurB} = partie(playerAStrategy, playerBStrategy);

    document.getElementById("playerAScore").innerHTML = playerAStrategyName + " : " + score_joueurA;
    document.getElementById("playerBScore").innerHTML = playerBStrategyName + " : " + score_joueurB;
}

</script>



<div style="display: flex;justify-content: center;">
<div>
    <select id="playerAStrategy" style="font-size:1.3em;width:150px;">
    <option value="TitforTat">Tit for Tat</option>
    <option value="Grudger">Grudger</option>
    <option value="Joss">Joss</option>
    <option value="Rando">Rando</option>
    <option value="AllD">AllD</option>
    <option value="AllC">AllC</option>
    <option value="TitforTwoTats">Tit for Two Tats</option>
    <option value="TwoTitsforTat">Two Tits for Tat</option>
    <option value="Tester">Tester</option>
    <option value="Eatherly">Eatherly</option>
    <option value="Alt">Alt</option>
    <option value="Gofman">Gofman</option>
    <option value="Tullock">Tullock</option>
    <option value="Pavlov">Pavlov</option>
</select>

<p style="text-align:center; font-size:2em">&#9889;</p> 

<select id="playerBStrategy" style="font-size:1.3em;width:150px;">
     <option value="TitforTat">Tit for Tat</option>
    <option value="Grudger">Grudger</option>
    <option value="Joss">Joss</option>
    <option value="Rando">Rando</option>
    <option value="AllD">AllD</option>
    <option value="AllC">AllC</option>
    <option value="TitforTwoTats">Tit for Two Tats</option>
    <option value="TwoTitsforTat">Two Tits for Tat</option>
    <option value="Tester">Tester</option>
    <option value="Eatherly">Eatherly</option>
    <option value="Alt">Alt</option>
    <option value="Gofman">Gofman</option>
    <option value="Tullock">Tullock</option>
  <option value="Pavlov">Pavlov</option>
</select>
</div>
</div>


<div style="text-align:center">

<style>
  button {
            font-size: 1.2em; 
            padding: 10px 20px; 
            border-radius: 20px; 
            border: none; 
            background-color: lightgreen; 
            cursor: pointer; 
            transition: background-color 0.3s; 
        }
        button:hover {
            background-color: red; 
            color: white;
        }
</style>

<button onclick="playMatch()">Lancer le match</button>


<h3>Scores:</h4>
<p id="playerAScore" style="font-size:30px">Player A : 0</p>
<p id="playerBScore" style="font-size:30px">Player B : 0</p>

</div>

---

## Mission bonus :

Imaginer une nouvelle stratégie qui se hisse sur le podium du tournoi contre les autres stratégies déjà implémentées.