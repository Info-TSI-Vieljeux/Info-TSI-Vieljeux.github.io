---
title: "TP 5 : fonctions récursives"
date: 2021-03-06T14:23:56+01:00
weight : 5
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


# Fonctions récursives



<p style="text-align: center;">  Cliquez sur <a href="https://classroom.github.com/a/ti0x49a6">cette invitation</a> pour récupérer le repository du TP. </p>



{{< youtube lIIXLQvcd4Q>}}

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (10, 10)
fig, ax = plt.subplots()
ax.set_aspect(1)
couleurs = plt.rcParams['axes.prop_cycle'].by_key()['color']
```
&nbsp;

## Visualisation des appels récursifs

Installons un module permettant de représenter sous forme de graphe les différents appels récursifs d'une fonction.

```python
%%capture
!pip install recursionvisualisation==0.2
```
On construit une fonction récursive `somme(n)` qui retourne la somme des n premiers entiers et on utilise un décorateur (fonction qui modifie le comportement d'autres fonctions) pour visualiser les différents appels récursifs faits par `somme`.

```python
from recursionvisualisation import viz, CallGraph
cg = CallGraph()
@viz(cg) # décorateur

def somme(n):
    if n < 1:
        return 0
    return n + somme(n - 1)
    
print(f'somme(5) = {somme(5)}')
cg.render()
```


`somme(5) = 15`
![](/sommerecu.png?width=900px)

On observe l'empilement des appels successifs de `somme` jusqu'à ce que le cas de base soit touché. Ces appels forment une **pile d'exécution** (ou pile d'appels, "call stack" en anglais).<br>
Le cas de base correspond à la première valeur retournée (0 ici) et donc au premier appel retiré de la pile. Tous les appels précédents sont restés **en attente**.<br>
On remonte ensuite chronologiquement la pile des appels avec à chaque fois une nouvelle valeur retournée, jusqu'à l'appel initial, appelé **appel terminal**.

> Combien l'expression `somme(100)` va-t-elle provoquer d'appels de la fonction `somme` ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
101
</blockquote>
</details>

Les choses se compliquent si plusieurs appels récursifs sont faits dans la définition de la fonction.<br>
Le nombre d'appels progresse maintenant exponentiellement mais pas la taille de la pile d'exécution qui correspond au nombre de niveaux (à la profondeur de l'arbre).<br>

```python
cg = CallGraph()
@viz(cg)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(f'{fib(5) = }')
cg.render()
```
`fib(5) = 5`
![](/fibrecu.png?width=900px)

Comme on le voit ci-dessus, `fib(5)` fait 15 appels à la fonction mais la pile ne dépasse jamais 6 appels en attente.<br>
En effet, `fib(5)` appelle `fib(4)` qui appelle `fib(3)`qui appelle `fib(2)` qui appelle `fib(1)`. Comme `fib(1)` est un des deux cas de base possible, il retourne la valeur 1 et est retiré de la pile. Le dernier appel en attente de la pile est alors `fib(2)`, on y retourne.<br>
`fib(2)` fait son deuxième appel : `fib(0)`. `fib(0)` étant l'autre cas de base, il retourne une valeur (0) et est retiré de la pile. `fib(2)` peut maintenant elle aussi retourner une valeur (1+0) et est à son tour retirée de la pile.<br> 
Le dernier appel en attente est dorénavant `fib(3)` qui fait maintenant son deuxième appel : `fib(1)`. `fib(1)` retourne 1 et est retiré de la liste, `fib(2)` retourne 2 (1+1) et est retirée à son tour, et on remonte à `fib(4)` qui fait son deuxième appel, `fib(2)`, qui elle-même appelle `fib(1)`, etc.

> Quelle sera la taille maximale de la pile d'exécution de `fib(100)` ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
100
</blockquote>
</details>

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
Par contre, le nombre d'appels est bien plus grand (cf. vidéo).
</blockquote>
</details>

&nbsp;


## Deux tris récursifs

Construisons les deux tris récursifs présentés dans la vidéo.

### Tri insertion

> Écrire la fonction `insertion` qui insert au bon endroit un nombre dans une liste triée afin qu'elle reste triée.


```python
def insertion(element,Ltriee):
    """
    insertion(element: nombre, Ltriee: liste de nombres) -> Lsortie: liste de nombres
    insertion insert 'nombre' au bon endroit dans 'Ltriee' et retourne cette nouvelle liste.
    préconditions: 'element' est un entier ou un flottant, 'Ltriee' est une liste de nombres triée en ordre croissant
    postconditions: 'Lsortie' est triée dans l'ordre croissant (et len(Lsortie)==len(Ltriee)+1)
    """
    ### VOTRE CODE
```

Exemple : `insertion(5,[-12,1e-2,0,3,18])` doit renvoyer `[-12,1e-2,0,3,5,18]` .

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def insertion(element,Ltriee):
    i = 0
    while i < len(Ltriee) and element > Ltriee[i]:
        #inverser les deux conditions provoque une erreur (caractère paresseux de and)
        i += 1
    Lsortie = Ltriee[:i]+[element]+Ltriee[i:]
    return Lsortie
</pre></code>
</blockquote>
</details>

> Combien d'itérations sont nécessaires dans le pire des cas pour insérer un élément dans une liste de longueur `n` ?

- A : $n$
- B : $2n$
- C : $n^2$


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$n$
</blockquote>
</details>


> Ajouter le cas de base à la fonction `tri_insertion` :


```python
def tri_insertion(liste) :
    n = len(liste)
    ### VOTRE CODE
    else :
        element = liste[0]
        reste = liste[1:]
        return insertion(element,tri_insertion(reste))
        # si pas de return dans le else alors tous les appels de tri_insertion avec un len > 1 sont de type None !!!
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def tri_insertion(liste) :
    n = len(liste)
    if n == 1 or n == 0 : # cas de base
        return liste
    else :
        element = liste[0]
        reste = liste[1:]
        return insertion(element,tri_insertion(reste))
</pre></code>
</blockquote>
</details>

> Combien d'appels à `tri_insertion` sont faits au sein de `tri_insertion(L)` quand `L` à une taille `n` ?

- A : $n-1$
- B : $2^n$
- C : $\log_2(n)$


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$n-1$
</blockquote>
</details>

&nbsp;

### Tri fusion


{{< youtube XaqR3G_NVoo>}}


> Écrire la fonction `fusion` qui fusionne deux listes triées en une seule liste triée.


```python
def fusion(Ltrie1,Ltrie2):
    """
    fusion(Ltrie1: liste de nombres, Ltrie2: liste de nombres) -> liste_sortie: liste de nombres
    fusion retourne une seule liste ordonnée à partir de deux sous-listes ordonnées.
    préconditions: Ltrie1 et Ltrie2 sont triées dans l'ordre croissant.
    postconditions: 'Lfus' est triée dans l'ordre croissant (et len(Lfus)==len(Ltrie1)+len(Ltrie2)).
    """
	### VOTRE CODE
```
Exemple : `fusion([-12,3.5,18],[-2,15])` doit renvoyer `[-12,-2,3.5,15,18]`.

  <details>
  <summary id="correcsum">
  Correction (cliquer pour afficher)</summary>
  <blockquote id="correc">
  <pre><code class="language-python">def fusion(Ltrie1,Ltrie2) :
      if Ltrie1 == []:
          return Ltrie2
      elif Ltrie2 == []:
          return Ltrie1
      elif Ltrie1[0] <= Ltrie2[0]:
          return [Ltrie1[0]] + fusion(Ltrie1[1:],Ltrie2)
      else:
          return [Ltrie2[0]] + fusion(Ltrie1,Ltrie2[1:])</pre></code>
  </blockquote>
  </details>

> Compléter la définition de `tri_fusion` pour le rendre opérant. Il faut que chaque appel récursif concerne approximativement une moitié de la liste.

```python
def tri_fusion(L):
    n = len(L)
    if n == 1:
        return L
    else:
        L = fusion(trifusion(L[...]),trifusion(L[...]))
        return L
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Un découpage en deux parties approximativement égales de la liste est obtenu par <code>L[:n//2]</code> et <code>L[n//2:]</code>.<br>
On écrit donc&nbsp;:<br>
<code>L = fusion(trifusion(L[:n//2]),trifusion(L[n//2:]))</code>
</blockquote>
</details>

Supposons que la longueur de la liste `L` soit une puissance de 2.\
Au niveau de récursivité $j$ (à l'appel initial de `tri_fusion(L)`, $j=0$, pour les deux appels à `tri_fusion` au sein de `tri_fusion(L)`, $j=1$, etc.), on a décomposé le problème initial en ... fusions, chacune opérant sur des sous-listes de taille ... .

> Par quoi faut-il compléter les pointillés respectivement ?

- A : $2^j$ et $2^j$
- B : $n/2^j$ et $n/2^j$
- C : $2^j$ et $n/2^j$
- D : $n/2^j$ et $2^j$

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On a décomposé le problème initial en $2^j$ fusions, chacune opérant sur des sous-listes de taille $n/2^j$.
</blockquote>
</details>

&nbsp;
&nbsp;

## Algorithme d'Euclide

Un des plus vieux algorithmes connus, l'algorithme d'Euclide, suit un raisonnement récursif et s'écrit donc naturellement de cette façon.\
Principe de l'algorithme : le plus grand commun divisieur (pgcd) entre deux nombres a et b est le même que celui entre b et le reste de la division euclidienne de a par b ($a\pmod b$). Algébriquement, cela donne $\text{pgcd}(a,b)=\text{pgcd}(b,a\pmod b)$.\
On a donc ainsi réduit le problème initial en un problème plus simple, ce qui permet d'appliquer la technique algorithmique **diviser pour régner**.

> Écrivez une fonction récursive `pgcd` permettant de calculer le pgcd entre deux nombres (n'oubliez pas le cas de base qu'il vous faudra déterminer).


```python
def pgcd(a,b):
    """
    pgcd(a: int,b: int) -> int
    """
    ### VOTRE CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def pgcd(a,b):
    if b == 0:
        return a
    else:
        return pgcd(b,a%b)
</pre></code>
</blockquote>
</details>


```python
pgcd(1080,480)
```
`120`

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
Une petite vidéo sur l'algorithme d'Euclide&nbsp;:<br><br>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/70jd0Mthyl8" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="YouTube Video"></iframe>
</div>
</blockquote>
</details>

Une utilité géométrique du pgcd : le pavage d'un rectangle par les plus grands  carrés possibles.


```python
ax.clear()
a = 1080
b = 480
ax.set_xlim([0, a])
ax.set_ylim([0, b])
ax.add_patch(Rectangle((0,0), a, b, color='white'))
# Le côté du plus gros carré pavant le rectangle de longueur a et largeur b vaut pgcd(a,b) !
for i in range(a//pgcd(a,b)) : # a//pgcd(a,b) : nombre de carrés dans la longueur
    for j in range(b//pgcd(a,b)) : # b//pgcd(a,b) : nombre de carrés dans la largeur
        ax.add_patch(Rectangle((pgcd(a,b)*i, pgcd(a,b)*j), pgcd(a,b), pgcd(a,b),color=couleurs[(i+j)%2]))
fig
```

![png](/euclide_paves.png)

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
Une vidéo un peu chargée sur la complexité de l'algorithme d'Euclide&nbsp;:<br><br>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/X6WnBdmNYiM" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="YouTube Video"></iframe>
</div>
</blockquote>
</details>

&nbsp;
&nbsp;


## Dessins récursifs


```python
def dessine_cercle(centre,rayon) :
    theta = np.linspace(0, 2*np.pi, 100) # permet d'avoir 100 valeurs entre 0 et 2pi
    x0,y0 = centre
    x = rayon*np.cos(theta)+x0
    y = rayon*np.sin(theta)+y0
    ax.plot(x, y)
    ax.fill(x, y)
    return fig
```


```python
ax.clear()
dessine_cercle((4,6),5) # cercle de centre (4,6) et de rayon 5
```

![png](/cerclesimple.png)


```python
def cercles(centre,rayon) :
    dessine_cercle(centre,rayon)
    if rayon > 0.1 :
        cercles(centre,rayon*0.9)
    return fig
```

```python
ax.clear()
cercles((10,10),20)
```

![png](/cerclesrecu.png)


> Définir une fonction récursive `dessin` qui affiche l'image ci-dessous avec l'appel `dessin((0,0),20)`.

![](/dessin_a_reproduire.png)

```python
def dessin(centre,rayon):
    ### VOTRE CODE
    return fig
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def dessin(centre,rayon):
    dessine_cercle(centre,rayon)
    if rayon > 1:
        x,y = centre
        dessin((x+rayon/2,y),rayon/2)
        dessin((x-rayon/2,y),rayon/2)
    return fig
</pre></code>
</blockquote>
</details>

```python
# La figure qui s'affiche en exécutant cette cellule doit être identique à l'image précédente.
ax.clear()
dessin((0,0),20)
```

&nbsp;
&nbsp;

## L-système (système de Lindenmayer)


```python
plt.rcParams['figure.figsize'] = (7, 7)
ax.clear()
```

Pour tracer une ligne brisée allant du point $\left(0;0\right)$ au point $\left(2;0\right)$ en passant par le point $\left(1;1\right)$ avec matplotlib, on peut faire l'appel suivant à `plot` :


```python
ax.plot([0, 1, 2], [0, 1, 0])
# [0, 1, 2] sont les valeurs des x
# et [0, 1, 0] sont les valeurs des y
fig
```

![png](/Linden1.png)



Comme c'est plus courant de penser en termes de coordonnées, on va construire une fonction `dessine_points` qui permet de tracer des lignes joignant une liste de points donnés sous le format `(x,y)`.

> Complétez la définition de `dessine_points` ci-dessous.

```python
def dessine_points(liste_points):
    """
    précondition: liste_points est une liste de tuples contenant chacun deux nombres (x1,y1),(x2,y2),etc.
    """
    ### VOTRE CODE
    ax.plot(X,Y)
    return fig
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def dessine_points(liste_points):
    X = [M[0] for M in liste_points]
    Y = [M[1] for M in liste_points]
    ax.plot(X,Y)
    return fig
</pre></code>
</blockquote>
</details>


```python
# les instructions suivantes doivent afficher le même graphe que plus haut.
ax.clear()
dessine_points([(0,0),(1,1),(2,0)])
```
![png](/Linden1.png)

Le "**graphisme tortue**" est un style de graphique où on commande le crayon en vue subjective ; on bouge un curseur (la tortue) sur le plan cartésien en retenant systématiquement sa position et sa direction actuelles (où est la tortue et vers où elle est tournée).

Dans la suite, on va faire en sorte de pouvoir envoyer trois ordres à la tortue codés chacun par un caractère :

- `'A'` : avance d'une certaine longueur dans ta direction actuelle
- `'+'` : tourne dans le sens des aiguilles d'une montre d'un certain angle sans avancer
- `'-'` : tourne dans le sens inverse des aiguilles d'une montre d'un certain angle sans avancer

On va donc devoir convertir une suite de consignes comme `'A+A-A+A-A'` en une liste de points.


```python
from math import pi, sin, cos
```

> Compléter la définition de `consigne_vers_points` de façon à ce que le nouveau point `(x_new,y_new)` corresponde à une tortue ayant avancé de la distance `D` dans la direction actuelle depuis `(x_old,y_old)` (il manque seulement la définition de `y_new`).


```python
def consigne_vers_points(consigne,angle):
    """
    consigne_vers_points(consigne: string) -> liste_de_points: list
    precondition: angle est donné en radian
    postcondition: liste_de_points est une liste de tuples contenant chacun deux nombres
    """
    liste_de_points = [(0,0)]  # point de départ
    D = 1                      # distance de laquelle la tortue avance à chaque F
    direction = 0              # direction initiale de la tortue (vers la droite)
    for c in consigne:
        x_old,y_old = liste_de_points[-1]
        if c == 'A':
            # création de x_new et y_new
            x_new = x_old + D*cos(direction)
            ### VOTRE CODE
            liste_de_points.append((x_new,y_new))
        elif c == '+':
            direction -= angle
        elif c == '-':
            direction += angle
    return liste_de_points
```


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Il manque la définition de <code>y_new</code>&nbsp;:<br>
<code>y_new = y_old + D*sin(direction)
</code>
</blockquote>
</details>

L'exécution des deux lignes suivantes doit afficher le graphe ci-dessous.
```python
ax.clear()
dessine_points(consigne_vers_points('A-A+A--A-A',pi/4))
```

![png](/Linden2.png)



> Donner la consigne et l'angle permettant de tracer le triangle équilatéral suivant (**votre consigne ne devra comprendre que 5 caractères !**) :
![](/trianglefractale.png)


```python
ax.clear()
consigne = '...'
angle = 0
dessine_points(consigne_vers_points(consigne,angle))
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<code>consigne = 'A-A-A'
</code><br>
<code>angle = 2*pi/3
</code>
</blockquote>
</details>

<br>

Ajoutons  un jeu de règles capables de transformer une chaîne de caractères.\
Imaginons la séquence 'abca' et les règles suivantes :

- `'a'` -> `'b'`
- `'b'` -> `'aba'`

Alors la séquence 'abca' transformée par la règle devient 'babacb' ('c' n'étant pas touché par la règle, il n'est pas modifié).

>Construisez une fonction `transformation` prenant en argumant une chaîne de caractères appelée *axiome* et une *règle* donnée sous la forme d'un dictionnaire et retournant la séquence transformée.\
Pour la règle de notre exemple, le dictionnaire serait `{'a':'b','b':'aba'}`.


```python
def transformation(axiome,regle):
    """
    transformation(axiome: string, regle: dictionnary) -> nvelle_chaine: string
    """
    ### VOTRE CODE
```

```python
axiome = 'abca'
regle = {'a':'b','b':'aba'}
transformation(axiome,regle)
```
Doit donner `'babacb'`.


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def transformation(axiome,regle):
    nvelle_chaine = ''
    for car in axiome:
        if car in regle:
            nvelle_chaine += regle[car]
        else:
            nvelle_chaine += car
    return nvelle_chaine
</pre></code>
</blockquote>
</details>


Faisons maintenant en sorte de pouvoir appliquer la transformation à elle-même : 

- si le niveau de récursivité vaut zéro, on retourne juste l'axiome, 
- sinon, on retourne le résultat de la transformation appliquée non plus sur l'axiome, mais sur la transformation de l'axiome par la règle, et on diminue le niveau d'une unité (il faut nécessairement faire en sorte d'atterrir sur le cas de base).

> Complétez la définition de la fonction ci-dessous et testez-la dans la cellule suivante (il ne manque que l'appel récursif).

```python
def transformation_recu(axiome,regle,niveau):
    """
    transformation_recu(axiome: string, regle: dictionnary, niveau: int) -> nvelle_chaine: string
    precondition: niveau doit être un entier positif !
    """
    if niveau > 0 :
        return transformation_recu(...,...,...)
    else :
        nvelle_chaine = axiome
        return nvelle_chaine
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On complète les arguments de <code>transformation_recu</code>&nbsp;:<br>
<code>
transformation_recu(transformation(axiome,regle),regle,niveau-1)
</code>
</blockquote>
</details>


```python
axiome = 'aba'
regle = {'a':'b','b':'aba'}
for i in range(6):
    print(transformation_recu(axiome,regle,i))
#doit s'afficher :
#aba
#babab
#abababababa
#babababababababababab
#abababababababababababababababababababababa
#babababababababababababababababababababababababababababababababababababababababababab
```

À partir d'un axiome, d'une règle de transformation, et de l'application récursive de la transformation sur l'axiome, on obtient une consigne permettant de faire dessiner des fractales à la tortue !

Pour le flacon de Koch, on part d'un triangle équilatéral comme axiome (construit à partir d'un angle de π/3 pour les virages de la tortue), et pour chaque segment de droite, on suit la règle de transformation représentée dans le schéma suivant.<br>


> À vous de déterminer l'axiome et la bonne règle.

![](/RegleKoch.png?width=800px)


```python
axiome = '...'
regle_Koch = {'A':'...'}
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<code>axiome = 'A--A--A'
</code><br>
<code>regle_Koch = {'A':'A+A--A+A'}
</code>
</blockquote>
</details>

```python
ax.clear()
dessine_points(consigne_vers_points(transformation_recu(axiome,regle_Koch,5),pi/3))
```

![png](/Koch.png)


Autre exemple : comment construire une surface 2D à partir d'une courbe 1D avec la courbe de Hilbert.


```python
axiome = 'L'
regle_Hilbert = {'L':'-RA+LAL+AR-','R': '+LA-RAR-AL+'}
ax.clear()
dessine_points(consigne_vers_points(transformation_recu(axiome,regle_Hilbert,6),pi/2))
```

![png](/Hilbert.png)


Autre exemple : un triangle de Sierpinski.

```python
axiome = "YA"
regle = {"X":"YA+XA+Y", "Y":"XA-YA-X"}
angle = pi/3
ax.clear()
dessine_points(consigne_vers_points(transformation_recu(axiome,regle,7),angle))
```

![png](/Sierpinski.png)


Et enfin, une jolie courbe du dragon.

```python
axiome = "AX"
regle = {"X":"X+YA+", "Y":"-AX-Y"}
angle = pi/2
ax.clear()
dessine_points(consigne_vers_points(transformation_recu(axiome,regle,16),angle))
```

![png](/courbedragon.png)


En donnant de la mémoire à la tortue, on va pouvoir dessiner des branches.\
Pour cela, il faut ajouter deux nouvelles consignes à `consigne_vers_points_branche` :

- `'['` : qui ajoute à une liste (la "mémoire"), la position actuelle de la tortue.
- `']'` : qui permet à la tortue de retourner à la dernière position en mémoire.

Voici une implémentation possible d'une fonction `consigne_vers_points_branche` intégrant ces deux nouvelles consignes :


```python
def consigne_vers_points_branche(consigne,angle):
    liste_de_points = [(0,0)]  
    D = 1                      
    direction = pi/2
    memoire = []
    for c in consigne:
        x_old,y_old = liste_de_points[-1]
        if c == 'A':
            x_new = x_old+D*cos(direction)
            y_new = y_old+D*sin(direction)
            liste_de_points.append((x_new,y_new))
        elif c == '+':
            direction -= angle
        elif c == '-':
            direction += angle
        elif c == '[':
            memoire.append(((x_old,y_old),direction))
        elif c == ']':
            souvenir = memoire.pop()
            x_new,y_new = souvenir[0]
            direction  = souvenir[1]
            liste_de_points.append((float('nan'),float('nan')))
            liste_de_points.append((x_new,y_new))
    return liste_de_points
```

```python
ax.clear()
dessine_points(consigne_vers_points_branche('A[-A]+A', pi/4))
```

![png](/Linden3.png)


> Reproduisez la figure suivante en définissant la bonne consigne et le bon angle :

```python
ax.clear(ax.clear(`ax.clear(ax.clear(`)
consigne = '...'
angle = 0
dessine_points(consigne_vers_points_branche(consigne, angle))
draw_circle = plt.Circle((0.5, 2.7), 0.3)
ax.add_artist(draw_circle)
fig
```

![](/bonhomerecu.png)

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<code>consigne = '+A[++++A]-A[A][--A]++A'
</code><br>
<code>angle = pi/6
</code>
</blockquote>
</details>


Et en utilisant la récursivité, on peut désormais dessiner de jolis arbres :


```python
axiome = 'P'
regle = {'A': 'AA', 'P': 'A[+PA-[P]--P][---P]'}
angle = pi*0.11
ax.clear()
dessine_points(consigne_vers_points_branche(transformation_recu(axiome,regle,8),angle))
```

![png](/arbrefractale.png)

![](/animfractales.gif)
