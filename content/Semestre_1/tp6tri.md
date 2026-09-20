---
title: "TP 6 : algorithmes de tri"
date: 2021-03-06T14:23:56+01:00
weight : 6
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
#debord
{
overflow-x: auto; 
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

# Algorithmes de tri

<p style="text-align: center;">  Cliquez sur <a href="https://classroom.github.com/a/kRMFzFeu">cette invitation</a> pour récupérer le repository du TP. </p>

![](/comptri.png)

<p style="text-align:center">
<i>Tous ces algos de tri semblent faire correctement le boulot. Qu'est-ce qui les différencie&nbsp;?</i>
</p>

<br>

Trier c'est partir d'une structure de données désordonnée et la remettre en ordre.\
Les tris sont omniprésents en informatique et Tim Roughgarden (auteur d'*Algorithms illuminated*) en parle même comme de la "*mère de tous les problèmes algorithmiques*".\
Plusieurs stratégies existent. On va en passer certaines en revue et essayer de trier les algorithmes de tri.


{{< runpython lang="vpython" mode="output" width="800" version="3.1" file="tris.py"  autorun="true"/>}}

## Tris par comparaison

La plupart des algorithmes de tri sont dits **par comparaison** car ils reposent sur des comparaisons deux à deux des éléments de la liste.

On a déjà rencontré deux algorithmes de tri par comparaison dans le TP sur la récursivité : le tri par insertion et le tri fusion.


### Tri fusion


```python
def fusion(L1,L2):
    """
    fusion(L1:list,L2:list)->Lfus:list
    fusion retourne une seule liste ordonnée à partir de deux sous-listes ordonnées
    préconditions : L1 et L2 sont triée dans l'ordre croissant
    postconditions : 'Lfus' est triée dans l'ordre croissant (et len(Lfus)==len(L1)+len(L2))
    """
    if L1 == []:
        return L2
    if L2 == []:
        return L1
    if L1[0] <= L2[0]: # devient instable si < au lieu de <= !
        return [L1[0]] + fusion(L1[1:],L2)
    else:
        return [L2[0]] + fusion(L1,L2[1:])

def tri_fusion(L):
    n = len(L)
    if n <= 1:
        return L
    else:
        return fusion(tri_fusion(L[:n//2]),tri_fusion(L[n//2:]))
```

> Combien de comparaisons entre deux éléments de la liste effectue l'algorithme de tri fusion pour ordonner `[1,2,3,4,5,6,7,8]` et `[8,7,6,5,4,3,2,1]` ? 
- A : 0 et 8
- B : 8 et 16
- C : 12 et 12
- D : 16 et 8

Vous pouvez trouver la réponse à la main, mais vous pouvez aussi intégrer à `fusion` une [**variable globale**](https://info-tsi-vieljeux.github.io/python/traitsgaux/#portée-lexicale) `nb_comp` qui est incrémentée à chaque comparaison entre deux éléments de la liste.<br>
Pensez à systématiquement réinitialiser `nb_comp` à 0 avant chaque appel de `tri_fusion`, car sinon la valeur continue à courir. C'est un des dangers de l'utilisation de variables globales dans les fonctions.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Incorporation d'un compteur de comparaisons dans <code>fusion</code>&nbsp;:
<pre><code class="language-python">def fusion(L1,L2):
    global nbcomp
    if L1 == []:
        return L2
    if L2 == []:
        return L1
    if L1[0] <= L2[0]:
        nbcomp += 1
        return [L1[0]] + fusion(L1[1:],L2)
    else:
        nbcomp += 1
        return [L2[0]] + fusion(L1,L2[1:])
nbcomp = 0
L1 = [1,2,3,4,5,6,7,8]
tri_fusion(L1)
print(f'nombre de comparaisons pour trier la liste {L1} : {nbcomp}')
nbcomp = 0
L2 = [8,7,6,5,4,3,2,1]
tri_fusion(L2)
print(f'nombre de comparaisons pour trier la liste {L2} : {nbcomp}')
</code></pre>
S'affiche alors&nbsp;:<br>
<code>nombre de comparaisons pour trier la liste [1, 2, 3, 4, 5, 6, 7, 8] : 12</code><br>
<code>nombre de comparaisons pour trier la liste [8, 7, 6, 5, 4, 3, 2, 1] : 12</code><br><br>
C'était donc la réponse C.
</blockquote>
</details>


&nbsp;
&nbsp;

### Tri par insertion

On va écrire une version itérative de l'algorithme de tri par insertion.

Son principe : on compare chacun des éléments `i` de la liste donnée en argument (à partir du deuxième) à ceux qui le précèdent en remontant la liste un par un (`i-1`,`i-2`,etc.). Tant qu'un des éléments qui précèdent est plus grand que l'élément `i`, on les permute, jusqu'à ce que l'élément `i` soit à la bonne place.

>Construisez d'abord une fonction `permute(L,i,j)` qui permute les éléments `i` et `j` d'une liste `L`.<br>


```python
def permute(L,i,j):
    """
    permute(L: list,i: int,j: int) -> None
    préconditions: 0 < i,j < len(L)
    """
    ### VOTRE CODE
```

{{%notice info%}}
On remarque que la fonction ne **retourne rien** (de manière assez paradoxale, il y a un objet python correspondant à "rien" qui s'appelle `None`), mais elle aura bien un effet sur la liste du fait de son caractère **mutable**.<br>
On dit alors que la fonction a un **effet de bord** (traduction bizarre de *side effect* qui signifie que la fonction a un effet en-dehors de son environnement local).<br>
Et pour ce qui est de la liste, on dit qu'elle a été modifiée **en place**, sans avoir eu besoin d'en créer une copie.
{{%/notice%}}

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def permute(L,i,j):
    assert -len(L) <= i < len(L) and -len(L) <= j < len(L)
    L[i], L[j] = L[j], L[i]
</code></pre>
</blockquote>
</details>

```python
# Tester tous les cas particulier auxquels vous pensez qui pourraient mettre votre fonction en défaut
L = [1,2,3]
permute(L,0,2)
L
```


>Puis complétez la fonction `tri_insertion` en utilisant `permute`.


```python
def tri_insertion(L):
    """
    tri_insertion(L: list) -> None
    """
    for i in range(1,len(L)):
        j = i
        X = L[i]
        while j > 0 and L[j-1] > X:
            ### VOTRE CODE
            j -= 1
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def tri_insertion(L):
    for i in range(1,len(L)):
        j = i
        X = L[i]
        while j > 0 and L[j-1] > X:
            permute(L,j,j-1)
            j -= 1
</code></pre>
</blockquote>
</details>

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)</summary>
<blockquote id="comm">
Comme <code>permute</code>, <code>tri_insertion</code> ne retourne rien, mais la liste est bien finalement triée.<br>
Rien ne nous empêche d'ailleurs d'ajouter un <code>return L</code> à la fin du code si on veut que la fonction retourne la liste.
</code></pre>
</blockquote>
</details>

La cellule de tests suivante permet de comparer le résultat de la fonction `tri_insertion` à la fonction native de tri `sort` sur 1000 listes de 10 nombres tirés au hasard entre -5 et 5. Si pas d'`AssertionError`, a priori votre fonction... fonctionne.


```python
from random import randint
for i in range(1000):
    L_desord = [randint(-5,5) for i in range(10)]
    L_desord_copie1 = L_desord[:] # attention à ne pas juste écrire L_desord_copie1 = L_desord (copie superficielle) !
    L_desord_copie2 = L_desord[:]
    L_desord_copie1.sort()
    tri_insertion(L_desord_copie2)
    assert L_desord_copie1==L_desord_copie2, f"y a un problème avec {L_desord} :\ndonne {L_desord_copie2}\nau lieu de {L_desord_copie1}"
```

> Combien de comparaisons entre deux éléments de la liste effectue l'algorithme de tri insertion pour ordonner `[1,2,3,4,5,6,7,8]` et `[8,7,6,5,4,3,2,1]` ? 
- A : 7 et 28
- B : 0 et 7
- C : 28 et 28
- D : 5 et 35


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Incorporation d'un compteur de comparaisons dans <code>tri_insertion</code> (on modifie un peu le code sans changer sa logique pour que le décompte soit plus évident)&nbsp;:
<pre><code class="language-python">def tri_insertion(L):
    global nbcomp
    for i in range(1,len(L)):
        j = i
        X = L[i]
        while j > 0:
            nbcomp += 1
            if L[j-1] > X:
                permute(L,j,j-1)
                j -= 1
            else:
                break
nbcomp = 0
L1 = [1,2,3,4,5,6,7,8]
tri_insertion(L1[:])
print(f'nombre de comparaisons pour trier la liste {L1} : {nbcomp}')
nbcomp = 0
L2 = [8,7,6,5,4,3,2,1]
tri_insertion(L2[:])
print(f'nombre de comparaisons pour trier la liste {L2} : {nbcomp}')
</code></pre>
S'affiche alors&nbsp;:<br>
<span style="font-family:monospace">nombre de comparaisons pour trier la liste [1, 2, 3, 4, 5, 6, 7, 8] : 7</span><br>
<span style="font-family:monospace">nombre de comparaisons pour trier la liste [8, 7, 6, 5, 4, 3, 2, 1] : 28</span><br><br>
C'était donc la réponse A.
</blockquote>
</details>

> Combien de comparaisons entre deux éléments de la liste demande le tri par insertion d'une liste de 200 éléments rangés en ordre inverse ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On est ici dans le pire des cas possibles pour <code>tri_insertion</code> (liste en ordre inversé)&nbsp;:<br>
pour la $i^e$ des $n-1$ itérations dans la boucle principale, il y a $i$ tours dans le <code>while</code> avec à chaque fois une comparaison.<br>
Le nombre de comparaisons est donc donné par&nbsp;:<br>
$\sum_{i=1}^{n-1} i = n(n-1)/2$, soit ici $200\times 199/2 = 19900$
</blockquote>
</details>

&nbsp;
&nbsp;

### Tri par sélection



Principe :  parmi les éléments de la liste, on cherche le plus petit, et on le permute avec le premier élément. Puis on recommence avec tous les éléments restants (tous moins le premier) : on cherche le plus petit et on le permute avec le deuxième élément. On recommence jusqu'à épuiser la liste

*fonction tri_selection(liste L)\
&nbsp;&nbsp;&nbsp;&nbsp;n ← longueur(L)\
&nbsp;&nbsp;&nbsp;&nbsp;pour i de 0 à n - 2\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min ← i\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pour j de i + 1 à n - 1\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;si L[j] < L[min], alors min ← j\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fin pour\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;si min ≠ i, alors échanger L[i] et L[min]\
&nbsp;&nbsp;&nbsp;&nbsp;fin pour\
fin fonction*

> Traduisez le pseudocode ci-dessus en python.

```python
def tri_selection(L):
    ### VOTRE CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def tri_selection(L):
    n = len(L)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if L[j] < L[min]:
                min = j
        if min != i:
            permute(L,i,min)</code></pre>
</blockquote>
</details>

> Combien de comparaisons entre deux éléments de la liste effectue l'algorithme de tri par sélection pour ordonner `[1,2,3,4,5,6,7,8]` et `[8,7,6,5,4,3,2,1]` ? 
- A : 7 et 28
- B : 0 et 7
- C : 28 et 28
- D : 5 et 35

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Incorporation d'un compteur de comparaisons dans <code>tri_selection</code>&nbsp;:
<pre><code class="language-python">def tri_selection(L):
    global nbcomp
    n = len(L)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            nbcomp += 1
            if L[j] < L[min]:
                min = j
        if min != i:
            permute(L,i,min)
nbcomp = 0
L1 = [1,2,3,4,5,6,7,8]
tri_selection(L1[:])
print(f'nombre de comparaisons pour trier la liste {L1} : {nbcomp}')
nbcomp = 0
L2 = [8,7,6,5,4,3,2,1]
tri_selection(L2[:])
print(f'nombre de comparaisons pour trier la liste {L2} : {nbcomp}')</code></pre>
S'affiche alors&nbsp;:<br>
<span style="font-family:monospace">nombre de comparaisons pour trier la liste [1, 2, 3, 4, 5, 6, 7, 8] : 28</span><br>
<span style="font-family:monospace">nombre de comparaisons pour trier la liste [8, 7, 6, 5, 4, 3, 2, 1] : 28</span><br><br>
C'était donc la réponse C.
</blockquote>
</details>

Le tri par sélection ressemble beaucoup au tri par insertion. Dans les deux, après k traversées de la liste, les k premiers éléments sont triés. Cependant la différence fondamentale entre les deux algorithmes est le sens dans lequel ces tris s'opèrent ; le tri par insertion trie de la fin vers le début alors que le tri par sélection trie du début vers la fin.<br>
Conséquence : dans le tri par sélection, les k premiers éléments de la liste en cours de tri sont les plus petits de la liste entière alors que dans le tri par insertion, ce sont seulement les k premiers éléments d'origine qui sont triés.

Le tri par sélection doit toujours inspecter tous les éléments restant pour trouver le plus petit, tandis que le tri par insertion ne requiert qu'une seule comparaison quand le (k+1)<sup>e</sup> élément est plus grand que le k<sup>e</sup> ; lorsque c'est fréquent (si la liste est déjà partiellement triée), le tri par insertion est bien plus efficace. En moyenne, le tri par insertion nécessite de comparer et décaler la moitié des éléments seulement, ce qui correspond donc à la moitié des comparaisons que le tri par sélection doit faire.

Dans le pire des cas pour le tri par insertion (liste triée en sens inverse), les deux tris opèrent autant d'opérations l'un que l'autre, mais le tri par insertion va nécessiter plus de permutations puisqu'il décale toujours d'une position voisine à l'autre. Le dernier élément d'une liste renversée, par exemple, va devoir traverser toute la liste en échangeant sa place avec chacun des éléments qui le précèdent, alors qu'avec le tri par sélection, il n'y a jamais au plus qu'une permutation par élément. 

En général, le tri par insertion va écrire dans la liste $O(n^2)$ fois (chaque permutation écrit dans la liste), alors que le tri par sélection va écrire seulement $O(n)$ fois. Pour cette raison, le tri par sélection peut être préférable au tri par insertion lorsque l'écriture sur la mémoire est significativement plus coûteuse que la lecture (comme sur les EEPROM ou sur les mémoires flash). Ce point est illustré dans l'animation interactive du début car limiter les permutations y correspond à limiter les déplacements, ce qui donne l'illusion d'un algorithme plus rapide.

&nbsp;
&nbsp;

### Tri à bulles

Le tri à bulles est surtout à visée pédagogique, il ne sert quasiment jamais réellement. Il tire son nom du fait qu'on pousse vers la fin de la liste, de proche en proche, des éléments de plus en plus grands, comme une bulle qui grossit en remontant à la surface.


```python
def tri_a_bulles(L):
    n = len(L)
    for i in range(n-1):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                permute(L,j,j+1)
    return L
```

> Combien de comparaisons effectue l'algorithme de tri à bulles pour ordonner `[1,2,3,4,5,6,7,8]` et `[8,7,6,5,4,3,2,1]` ? 
- A : 7 et 28
- B : 0 et 7
- C : 28 et 28
- D : 5 et 35

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Incorporation d'un compteur de comparaisons dans <code>tri_selection</code>&nbsp;:
<pre><code class="language-python">def tri_a_bulles(L):
    global nbcomp
    n = len(L)
    for i in range(n-1):
        for j in range(n-i-1):
            nbcomp += 1
            if L[j] > L[j+1]:
                permute(L,j,j+1)
nbcomp = 0
L1 = [1,2,3,4,5,6,7,8]
tri_a_bulles(L1[:])
print(f'nombre de comparaisons pour trier la liste {L1} : {nbcomp}')
nbcomp = 0
L2 = [8,7,6,5,4,3,2,1]
tri_a_bulles(L2[:])
print(f'nombre de comparaisons pour trier la liste {L2} : {nbcomp}')</code></pre>
S'affiche alors&nbsp;:<br>
<span style="font-family:monospace">nombre de comparaisons pour trier la liste [1, 2, 3, 4, 5, 6, 7, 8] : 28</span><br>
<span style="font-family:monospace">nombre de comparaisons pour trier la liste [8, 7, 6, 5, 4, 3, 2, 1] : 28</span><br><br>
C'était donc la réponse C.
</blockquote>
</details>


> Combien de comparaisons demande le tri à bulles d'une liste de 200 éléments rangés en ordre inverse  ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$19\,900$ comme pour les autres tris vus jusqu'ici.
</blockquote>
</details>

&nbsp;
&nbsp;

### Tri rapide

Le tri rapide n'est pas toujours le plus rapide... Mais il peut l'être (surtout sur les grandes listes) !<br>
C'est un algorithme récursif utilisant une partition de la liste à trier.<br>
Son avantage sur le tri fusion est d'être un tri en place.<br>
Désavantage : il est instable.

{{<youtube Cubuk-9gzvk>}}

```python
from random import randint

def partition(L, g, d):
    p = L[g]
    i = g+1
    for j in range(g+1,d+1):
        if L[j] < p:
            permute(L,i,j)
            i += 1
    permute(L,g,i-1)
    return i-1

def tri_rapide_gd(L, g, d):
    if g < d: 
        pivot = randint(g,d)
        permute(L,pivot,g)
        pivot = partition(L, g, d)
        tri_rapide(L, g, pivot-1)
        tri_rapide(L, pivot+1, d)
    return L
```

Pour ne pas s'embêter avec `g` et `d`, on peut encapsuler `tri_rapide_gd` dans une nouvelle fonction dont le seul rôle est d'initialiser `g` et `d`.

```python
def tri_rapide(L):
    g = 0
    d = len(L)-1
    tri_rapide_gd(L, g, d)
```

![](/fusrap.png)

La figure précédente permet de supposer que la complexité dans le pire des cas du tri fusion est égale à sa complexité dans le meilleur des cas et à la complexité en moyenne du tri rapide.

Sur la vidéo qui suit, des danseurs hongrois exécutent une implémentation classique du tri rapide utilisant systématiquement le premier élément comme pivot (et non un élément tiré au hasard) et où la partition marche un peu différemment : le chapeau rouge (élément comparé au pivot) est donné au voisin le plus proche du pivot et quand le pivot récupère le chapeau rouge, il est à la bonne place.

{{<youtube ywWBy6J5gz8>}}

<br>

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)</summary>
<blockquote id="comm">
<a href="https://presentationssite.github.io/info/defis/#/6">Un des défis</a> de la section <a href="https://info-tsi-vieljeux.github.io/projets/"><i>Projets</i></a> du site propose d'implémenter cette variante danse hongroise du tri rapide.<br>La fonction de partition à base de chapeau rouge et chapeau noir diffère pas mal de celle écrite plus haut.
</blockquote>
</details>


En levant la contrainte d'un tri en place, on escamote lâchement la réelle difficulté et on peut maintenant s'affranchir de la fonction de partition, ce qui permet un code bien plus court et clair.<br>
On va visualiser les différents appels récursifs d'un tel code grâce au module introduit dans le TP précédent.<br>

```python
from recursionvisualisation import viz, CallGraph
cg = CallGraph()
@viz(cg)

def triRapide(elements):
    if len(elements) <= 1:
        return elements
    else: 
        pivot = elements[0]
        plusPetit = triRapide([e for e in elements[1:] if e <= pivot])
        plusGrand = triRapide([e for e in elements[1:] if e > pivot])
        return plusPetit + [pivot] + plusGrand

print(triRapide("hanniballecter"))
cg.render()
```
<div id="debord">
<code>['a', 'a', 'b', 'c', 'e', 'e', 'h', 'i', 'l', 'l', 'n', 'n', 'r', 't']</code>
</div>

![](/hannibal.png)

Placer le pivot en premier élément a un inconvénient : `triRapide` devient très lent avec les listes déjà triées (ou quasi triées).<br>

> Quelle sera la taille de la pile d'exécution si on donne en argument à `triRapide` une liste déjà triée de 500 éléments ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$500$<br>
En effet, le pivot serait sans cesse placé en première position donnant un appel récursif sur une liste vide et l'autre sur une liste avec un élément en moins.<br>
Élément par élément, on arrive au cas de base sur le deuxième appel après avoir retiré 499 éléments, ce qui fait 500 appels avec l'appel initial.<br><br>

On peut s'en convaincre en dessinant un arbre plus petit&nbsp;:
<pre><code class="language-python">triRapide([1,2,3,4,5])
cg.render()</code></pre>
<img src="/cgrendertrirap.png">
</blockquote>
</details>


&nbsp;

***
Les tris par comparaison n'ont que faire de la nature des éléments de la liste à trier du moment qu'on peut les comparer entre eux. On peut ainsi trier tout aussi bien des chaînes de caractères que des flottants.<br>
Par contre, si les éléments de la liste sont contraints d'une façon ou d'une autre, on peut essayer de tirer parti de la situation.
***
&nbsp;
&nbsp;

## Tris non comparatifs

### Tri par dénombrement (ou par comptage)

Si la liste à trier n'est constituée que d'entiers positifs, on peut mettre au point un tri très rapide n'utilisant aucune comparaison : le tri par dénombrement (counting sort).

Principe : on construit un histogramme des valeurs de la liste à trier `L` dans une liste intermédiaire `L_eff`.
- Si `m` est la plus grande valeur des éléments de la liste à trier, alors la taille de `L_eff` doit valoir `m+1`. Et on initialise toutes ses valeurs à zéros. Chaque valeur `L[i]` de la liste à trier est donc aussi un indice de la liste `L_eff` !
- On parcourt ensuite la liste à trier et on incrémente de 1 la valeur de l'élément `L_eff[L[i]]` de la liste intermédiaire. On obtient bien ainsi les effectifs pour chaque valeur de la liste à trier.
- Il suffit enfin de parcourir `L_eff` depuis le début et pour chaque élément `L_eff[i]` non nul, d'ajouter à une nouvelle liste `L_sortie` autant de fois `i` que la valeur de `L[i]`.
- Plus qu'à retourner `L_sortie`.

>Implémentez la fonction `tri_par_denombrement` telle qu'elle est décrite ci-dessus.


```python
def tri_par_denombrement(L,m):
    """
    tri_par_denombrement(L: list,m: int) -> L_sortie: list
    m est la valeur maximum des éléments de L 
    """
    ### VOTRE CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def tri_par_denombrement(L,m):
    L_eff = [0]*(m+1) # liste des effectifs
    L_sortie = L.copy() # liste triée
    n = len(L)
    for i in range(n):
        j = L[i]
        L_eff[j] += 1
    k = 0
    for i in range(m):
        for j in range(L_eff[i]):
            L_sortie[k] = i
            k += 1
    return L_sortie
</code></pre>
</blockquote>
</details>

> Le nombre d'étapes de `tri_denombrement` peut s'écrire en fonction du nombre d'éléments `n` de la liste comme (on considérera que `m` est une constante) :
- A : $a$
- B : $a\times n + b$
- C : $a\times n^2+b\times n + c$
- D : $a\times n^3+b\times n^2 + c\times n + d$



<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$a\times n + b$
<ul>
<li>1<sup>re</sup> ligne : m+1 étapes</li>
<li>2<sup>e</sup> ligne : n étapes</li>
<li>3<sup>e</sup> ligne : 1 étape</li>
<li>4<sup>e</sup> ligne - 6<sup>e</sup> ligne (boucle <code>for</code>) : 2n étapes (2 étapes par itération)</li>
<li>7<sup>e</sup> ligne : 1 étape</li>
<li>8<sup>e</sup> ligne - 11<sup>e</sup> ligne (boucles <code>for</code> imbriquées) : 2n étapes (il y aura en tout n tours dans la boucle intérieur puisqu'on parcourt l'ensemble des effectifs et il s'y trouve deux étapes) </li>
</ul>
</blockquote>
</details>

&nbsp;
&nbsp;

## Comparer les tris

Essayons maintenant de classer ces tris suivant différents critères.<br>
Commençons par ce qui est souvent le plus critique&nbsp;: leur complexité en temps. À quoi doit-on s'attendre lorsque la taille de la liste à trier prend un facteur d'échelle&nbsp;?

### Complexité en temps

Le graphe suivant présente le temps mis par les différents algorithmes pour trier des listes de taille croissante.

![](/comptrivit1.png?width=900)
![](/comptrivit2.png?width=900)

On peut classer ces algorithmes en 3 catégories de complexité temporelle :
- les tris par insertion, sélection et à bulles sont de complexité quadratique ($O(n^2)$)
- les tris fusion et rapide sont quasilinéaires ($O(n\log n)$)
- le tri par dénombrement est linéaire ($O(n)$)

Pour des petites listes (et lorsque des tris non comparatifs ne sont pas applicables), le tri par insertion est en moyenne plus rapide que les autres alors que pour des grandes listes, c'est le tri rapide qui domine.

&nbsp;
&nbsp;

### Complexité en espace : en place ou non ?

L'algorithme a-t-il besoin d'utiliser une liste intermédiaire pour opérer son tri ou parvient-il à écrire directement sur la liste d'origine&nbsp;? Dans ce dernier cas, les tri est dit **en place**.

> Dans la liste suivante, affectez à chaque variable correspondant à un algorithme de tri le caractère `'O'` si son tri se fait en place ou `'X'` sinon.

```python
# Retirer la mauvaise réponse
triinsertion    = 'O' 'X'
tiselection     = 'O' 'X'
triabulles      = 'O' 'X'
trifusion       = 'O' 'X'
trirapide       = 'O' 'X'
tridenombrement = 'O' 'X'
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Seuls le tri fusion et le tri par dénombrement ne sont pas en place (le tri rapide l'est même si on a aussi vu une implémentation plus simple qui ne l'était pas).<br>
</blockquote>
</details>


&nbsp;
&nbsp;

### Stabilité

Un algorithme de tri est **stable** s'il conserve l'ordre relatif de départ entre deux valeurs égales.<br>
Dans l'animation suivante, un algorithme est stable si les deux barres noires et blanches restent toujours dans le même ordre après et avant le tri.

{{< runpython lang="vpython" mode="output"  width="800" version="3.1" file="tristable.py"  autorun="true"/>}}

On compte le nombre de fois que les caractères 'r', 'c', 'q' et 'p' apparaissent dans cette phrase&nbsp;:
- 'r' : 6
- 'c' : 5
- 'q' : 2
- 'p' : 5

On crée à partir de ces données le tuple `(('r',6),('c',5),('q',2),('p',5))`.<br>
Si on trie ce tuple selon le premier élément de chacune des paires qu'il contient (tri alphabétique), tous les tris donnent le même résultat :<br>
`(('c',5),('p',5),('q',2),('r',6))`<br>
Mais si maintenant, on part de ce tuple trié et qu'on le trie en fonction des effectifs, les algorithmes ne sont pas tous d'accords !

Pour vous en convaincre, triez à la main `(('c',5),('p',5),('q',2),('r',6))` selon le deuxième élément de chacun des tuples en suivant l'algorithme du tri à bulle, puis en suivant l'algorithme de tri sélection.<br>
Notez ci-dessous les tuples obtenus.

```python
# tuple obtenu avec le tri à bulle (modifiez le tuple pour qu'il corresponde à ce que vous avez trouvé)
T1 = (('c',5),('p',5),('q',2),('r',6))
# tuple obtenu avec le tri sélection (modifiez le tuple pour qu'il corresponde à ce que vous avez trouvé)
T2 = (('c',5),('p',5),('q',2),('r',6))
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python"># tuple obtenu avec le tri à bulle (modifiez le tuple pour qu'il corresponde à ce que vous avez trouvé)
T1 = (('q',2),('c',5),('p',5),('r',6))
# tuple obtenu avec le tri sélection (modifiez le tuple pour qu'il corresponde à ce que vous avez trouvé)
T2 = (('q',2),('p',5),('c',5),('r',6))
</code></pre>
Le tri sélection a donc permuté l'ordre initiale initial entre <code>(p,5)</code> et <code>(c,5)</code> alors que le tri à bulles l'a conservé.
</blockquote>
</details>

On dit alors que le tri sélection n'est pas stable car il ne conserve pas nécessairement l'ordre de deux éléments égaux.<br>
- tris instables : le tri sélection et le tri rapide.<br>
- tris stables : le tri insertion, le tri à bulle et le tri fusion

Un tri instable peut sans trop de peine être rendu stable, il suffit de garder la trace de l'ordre initial pour les éléments égaux, mais cela a un coût !<br>
L'instabilité du tri par sélection peut être éliminée en utilisant une fonction intermédiaire `minimum` cherchant l'indice du plus petit des éléments restant à trier et en ajoutant successivement les éléments trouvés dans une nouvelle liste tout en les retirant de la première liste (on détricote la liste de départ pour retricoter à l'endroit la liste triée). 
Mais l'algorithme n'est alors plus en place ! On a troqué l'instabilité contre de la place mémoire.

> Donnez le code de `minimum` et `tri_selection_stable` (avec une contrainte supplémentaire : le bloc de code de `tri_selection_stable` ne devra pas dépasser 4 lignes). Pour retirer un élément d'une liste, vous pouvez regarder [ici](https://info-tsi-vieljeux.github.io/python/typesstruct/#retirer-un-élément).

```python
def minimum(L):
    """
    minimum(L: list) -> imin: int
    imin est l'indice du plus petit élément de la liste
    et s'il y a plusieurs minimaux, imin est le plus petit des indices
    """
    ### VOTRE CODE

# le bloc de code de tri_selection_stable ne devra pas dépasser 4 lignes pour être considéré comme juste.
    
def tri_selection_stable(L) :
    ### VOTRE CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def minimum(L):
    imin = 0
    for i in range(1,len(L)):
        if L[i] < L[imin]:
            imin = i
    return imin
</code></pre>
<pre><code class="language-python">def tri_selection_stable(L):
    L_sortie = []
    for i in range(len(L)):
        L_sortie.append(L.pop(minimum(L)))
    return L_sortie
</code></pre>
On pouvait réduire à 2 lignes avec une construction par compréhension de <code>L_sortie</code>.
</blockquote>
</details>



![](https://imgs.xkcd.com/comics/ineffective_sorts.png)


<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)</summary>
<blockquote id="comm">
Il existe <a href="https://www.explainxkcd.com/wiki/index.php/1185:_Ineffective_Sorts">un wiki</a> dédié à l'explication des dessins de <a href="https://xkcd.com">xkcd</a>.
</code></pre>
</blockquote>
</details>