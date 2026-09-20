---
title: "Types de base"
date: 2021-03-06T14:23:56+01:00
weight : 2
draft: false
---



# Types de base

Les types de base en python (les catégories fondamentales des objets manipulés) sont :

- Les **entiers** `int` (en anglais, *entier* se dit *integer*).\
Exemples : 1, 2, 1012, -18 etc. 
{{% notice note%}}
Leur précision est infinie et leur taille est illimitée en Python.
{{%/notice%}}
- Les **flottants** `float`. Ce sont des approximations de nombres réels. La méthode d'écriture en machine de ces nombres, équivalente à une écriture scientifique pour nombre binaire, explique leur nom : ce sont des nombres à virgule flottante.\
Exemples : 3.58, -0.0398, 2e-7, 3e4 (les puissances de dix, notés `e` ou `E` renvoient toujours des nombres flottants).
{{% notice info%}}
**Leur précision est limitée** à 53 bits, soit **environ 16 chiffres significatifs en décimal**.
{{%/notice%}}
{{% notice warning%}}
C'est le point `.` qui sert de démarcation entre la partie entière et la partie décimale et non la virgule `,`.
{{%/notice%}}

- Les **booléens** `bool`. Ce sont des variables à deux états, `True` ou `False`, permettant de représenter des propositions logiques vraies ou fausses.

On peut **convertir d'un type en l'autre** en utilisant les fonctions natives `int()`, `float()` et `bool()`.\
Exemple :\
`>>> int(5.8)`\
`5`
{{% notice tip%}}
`int()` donne la partie entière d'un nombre flottant.
{{%/notice%}}
`>>> float(5)`\
`5.0`\
`>>> bool(0)`\
`False`\
`>>> bool(5.8)`\
`True`
{{% notice note%}}
N'importe quel nombre non nul (entier ou flottant) est considéré comme vrai.
{{%/notice%}}
&nbsp;

## Opérations sur les entiers (`int`)
Les entiers sont stables pour les opérations suivantes (le résultat est un entier).

&nbsp;

### Addition `+`

`>>> 2+3`\
`5`

&nbsp;


### Soustraction `-`

`>>> 2-3`\
`-1`

&nbsp;


### Multiplication `*`

`>>> 2*3`\
`6`

&nbsp;


### Division entière `//`
`a//b` donne le quotient de la division euclidienne de `a` par `b`.

`>>> 2//3`\
`0`
{{% notice warning%}}
Attention à ne pas confondre avec la division décimale `/`. 
{{%/notice%}}
{{% notice tip%}}
Si on travaille avec des entiers, de précision infinie, il est contre-productif d'introduire des flottants en utilisant `/` plutôt que `//`.
{{%/notice%}}

&nbsp;


### Modulo `%`
`a%b` donne le reste de la division euclidienne de `a` par `b`.

`>>> 2%3`\
`1`
{{% notice info%}}
L'opérateur modulo sert énormément en informatique, notamment pour éviter de dépasser des valeurs (`i%8` ne dépassera jamais 7, quoi que valle `i`).
{{%/notice%}}

Les opérations suivent les règles de priorité habituelles, et on utilise les parenthèses pour les modifier :\
`>>> 8//2*(2+2)`\
`16`

Que va donner `5*3%2` ?  Et `5*(3%2)` ?

&nbsp;


### Puissance `**`

`>>> 2**3`\
`8`

{{% notice note%}}
On parle aussi d'opérateur d'exponentiation.
{{%/notice%}}
{{% notice note%}}
Les puissances négatives retournent des flottants.\
`>>> 2**(-3)`\
`0.125`
{{%/notice%}}

&nbsp;

## Opérations sur les flottants (`float`)

{{% notice info%}}
Du moment qu'un des deux nombres est un flottant, les opérations `+`, `-` et `*` donnent des flottants.
{{%/notice%}}

Exemples :\
`>>> 3-1.0`\
`2.0`\
`>>> 2e-3*500`\
`1.0`\
`>>> 2**(5/2)`\
`5.656854249492381`

{{% notice warning%}}
La précision limitée des flottants et le fait qu'ils soient définis en binaire peut donner des résultats surprenants.\
Exemple :\
`>>> 3*0.1`\
`0.30000000000000004`
{{%/notice%}}

{{% notice note%}}
La division décimale `/` retourne un flottant même avec deux entiers, et même si le résultat est entier :
{{%/notice%}}

`>>> 10/5`\
`2.0`

&nbsp;

## Opérations sur les booléens (`bool`)

### Négation logique (`not`)
Sert à nier une proposition :

|  P   |  ¬P  |
| :--: | :--: |
|  F   |  V   |
|  V   |  F   |

```python
a , b = True, False
print(not a,not b)
```
`False True`

### Disjonction logique (`or`)
|  P   |  Q   | P ∨ Q |
| :--: | :--: | :---: |
|  V   |  V   |   V   |
|  V   |  F   |   V   |
|  F   |  V   |   V   |
|  F   |  F   |   F   |

```python
print(True or True,True or False,False or True, False or False)
```
`True True True False`

### Conjonction logique (`and`)
|  P   |  Q   | P ∧ Q |
| :--: | :--: | :---: |
|  V   |  V   |   V   |
|  V   |  F   |   F   |
|  F   |  V   |   F   |
|  F   |  F   |   F   |

```python
print(True and True,True and False,False and True, False and False)
```
`True False False False`

{{% notice note%}}
`not` est prioritaire devant `and` qui est prioritaire devant `or`.\
Que vaut `False or not False and True` ?
{{%/notice%}}


&nbsp;


### Caractère paresseux des opérateurs `or` et `and`
Lorsqu'on écrit `a or b`, si `a` est vrai, alors Python ne s'embête pas à évaluer `b`. Le résultat est nécessairement vrai (cf. la table de vérité), et c'est donc ce qui est retourné.
```python
True or qué_pasa
```
`True`

De même, si `a` est faux, alors `a and b` retourne `False` sans évaluer `b`.

Ce comportement peut s'avérer utile pour éviter les erreurs.\
Exemple : on veut tester si la première valeur d'une liste est positive. Appelons ce test `Test`. Si la liste est vide, l'expression `Test` va provoquer une erreur.\
On ajoute alors un deuxième test, `Test_vide`, qui n'est vrai que si la liste est vide. En utilisant l'expression `(non Test_vide) and Test`, on s'assure de ne pas lever d'erreur en cas de liste vide.

Pour en savoir plus sur l'algèbre de Boole :
{{< youtube _9nogCrIrIY>}}

&nbsp;

## Comparaisons

Les différents comparateurs utilisables en Python sont :

| comparateur |    signification    |
| :---------: | :-----------------: |
|    `==`     |       égal à        |
|    `!=`     |    différent de     |
|     `>`     |     supérieur à     |
|     `<`     |     inférieur à     |
|    `>=`     | supérieur ou égal à |
|    `<=`     | inférieur ou égal à |

Le résultat d’une comparaison est un booléen.

{{% notice warning%}}
Ne pas confondre l'opérateur d'affectation `=` et l'opérateur de comparaison `==`. 
{{%/notice%}}

{{% notice warning%}}
La précision finie des nombres flottants rend leur comparaison dangereuse :\
`0.1**2 == 0.01` retourne `False` !\
Solution : utiliser un encadrement.\
`0.1**2 > 0.01 - 1e-9 and 0.1**2 < 0.01 + 1e-9` renvoie bien `True`.
{{%/notice%}}

{{% notice note%}}
Les opérateurs de comparaison sont prioritaires devant `not`, `and` et `or`.\
Exemple : que vaut `not 7.5 < 0.9 or 4 == 4` ?
{{%/notice%}}