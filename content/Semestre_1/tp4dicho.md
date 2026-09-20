---
title: "TP 4 : algorithmes dichotomiques"
date: 2021-03-06T14:23:56+01:00
weight : 4
draft: false
---

<link rel="stylesheet" href="/path/to/styles/default.min.css">
<script src="/path/to/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
<style>
#correc
{
  color: #006C65;
  border-left: solid 10px #C7DDDC;
}
#comm
{
  color: #004D80;
  border-left: solid 10px #B3CAD9;
}
#commsum
{
  color: #004D80;
}
#correcsum
{
  color: #006C65;
}
details > summary:first-of-type {
  display: list-item;     
  cursor: pointer;      
}

details > summary:first-of-type {
  list-style: disclosure-closed inside;
}
details[open] > summary:first-of-type {
  list-style-type: disclosure-open;
}
</style>


# Algorithmes dichotomiques

<p style="text-align: center;">  Cliquez sur <a href="https://classroom.github.com/a/VzwADzeZ">cette invitation</a> pour récupérer le repository du TP. </p>

## Recherche dichotomique

L'algorithme de recherche mis au point dans le tp1 compte dans le pire des cas autant d'étapes que l'ensemble scruté contient d'éléments.<br>
Peut-on faire mieux ?<br>
Dans le cas, d'un ensemble ordonné **trié**, la réponse est oui. On peut même faire *beaucoup* mieux !

Imaginons que l'on cherche une carte dans un jeu trié en ordre croissant. L'idée est de regarder d'abord au milieu du paquet. Si la carte du milieu est plus petite (repectivement plus grande) que la carte cherchée, on en déduit que celle-ci ne peut être que dans la deuxième partie (respectivement dans la première partie) du paquet (si elle est bien présente).\
On peut alors se débarrasser de la moitié des cartes environ et on recommence la manœuvre avec les cartes restantes.

{{< youtube iP897Z5Nerk >}}

Voilà ci-dessous une tentative d'implémentation de cet algorithme :


```python
def recherche_dicho(L,x):
    n = len(L)
    g, d = 0, n-1
    while g < d:
        i = (g + d)//2
        if x < L[i]:
            d = i - 1 
        elif x > L[i]:
            g = i + 1
        else:
            return True           
    return False
```

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
Attention à ne pas confondre avec <code>recherche_dico</code> du TP1, il ne s'agit pas ici de dictionnaires, mais de dic<u>h</u>otomie...
</blockquote>
</details>



> Testez cet algorithme et constatez qu'il contient une erreur.<br>
> Recopier ci-dessous une liste triée et un élément à rechercher qui mettent en échec l'algorithme.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On peut trouver de telles listes sans réfléchir en utilisant le code suivant&nbsp;:
<pre><code class="language-python">from random import randint
for k in range(20):
    L = [randint(1,10) for i in range(5)]
    L = sorted(L)
    x = randint(1,10)
    a = recherche_dicho(L,x)
    b = x in L
    if not ((not a and not b) or (a and b)):
        print(a,b,x,L) 
</pre></code>
Si on donne la liste <code>[2, 5, 7, 7, 8]</code> en argument, la fonction renverra <code>False</code> si on lui demande de rechercher <code>5</code>.
</blockquote>
</details>

> Corrigez l'algorithme `recherche_dicho_corr` en ajoutant un seul caractère.\
Attention, tout autre ajout, même un espace, rendra faux l'exercice.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Il suffit d'ajouter un <code>=</code> dans la condition de la boucle <code>while</code>&nbsp;:<br>
<code>while g <= d:</code>
</blockquote>
</details>

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
Voyons pourquoi ça ne marche pas sans la correction dans le cas du contre-exemple donné&nbsp;:<br>
<code>recherche_dicho([2, 5, 7, 7, 8],5)</code>
<ul>
<li>initialisation : $g\leftarrow 0$, $d\leftarrow 5$</li>
<li>itération 1 : $i\leftarrow 2$, <code>L[i]</code> vaut $7$ et donc, $d\leftarrow 1$ (on est dans le <code>if</code>)</li>
<li>itération 2 : $i\leftarrow 0$, <code>L[0]</code> vaut $2$ et donc, $g\leftarrow 1$  (on est dans le <code>elif</code>)</li>
</ul>
Sans la correction, on sort de la boucle <code>while</code> à ce moment. La fonction retourne donc à tort <code>False</code>.<br><br>
Avec la correction, on fait un nouveau tour dans la boucle&nbsp;:
<ul>
<li>itération 3 : $i\leftarrow 1$, <code>L[1]</code> vaut $5$ et on est donc dans le <code>else</code> $\Rightarrow$ la fonction retourne <code>True</code> </li>
</ul>

</blockquote>
</details>

La figure suivante est un arbre binaire décrivant tous les chemins possibles que prend l'algorithme à partir d'une liste de 16 éléments (en vert, le nombre d'éléments restant).

![](/arbrebin.jpg)

Cet algorithme peut se montrer bien plus rapide que la recherche simple du TP1.<br>
Réouvrons la liste de mots de passe du TP2 mais en la transformant en liste de mots plutôt qu'en long texte.


```python
# importation de la classique liste de mots de passe rockyou (cela prend quelques secondes)
from urllib.request import urlopen
url = 'http://cordier-phychi.toile-libre.org/Info/github/rockyou.txt'
rockyou = urlopen(url).read().decode('latin-1').split()
```

```python
rockyou = sorted(rockyou)
print(len(rockyou),'mots de passe')
```
`14445388 mots de passe`

```python
def trouve_indice(L, x):
    '''
    trouve_indice(L: liste, x: type des éléments de L) -> soit un entier, soit un booléen
    postcondition: renvoie l'indice d'un éléments x lorsqu'il est présent dans la liste L
    et renvoie False lorsqu'il est absent
    '''
    for indice, element in enumerate(L):
        if element == x:
            return indice
    return False
```

Rq : `enumerate` est une fonction native plutôt pratique (mais en rien indispensable et d'ailleurs pas au programme).


<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
Ce n'est pas bien dur de réécrire la fonction sans utiliser <code>enumerate</code>&nbsp;:
<pre><code class="language-python">def trouve_indice(L, x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return False
</pre></code>
</blockquote>
</details>


```python
from time import time
from random import randint
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (15, 6)

Indice, T_ch = [], []
liste_noms = ['567890','billgates','dollars','jklmno','pupuce','zorro']
for nom in liste_noms:
    start = time()
    i = trouve_indice(rockyou,nom)
    stop = time()
    Indice.append(i)
    T_ch.append(stop-start)
    print(f"{stop -start:.2e} s pour trouver '{nom}' qui est à la position {i}")
plt.plot(Indice,T_ch,'--')
plt.plot(Indice,T_ch,'o',c='C2')
plt.xlabel("Position dans la liste")
plt.ylabel("Temps pour trouver le nom (s)")
```
`1.84e-01 s pour trouver '567890' qui est à la position 2612528`\
`3.93e-01 s pour trouver 'billgates' qui est à la position 5584305`\
`4.85e-01 s pour trouver 'dollars' qui est à la position 6925245`\
`6.32e-01 s pour trouver 'jklmno' qui est à la position 8867150`\
`8.32e-01 s pour trouver 'pupuce' qui est à la position 11949039`\
`1.01e+00 s pour trouver 'zorro' qui est à la position 14416270`

![png](/tpstrouvernom.png)

> Comment semble évoluer le temps de recherche en fonction de la position dans la liste ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Le temps de recherche semble évoluer linéairement en fonction de la position dans la liste (durée $\propto$ position).
</blockquote>
</details>

Avec l'algorithme de recherche dichotomique, on obtient :

```python
T_ch = []
liste_noms = ['567890','billgates','dollars','jklmno','pupuce','zorro']
for i,nom in zip(Indice,liste_noms):
    start = time()
    recherche_dicho_corr(rockyou,nom)
    stop = time()
    T_ch.append(stop-start)
    print(f"{stop -start:.2e} s pour trouver {nom} qui est à la position {i}")

plt.plot(Indice,T_ch,'--')
plt.plot(Indice,T_ch,'o',c='C2')
for i in range(len(liste_noms)) :
    plt.text(Indice[i]+max(Indice)/100,T_ch[i],liste_noms[i])
plt.xlabel("Position dans la liste (s)")
plt.ylabel("Temps pour trouver le nom")
plt.savefig('graph.png',dpi=600)
```
`1.41e-05 s pour trouver 567890 qui est à la position 2612528`\
`1.41e-05 s pour trouver billgates qui est à la position 5584305`\
`1.10e-05 s pour trouver dollars qui est à la position 6925245`\
`2.19e-05 s pour trouver jklmno qui est à la position 8867150`\
`1.12e-05 s pour trouver pupuce qui est à la position 11949039`\
`1.41e-05 s pour trouver zorro qui est à la position 14416270`

![png](/tpsmotdicho.png)

On constate que l'algorithme dichotomique met beaucoup moins de temps et qu'il ne semble pas dépendre clairement de la position de l'élément.

Tentons de comparer le comportement des deux algorithmes quand la longueur de la liste augmente.

Quel que soit l'algorithme de recherche, la **pire situation possible** correspond à la recherche d'un élément absent de la liste.\
Se placer dans ce pire des cas permet une comparaison plus sûre des algorithmes ; on sait à quoi s'attendre !

Mesurer un temps dépend de trop de paramètres (processeur, utilisation de la mémoire par le système, etc.).\
Une information plus universelle est le **nombre d'étapes de l'algorithme**.\
Plus précisément, concentrons sur le nombre de comparaisons entre l'élément recherché `x` et les éléments de la liste `L`.

On a construit ci-dessous la fonction `trouve_indice_etapes` dont la description est donnée :
```python
def trouve_indice_etapes(L,x):
    """
    trouve_indice_etapes(liste: list, valeur: type des éléments de la liste) -> bool, int
    postcondition: retourne à la fois un booléen qui traduit la présence ou non de l'élément 
    et un entier correspondant au nombre de comparaisons effectuées entre x et les éléments de L
    """
    nb_comp = 0
    for indice, element in enumerate(L):
        nb_comp += 1
        if element == valeur:
            return True,nb_comp
    return False,nb_comp
```
> À vous de jouer pour construire sur le même modèle `recherche_dicho_etapes` :

```python
def recherche_dicho_etapes(L,x) :
    """
    recherche_dicho_etapes(liste: list, valeur: type des éléments de la liste) -> bool, int
    postcondition: doit retourner à la fois un booléen qui traduit la présence ou non de l'élément 
    et un entier correspondant au nombre de comparaisons effectuées entre x et les éléments de L
    """
    ### VOTRE CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Il faut faire très attention aux endroits où l'on place les incrémentations de <code>nbcomp</code> dans le code de <code>recherche_dicho</code>.<br>
À chaque itération, il peut y avoir soit 1 comparaison (en passant par le <code>if</code>), soit 2 (en passant par le <code>elif</code> ou le <code>else</code>).
<pre><code class="language-python">def recherche_dicho_etapes(L,x) :
    n = len(L)
    nb_comp = 0
    g, d = 0, n-1
    while g <= d:
        i = (g + d)//2
        nb_comp += 1 # toujours au moins 1 comparaison (celle du if)
        if x < L[i]:
            d = i - 1 # pas d'incrémentation car déjà comptée
        elif x > L[i]:
            g = i + 1
            nb_comp += 1 # on ajoute la comparaison du elif
        else:
            nb_comp += 1 # la comparaison du elif a été faite et elle s'est avérée fausse
            return True,nb_comp
    return False,nb_comp
</pre></code>
</blockquote>
</details>


Maintenant, comparons :
```python
import pandas as pd
NB_elts, NB_comp = [], []
nom = '???#!!!'
liste_longueurs = [10*2**i for i in range(1,19)]

for longueur in liste_longueurs:
    start = time()
    nb_comp = trouve_indice_etapes(rockyou[:longueur],nom)[1]
    stop = time()
    NB_elts.append(longueur)
    NB_comp.append(nb_comp)

d = {'taille' : NB_elts,'# comparaisons': NB_comp}
tableau = pd.DataFrame(data=d)
display(tableau)
fig, axs = plt.subplots(2,figsize=(15,12))
axs[0].plot(NB_elts,NB_comp,'--')
axs[0].plot(NB_elts,NB_comp,'o',c='C2')
axs[1].semilogx(NB_elts,NB_comp,'--')
axs[1].semilogx(NB_elts,NB_comp,'o',c='C2')
axs[0].set(xlabel='Longueur de la liste', ylabel='Nb de comparaisons')
axs[1].set(xlabel='Longueur de la liste (axe logarithmique)', ylabel='Nb de comparaisons')
```
{{<rawhtml>}}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>taille</th>
      <th># comparaisons</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2</th>
      <td>80</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>160</td>
      <td>160</td>
    </tr>
    <tr>
      <th>4</th>
      <td>320</td>
      <td>320</td>
    </tr>
    <tr>
      <th>5</th>
      <td>640</td>
      <td>640</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1280</td>
      <td>1280</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2560</td>
      <td>2560</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5120</td>
      <td>5120</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10240</td>
      <td>10240</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20480</td>
      <td>20480</td>
    </tr>
    <tr>
      <th>11</th>
      <td>40960</td>
      <td>40960</td>
    </tr>
    <tr>
      <th>12</th>
      <td>81920</td>
      <td>81920</td>
    </tr>
    <tr>
      <th>13</th>
      <td>163840</td>
      <td>163840</td>
    </tr>
    <tr>
      <th>14</th>
      <td>327680</td>
      <td>327680</td>
    </tr>
    <tr>
      <th>15</th>
      <td>655360</td>
      <td>655360</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1310720</td>
      <td>1310720</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2621440</td>
      <td>2621440</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml>}}

![](/linetlog.png)

```python
NB_elts, NB_comp = [], []
nom = '???#!!!'
liste_longueurs = [10*2**i for i in range(1,19)]

for longueur in liste_longueurs:
    start = time()
    nb_comp = recherche_dicho_etapes(rockyou[:longueur],nom)[1]
    stop = time()
    NB_elts.append(longueur)
    NB_comp.append(nb_comp)

d = {'taille' : NB_elts,'# comparaisons': NB_comp}
tableau = pd.DataFrame(data=d)
display(tableau)
fig, axs = plt.subplots(2,figsize=(15,12))
axs[0].plot(NB_elts,NB_comp,'--')
axs[0].plot(NB_elts,NB_comp,'o',c='C2')
axs[1].semilogx(NB_elts,NB_comp,'--')
axs[1].semilogx(NB_elts,NB_comp,'o',c='C2')
axs[0].set(xlabel='Longueur de la liste', ylabel='Nb de comparaisons')
axs[1].set(xlabel='Longueur de la liste (axe logarithmique)', ylabel='Nb de comparaisons')
```
{{<rawhtml>}}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>taille</th>
      <th># comparaisons</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>80</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>160</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>320</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>640</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1280</td>
      <td>11</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2560</td>
      <td>12</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5120</td>
      <td>13</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10240</td>
      <td>14</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20480</td>
      <td>15</td>
    </tr>
    <tr>
      <th>11</th>
      <td>40960</td>
      <td>16</td>
    </tr>
    <tr>
      <th>12</th>
      <td>81920</td>
      <td>17</td>
    </tr>
    <tr>
      <th>13</th>
      <td>163840</td>
      <td>18</td>
    </tr>
    <tr>
      <th>14</th>
      <td>327680</td>
      <td>19</td>
    </tr>
    <tr>
      <th>15</th>
      <td>655360</td>
      <td>20</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1310720</td>
      <td>21</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2621440</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml>}}

![png](/linetlogdich.png)

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
Dans le cas de la recherche linéaire, le nombre de comparaisons est proportionnel à la taille de la liste alors que dans le cas de la recherche dichotomique, le nombre de comparaisons est proportionnel au logarithme de la taille de la liste&nbsp;!
</pre></code>
</blockquote>
</details>

<br>


## Recherche dichotomique d'une racine

On cherche à appliquer la méthode de la dichotomie (découpage en deux systématique d'un intervalle) à la recherche d'une racine.

Plus précisément, on souhaite déterminer une approximation d’une racine (ou zéro) sur un intervalle $[a, b]$, avec une précision $ε$, d’une fonction continue et monotone $f$ sur cet intervalle et telle que $f(a)$ et $f(b)$ sont de signes opposés ($f(a)f(b)≤0)$. Elle consiste à comparer le signe de l’image $f\left(\frac{a + b}{2}\right)$ du milieu de l’intervalle $[a, b]$ avec le signe de $f(a)$ et $f(b)$ pour réduire l’intervalle de recherche de manière itérative.

Pour déterminer $x_0$, racine de la fonction $f$, strictement monotone sur l’intervalle $[a, b]$, avec une précision $ε,$ on procède comme suit :

1. On détermine le milieu de l’intervalle $m = \frac{a+b}{2}$ ;  
2. On compare le signe de $f(m)$ avec celui de $f(a)$ et $f(b)$ pour déterminer dans quel intervalle $[a, m]$ ou $[m, b]$ se trouve la racine $x_0$ ;  
3. On affecte à $a$ (resp. $b$) la valeur de $m$ si la racine se trouve entre $m$ et $b$ (resp. $a$) ;  
4. On itère tant que $|a − b| > ε$, (ε est la précision définie initialement), et on renvoie $m$. 

{{< video src="/dichot.mp4" type="video/mp4" preload="auto" >}}

> Construisez une fonction `racine` prenant en argument une fonction `f`, les bornes d'un intervalle `a` et `b`, et une précision `eps` et retournant la racine ainsi que le nombre d'itérations nécessaires.
> Vous vous assurerez grâce à un `assert` qu'au moins une racine existe bel et bien dans l'intervalle choisi et vous sécuriserez la boucle `while` en ajoutant une condition empèchant l'algorithme d'utiliser plus de 100 itérations.

```python
def racine(f,a,b,eps) :
    """
    racine(f: fonction, a: flottant, b: flottant, eps: flottant) -> racine: flottant, nbiter: entier
    précondition: f doit être une fonction n'ayant qu'un argument (un flottant) et ne retournant qu'un flottant.
    """
    ### BEGIN SOLUTION
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def racine(f,a,b,eps):
    assert f(a)*f(b)<0
    nbiter = 1
    nbitermax = 100
    m = (a + b)/ 2  
    while abs(a - b) > eps and nbiter < nbitermax:  # condition de convergence + non-dépassement d'un nombre limite d'iterations
        m = (a + b)/ 2  
        if f(a) * f(m) < 0:  
            b = m  
        else:  
            a = m  
        nbiter += 1  
    return m, nbiter
</pre></code>
</blockquote>
</details>


> Comment évolue l'accroissement du nombre d'iterations en fonction de l'accroissement du nombre de chiffres significatifs obtenus pour la racine ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Traçons cette évolution grâce au code suivant&nbsp;:
<pre><code class="language-python">def f(x):
    return x**2-2
Leps, Let = [], []
for i in range(1,15): 
    eps = 10**(-i)
    Leps.append(1+i)
    nb_etapes = racine(f,1,2,eps)[1]
    Let.append(nb_etapes)
plt.plot(Leps,Let,'--')
plt.plot(Leps,Let,'o',c='C2')
plt.xlabel("Nombre de chiffres significatifs")
plt.ylabel("Nombre d'étapes")
</pre></code>
On obtient :<br>
<img src="/corrdichofin.png">
<code>i+1</code> correspond bien ici au nombre de chiffres significatifs souhaités puisque la solution, 1,414..., ne contient qu'un seul chiffre avant la virgule.<br><br>
On constate que l'accroissement du nombre d'itérations semble proportionnel à l'accroissement du nombre de chiffres significatifs souhaité.
</blockquote>
</details>