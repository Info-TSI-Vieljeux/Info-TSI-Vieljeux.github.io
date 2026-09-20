---
title: "Correction / Terminaison"
date: 2021-03-06T14:23:56+01:00
weight : 2
draft: false
---


# Prouver un algorithme

Le mot algorithme vient de la latinisation du nom du savant arabe al-Khuwārizmī (780-850) qui a entre autres permis l'introduction de l'algèbre en Europe (et il est aussi à l'origine de ce mot).

![](/1983.png?width=300)

Un algorithme est une méthode qui sert à résoudre un problème en un nombre fini d’étapes : chercher un mot dans le dictionnaire, classer des mots par ordre alphabétique, classer des nombres par ordre de grandeur, chercher le meilleur parcours possible sur une carte, trouver une racine carrée, construire des listes de nombres premiers, etc. 

On peut décrire un algorithme comme étant une **suite d'actions à accomplir séquentiellement, dans un ordre fixé**.

Pour Gérard Berry, ex titulaire de la chaire Informatique et sciences numériques au Collège de France, *__l'algorithmique est l'art d'organiser un calcul complexe en partant d'opérations simples__ (un ordinateur étant un objet extraordinairement stupide mais très obéissant)*.


Les algorithmes manipulent trois types de choses :
- des objets : bits, entiers, flottants, mots, images, etc.
- des structures de données (comment on organise les objets) : piles, listes, chaînes, arbres, etc.
- des structures de contrôle (comment on organise les opérations) : séquence, condition, boucle, etc.

  

Face à un algorithme, on peut se poser plusieurs questions :
- Est-ce qu'il donne un résultat ou bien est-ce qu’il ne s’arrête jamais ? C'est le problème de la **terminaison** d'un algorithme.
- Est-ce qu'il donne le résultat attendu ou bien est-ce qu’il calcule n’importe quoi ? C'est le problème de la **correction** de l'algorithme.
- Est-ce qu’il donne le résultat en un temps raisonnable ou bien est-ce qu’il faut attendre plusieurs siècles ? C'est le problème de la **complexité** de l'algorithme.


&nbsp;

## Terminaison d'un algorithme

Un algorithme doit se terminer en un temps fini !\
On est sûr qu'un algorithme termine si le nombre d'étapes est fixé.

Les deux énemis de la terminaison sont :
- les boucles `while`
- la récursivité

&nbsp;

#### Algorithmes itératifs :

Chez les algorithmes itératifs, notre attention se tourne exclusivement vers les boucles `while` (tant que), car ce sont les seuls blocs de code où le nombre d'étapes n'est pas fixé à l'avance et qui peuvent donc dégénerer en boucles infinies.<br>
Pour prouver leur terminaison, on exhibe un variant de boucle.

{{%notice def%}}

Un **variant de boucle** est un entier strictement positif avant l'entrée dans la boucle qui décroît strictement à chaque passage dans la boucle.

{{%/notice%}}

Trouver un variant de boucle prouve que la boucle termine, car sinon il existerait une suite décroissante d'entiers naturels, ce qui est impossible.


Exemple : preuve de la terminaison de l'__algorithme d'exponentiation rapide__


```python
def puissance(a,n):
    p = 1
    while n > 0:
        if n%2 == 0:
            a *= a
            n //= 2
        else:
            p *= a
            n -= 1
    return p
```

Si on spécifie que `n` doit être un entier positif, alors `n` est un variant de boucle. En effet :
- $n$ est bien un entier strictement positif avant chaque passage dans la boucle : $n$ est initialement un entier positif (par hypothèse) et $n$ reste entier après k passages dans la boucle (par récurrence simple). De plus, la boucle s'arrête si $n≤0$.   
- $n$ est bien strictement décroissant : en notant $n'$ la valeur de $n$ après un passage dans la boucle, si $n$ est pair avant un passage dans la boucle, on a $\displaystyle n'=\frac{n}{2}$ et comme $n≥2$, $n'<n$. Et si $n$ est impair, alors on a $n'=n-1$ et donc à nouveau $n'<n$. 

&nbsp;

#### Algorithmes récursifs :

On prouve la terminaison d'un algorithme récursif par récurrence (par construction, tout ce qui est lié aux algorithme récursifs se prouve par récurrence).

Exemple : l'algorithme récursif suivant calcul la somme des n premiers entiers.

```python
def sommerec(n):
    """
    sommerec(n: int) -> int
    préconditions: n est un entier positif
    postcondition: retourne la somme des entiers positifs ≤ n
    """
    if n == 0:
        return 0
    else:
        return n + sommerec(n-1)
````

Prouvons par récurrence sur n que l'algorithme termine :
- pour n = 0, c'est bon (cas de base).
- supposons que l'algorithme termine pour l'entrée n-1 (ie `sommerec(n-1)` termine).\
Pour l'entrée `n`, l'algorithme retourne `n + sommerec(n-1)`, donc `sommerec(n)` termine.
- conclusion : `sommerec` termine pour tout n.


&nbsp;

{{%notice info%}}
On ne peut pas prouver automatiquement l'arrêt d'un programme.\
C'est ce qu'affirme le théorème de l'arrêt : il n'existe pas de programme prenant en entrée le code d'un programme et ses arguments et qui renvoie `oui` si le programme se termine pour une certaine entrée, `non` sinon.\
La conjecture de syracuse (tp0) est un exemple de programme dont on ne sait pas s'il se termine pour une entrée quelconque.
{{%/notice%}}
&nbsp;

## Preuve de correction d’un algorithme

Ariane 501 a explosé à cause d'un bug tout petit dans un programme qui ne servait à rien.\
**Prouver la correction** d'un algorithme permet d'éviter une telle mésaventure, mais c'est difficile. Il faut pouvoir prouver qu’un programme s’exécute correctement dans toutes les situations. Mais correct selon quels critères ? Quelles situations sont à considérer ?  

Spécifier les données acceptables (les préconditions), les résultats attendus (les postconditions) et exprimer logiquement la propriété devant lier les données aux résultats (les entrées aux sorties) sont des éléments fondamentaux. Plus précisément, on prouve qu'un algorithme fait ce qu'il est sensé faire si pour toute entrée vérifiant les préconditions, il donne une sortie vérifiant les postconditions.

{{%notice def%}}
Si on prouve que pour toute donnée d'entrée qui vérifie les **préconditions**, l'algorithme renvoie des données de sortie vérifiant les **postconditions**,\
on dit qu'on a prouvé la **correction partielle** de l'algorithme.
{{%/notice %}}
{{%notice def%}}
Si on prouve en plus que l'algorithme **termine**,\
on dit qu'on a prouvé la **correction totale** de l'algorithme.
{{%/notice %}}

&nbsp;

#### Algorithmes itératifs :

Les difficultés se concentrent encore au niveau des boucles.
Pour prouver qu'une boucle fait bien son boulot, on utilise cette fois-ci un **in**variant de boucle.  

{{%notice def%}}

Un **invariant de boucle** est une propriété vraie avant le premier tour de boucle et qui se conservera pendant toute l’exécution de la boucle (donc qui restera vraie d’un tour à l’autre de la boucle), et sera toujours vraie une fois que la boucle aura fini de s’exécuter.

{{%/notice%}}

Une démonstration par invariant de boucle se déroule en 3 étapes analogues à une **preuve par récurrence** (seule la terminaison diffère) :

- Entrée de boucle = initialisation ($\rightarrow$ initialisation) :\
on démontre que juste avant de rentrer dans le premier tour de boucle l’invariant est vrai.

- Passage dans la boucle = conservation ($\rightarrow$ hérédité) :\
on suppose que l’invariant est vrai au début d’un passage quelconque dans la boucle et on démontre que l’invariant reste vrai en fin de boucle.

- Sortie de boucle = terminaison ($\rightarrow$ conclusion) :\
l’invariant est toujours vrai (car il était vrai à la fin du dernier tour de boucle) mais la condition de boucle est devenue fausse.

&nbsp;

Exemple : preuve de la correction de l'__algorithme d'Euclide__


```python
def pgcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a
```

On note $a\_k$ et $b\_k$ les valeurs de `a` et `b` à la fin de la k<sup>ème</sup> itération ($a\_0$ et $b\_0$ désignent les valeurs de `a` et `b` avant d’entrer dans la boucle).  
L'invariant de boucle est le $pgcd$ de `a` et `b`. En effet :
- *Initialisation :*\
elle est triviale puisque $a$ et $b$ n'ont pas encore été modifié ($pgcd(a\_0,b\_0)=pgcd(a,b)$). 
- *Conservation :*\
si $a=bq+r$, il est clair que tout diviseur commun de $a$ et $b$ est un diviseur commun de $b$ et $r$ et réciproquement. Notamment, $pgcd(a,b) = pgcd(b,r)$.\
Ceci prouve que $pgcd(a\_k,b\_k) = pgcd(a\_{k+1},b\_{k+1})$. La quantité $pgcd(a\_k,b\_k)$ est donc bien un invariant de boucle.   
- *Terminaison :*\
à la fin de la dernière itération (numérotée $f$), $b\_f=0$ de sorte que $pgcd(a\_0,b\_0)=pgcd(a\_f,b\_f)=pgcd(a\_f,0)=a\_f.$\
En renvoyant $a\_f$, la fonction `pgcd(a,b)` renvoie donc bien le $pgcd$ de `a` et `b`.


&nbsp;

#### Algorithmes récursifs :

La correction d'un algorithme récursif est généralement beaucoup plus simple à prouver que celle d'un itératif (c'est là une des principales qualités de la récursivité).\
En effet, la propriété transmise des préconditions aux postconditions (jouant le rôle d'invariant de boucle) est souvent évidente voire tout à fait explicite puisqu'un algorithme récursif et une preuve par récurrence ont la même structure.

Reprenons l'exemple de la somme des entiers et démontrons par récurrence sa correction :
- si n = 0, la somme vaut bien 0.
- supposons que `sommerec(n-1)` donne la somme des n-1 premiers entiers. Alors la somme des n premiers entiers vaudra `sommerec(n-1) + n` et c'est bien ce que retourne `sommerec(n)`.
- Conclusion : pour tout n, `sommerec(n)` retourne la somme des n premiers entiers.

On aurait pu se montrer plus technique en utilisant comme propriété héréditaire : $u\_n=$`sommerec(n)` $=\frac{n(n+1)}{2}$\
En supposant la propriété vraie au rang n-1, `sommerec(n)` = `n + sommerec(n-1)` $=n+u\_{n-1}$ $= n + \frac{n(n-1)}{2} = \frac{n(n+1)}{2}$

&nbsp;

### Construire un algorithme pour qu'il soit correct

Expliciter l'invariant comme on a vu dans [les bonnes pratiques](https://info-tsi-vieljeux.github.io/semestre_2/bonnes_pratiques/#commenter-son-code) en s'en servir comme guide permet de s'assurer en amont de la correction de l'algorithme ; on sait où on va.

Par exemple, pour le tri par sélection, faire en sorte que l'invariant  "*la partie de la liste déjà inspectée est triée*" soit toujours vrai nous assure de la correction future de l'algorithme ; en faisant en sorte que la partie non triée diminue bien à chaque tour, on finira fatalement par obtenir une liste entièrement triée.

Autre exemple, pour consruire les méthodes liées à la jolie structure de données appelée tas (que l'on retrouvera dans le chapitre sur les graphes), on est guidé par la conservation de l'invariant "*les clés des enfants doivent être supérieures à celles du parent*" ([voir la vidéo pour les détails](https://youtu.be/JRzTS8zPwSE)).

> *Exercice : prouver la correction totale de l'algorithme de la division euclidienne vu dans [les bonnes pratiques](https://info-tsi-vieljeux.github.io/semestre_2/bonnes_pratiques/#commenter-son-code)*.
