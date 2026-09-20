---
title: "Strucutres de contrôle"
date: 2021-03-06T14:23:56+01:00
weight : 4
draft: false
---


# Structures de contrôle

## Instruction d'affectation

### Définition

Lorsqu'un objet est créé dans un programme Python, une certaine place en mémoire lui est allouée. Cette place est repérée par une adresse dont la valeur peut être obtenue grâce à la fonction `id()`.


```python
id(3.7)
```

`4387417928`

Il est beaucoup plus pratique de pouvoir récupérer une valeur en mémoire grâce à un petit nom plutôt que par son adresse. C'est à ça que servent les variables. Une variable est liée à un objet grâce à une **affectation** et identifie cet objet pour les calculs suivants. Une affectation est une instruction (pas de retour).

En Python, une affectation s'opère avec le symbole `=`.

{{% notice note%}} 
En pseudocode, on utilise généralement `:=` ou `←` pour les affectations.
{{% /notice %}}

La variable est un tiroir avec une étiquette. Et comme on l'a vu, en Python, pas besoin de choisir un tiroir correspondant au type d'objet qu'il va contenir, c'est l'interpréteur qui s'en charge pour nous (le typage est dynamique).

![](/variable0.png?width=500px)

![](/variable1.png?width=500px)


```python
a = 3
b = -2
a * b
```
`-6`

Si on veut pouvoir utiliser le résultat de `a * b` pour des calculs ultérieurs, il faut lui aussi le stocker en mémoire.


```python
c = a * b
c
```
`-6`

On peut interroger le type d'une variable avec la fonction `type()` :  

```python
c = 3,2
type(c)
```
`<class 'tuple'>`

&nbsp;

### Instruction plutôt qu'expression

Le fait que l'affectation soir une instruction plutôt qu'une expression est un choix d'écriture du langage (en C, l'affectation est une expression).\
D'ailleurs, Python 3.8 a introduit l'opérateur `:=` (dit le *walrus opérator* ou *opérateur de morse* du fait de sa ressemblance à un morse...) permettant justement une **expression d'affectation** au sein d'une expression plus large. L'intérêt est de permettre de raccourcir l'écriture ou d'éviter les répétitions dans certains cas.\
L'opérateur de morse n'est pas à connaître, mais il va nous permettre, dans les deux exemples suivants, de bien faire la différence entre une instruction et une expression.

```Python
if (n := len(a)) > 5:
    print(f"La liste est trop grande ({n} élements alors qu'on en attend 5 au plus)")
```
>Montrer que sans `:=`, on aurait soit une répétition, soit une ligne en plus.

Autre exemple :
```Python
while (choix := input('Entrer q ou p : ')) != 'q':
    if choix == 'p':
        print("Salut !")
```
>Comment aurait-on dû écrire ce code sans `:=` ?

&nbsp;

### Réaffectation

Une affectation ne retourne rien mais a un effet sur la mémoire : l'adresse de la variable est modifiée à chaque nouvelle affectation. C'est ce qui rend possible les **réaffectations** à partir de la variable elle-même.

```python
id(a)
```
`4304751488`

```python
id(a+1)
```
`4304751520`

```python
a = a + 1
id(a)
```
`4304751520`

{{% notice info%}}
Ces types de **réaffectation** sont si fréquents qu'il existe une notation raccourcie : `+=`, `-=`, `*=`, `/=`, `//=`, `%=`.\
Ainsi, `a += 1` équivaut à `a = a + 1` et `b /= 5` équivaut à `b = b/5`.
{{%/notice%}}

&nbsp;

### Affectation parallèle

Comment faire si on veut permuter les valeurs auxquelles sont liées deux variables ? Dès qu'on écrit `a = b`, la valeur initiale de `a` est perdue. Et si on commence par `b = a`, c'est la valeur initiale de `b` qui est perdue. Il faudrait donc utiliser une variable temporaire et écrire : `tmp = a`, `a = b` et `b = tmp`.\
Mais l'affectation parallèle de Python va nous permettre d'être plus élégants. Il suffit en effet d'une petite ligne :

```python
a = 'haut'
b = 'bas'
a , b = b , a
print(a,b)
```
`bas haut`

{{% notice info %}} 
**L'affectation parallèle** repose sur le **dépaquetage (*unpacking*) de tuples**.\
En effet, des objets séparés par des virgules forment un tuple (pas besoin de parenthèses). Donc `a,b,c = 1,2,3` correspond au dépaquetage du tuple `(1,2,3)` sur les 3 variables `a`, `b` et `c`.
{{% /notice %}} 

&nbsp;

### Noms de variable

Règles sur les noms de variables :

- ils sont sensibles à la casse (minuscule ou majuscule)
- ils peuvent contenir n'importe quelles lettres ou chiffres et le tiret-bas "_" mais ne doivent pas commencer par un chiffre.
- certains noms sont interdits (attention en particulier à lambda) :

`and`  `assert`  `break`  `class`  `continue`  `def`  `del`  `elif`  `else`  `except`  `finally`  `for`  `from`  `global`  `if` \
`import`  `in`  `is`  `lambda`  `nonlocal`  `not`  `or`  `pass`  `print`  `raise`  `return`  `try`  `while`  `yield`



{{% notice warning%}} 

Il est important pour la lisibilité de son code de donner les noms les plus explicites possibles aux variables. Les rapports de jury le répète tous les ans... {{% /notice %}}

Rapport 2019 de l'épreuve de Centrale par exemple :

>**Des noms de variables explicites aident à la compréhension du code. De trop nombreux candidats utilisent des noms de variables quelconques (a, b, c...) ce qui nuit à la compréhension du programme. La clarté du programme (en particulier le choix des noms de variables) ainsi que la présence de commentaires opportuns sont prises en compte dans l’évaluation.**

&nbsp;

## Instuction conditionnelle

Les instructions conditionnelles permettent de rediriger le flot d'exécution d'un programme en proposant des alternatives.

### `if`,`elif`,`else`

La structure `if ... elif ... else` permet d'exécuter des instructions seulement si une condition, donnée par le résultat d'un ou plusieurs tests logiques, est vérifiée. 

`if` <*expression logique 1*> :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<*bloc d'instructions 1*>  
`elif` <*expression logique 2*> :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<*bloc d'instructions 2*>  
**...**  
`else` :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<*bloc d'instructions*>

Si l'<*expression&nbsp;logique&nbsp;1*> est évaluée comme vraie, le <*bloc&nbsp;d'instructions&nbsp;1*> est exécuté ; dans le cas contraire, si l'<*expression logique&nbsp;2*> est évaluée comme vraie, le <*bloc&nbsp;d'instructions&nbsp;2*> est exécuté, et ainsi de suite&nbsp;; et si aucune des expressions logiques précédentes n'est vraie, le bloc d'instructions faisant suite au `else:` est exécuté.

Par exemple :


```python
for x in range(10):
    if x<= 3:
        print(x,'est inférieur ou égal à 3')
    elif x > 5:
        print(x,'est plus grand que 5')
    else:
        print(x,'doit être 4 ou 5')
```

    0 est inférieur ou égal à 3
    1 est inférieur ou égal à 3
    2 est inférieur ou égal à 3
    3 est inférieur ou égal à 3
    4 doit être 4 ou 5
    5 doit être 4 ou 5
    6 est plus grand que 5
    7 est plus grand que 5
    8 est plus grand que 5
    9 est plus grand que 5

{{%notice note%}}

Python reconnaît comme vrai n'importe quel type de donnée (même pas besoin d'expression logique) du moment qu'il ne s'agit ni de l'entier `0`, du décimal `0.`, de la chaîne de caractères vide `''`, du tuple vide `()`, de la liste vide `[]`, ou encore de la valeur `None`. 

{{% / notice %}}


Exemple :  
Dans le calendrier grégorien, une année est bissextile si elle est divisible par 4 sauf si elle est aussi divisible par 100 à l'exception des années divisibles par 400 qui sont bien bissextiles.  
Le programme suivant détermine si une année est bissextile :


```python
année = 2022
if not année % 400:
    est_bissextile = True
elif not année % 100:
    est_bissextile = False
elif not année % 4:
    est_bissextile = True
else:
    est_bissextile = False
s = 'est une' if est_bissextile else "n'est pas une"
print("L'année", année , s ,"année bissextile.")
```

`L'année 2022 n'est pas une année bissextile.`



&nbsp;

&nbsp;



## Boucle `while`

Une boucle `while` ou "tant que" permet de répéter une suite d'instructions *tant qu'* une condition est respectée.\
La suite d'instructions répétées devra être indentée et forme alors le corps de la boucle.

{{%notice warning%}}

Les boucles `while` sont dangereuses ! Rien ne dit en effet que la condition sera un jour fausse et la boucle peut donc tourner indéfiniment.\
Les boucles infinis posent le problème de la terminaison d'un programme.

{{% / notice %}}

```python
i = 0
while i < 10:
    i += 1
    print(i,end ='.')
print('\nLa boucle est finie...')
```
    1.2.3.4.5.6.7.8.9.10.
    La boucle est finie...

Le compteur `i` est initialisé à `0` et comme `0` est inférieur à `10`, la boucle `while` démarre. À chaque itération, `i` est incrémenté de `1` et sa valeur affichée. Puis `i` atteint `10` et à l'itération suivante `i < 10` devient faux, la boucle s'arrête et l'éxécution reprend après la boucle.  

Un exemple plus intéressant :\
implémentons l'algorithme d'Euclide permettant de déterminer le plus grand diviseur commun de deux entiers.


```python
a , b = 1920 , 1080
print(f'pgcd({a},{b}) = ',end = '')
while b:
    a , b = b, a % b
print(a)
```
`pgcd(1920,1080) = 120`

La boucle continue jusqu'à ce que `b` divise `a`. À chaque itération, `b` prend la valeur du reste de la division euclidienne de `a` par `b` et `a` prend l'ancienne valeur de `b`.\
`while b` est équivalent à `while b != 0` puisque la valeur `0` est évaluée comme fausse.

&nbsp;


### `break`

L'instruction `break`, placée dans le bloc d'instructions d'une boucle, met immédiatement fin à cette boucle lorsqu'arrive son tour d'être exécutée.  
L'exécution reprend à l'instruction suivant la boucle.  


```python
x = 0
while True:
    x += 1
    if not (x % 15 or x % 25):
        break
print(x,'est divisible à la fois par 15 et 25.')
```

`75 est divisible à la fois par 15 et 25.`

La condition du `while` est ici littéralement toujours vraie donc la seule sortie possible de la boucle passe par une exécution de l'instruction `break`, ce qui ne peut arriver que si `x` est à la fois divisible par 15 et 25 (c'est une pratique risquée !).



De la même manière, pour trouver l'indice de la première occurrence d'un nombre négatif dans une liste :


```python
liste = [5, 2, 99, 0, 100, -2, 37, 43, -124]
for i, a in enumerate(liste):
    if a < 0:
        break
print("L'élément d'indice",i,"valant",a,"est le premier élément négatif.")
```

`L'élément d'indice 5 valant -2 est le premier élément négatif.`

{{%notice note%}}

Après la sortie de la boucle, les variables `i` et `a` gardent les valeurs qu'elles ont au moment de l'instruction `break`. 

{{%/ notice%}}

&nbsp;

### `return`

L'instruction `return` permet elle aussi de s'échapper d'une boucle.

En effet, l'utilisation du `return` a pour effet de sortir du corps d'une fonction donc à fortiori, si une boucle est utilisée dans la définition de cette fonction, le `return` permet aussi d'en sortir.

```python
def vol(i):
    t = 0
    while(1):
        if not i%2:
            i //= 2
        elif i != 1:
            i = 3*i+1
        else:
            return t
        t += 1
```
`vol(27)` renvoie alors `111`.

&nbsp;

&nbsp;

## Boucle `for`

Une boucle `for` se différencie d'une boucle `while` en ce que le nombre d'itérations est connu à l'avance.

La structure d'une telle boucle est en effet :

`for` <*élément*> `in` <*itérable*>  :\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<*bloc d'instructions*>

L'itérable est une collection d'éléments et le bloc d'instructions est alors répété autant de fois que l'itérable contient d'éléments.

Passons en revue quelques itérables.

### `range`

`range` permet d'itérer sur une suite arithmétique d'entiers :

```python
for i in range(5):
	print(i,end=".")
```
`0.1.2.3.4.`

{{% notice warning %}}
L'itération sur `range(n)` va de $0$ à $n-1$ par pas de 1.
{{%/ notice%}}

On peut spécifier un point de départ et un pas différents en les passant en argument : `range(depart,fin,pas)`.

```python
for i in range(5,10):
	print(i,end=".")
```
`5.6.7.8.9.`

```python
for i in range(0,100,20):
	print(i,end=".")
```
`0.20.40.60.80.`

&nbsp;

### une chaîne de caractères

Itérer sur une chaîne de caractères  décompose la chaîne caractère par caractère :

```python
for car in 'abc😱':
	print(car*2,end=' ')
```
`aa bb cc 😱😱 `

&nbsp;

### une liste, un tuple

On peut de même parcourir une liste ou un tuple élément par élément.

```python
L = [('🙈','🙊','🙉'),('🌖','🌗','🌘'),]
s = ''
i = 1
for tuple in L:
	for element in tuple:
		s += element*i
		i += 1
print(s)
```
`🙈🙊🙊🙉🙉🙉🌖🌖🌖🌖🌗🌗🌗🌗🌗🌘🌘🌘🌘🌘🌘`

&nbsp;

### un dictionnaire

Pour pacourir uniquement les clés d'un dictionnaire, on peut utiliser la méthode `keys` : 

```python
Dico = {'pwd_1' : '123456', 'pwd_2' : 'qwerty', 'pwd_3' : 'password'}
for cle in Dico.keys():
    print(cle,'->',Dico[cle])
```
`pwd_1 -> 123456`\
`pwd_2 -> qwerty`\
`pwd_3 -> password`

Et grâce à la méthode `items`, on peut déballer clés et valeurs associées dans un tuple :

```python
for cle,valeur in Dico.items():
    print(cle,'->',valeur)
```
`pwd_1 -> 123456`\
`pwd_2 -> qwerty`\
`pwd_3 -> password`

Construisons par exemple un nouveau dictionnaire inversant clés et valeurs :

```python
Dico = {'$' : 'dollar', '€' : 'euro', '¥' : 'yen', '£' : 'livre'}
Dico_inv = {}
for cle,valeur in Dico.items():
    Dico_inv[valeur] = cle
print(Dico_inv)
```
`{'dollar': '$', 'euro': '€', 'yen': '¥', 'livre': '£'}`

Dernier exemple, modifions une à une chaque valeur d'un dictionnaire  :
```python
dico_notes = {'Kurt' : 19, 'Kris' : 11, 'Dave' : 13, 'Pat' : 10, 'Courtney' : 15}
for eleve,note in dico_notes.items():
    dico_notes[eleve] = note+1
print(dico_notes)
```
`{'Kurt': 20, 'Kris': 12, 'Dave': 14, 'Pat': 11, 'Courtney': 16}`
&nbsp;

&nbsp;

## Définition d'une fonction

Une fonction est un ensemble d'instructions auxquelles on accède par un raccourci : le nom de la fonction. Elles se comportent comme des sous-programmes à l'intérieur du programme principal. Et comme tout programme, elles peuvent agir sur des données, les entrées, et fournir de nouvelles données, les sorties.

La signature d'une fonction résume ces points clés : son nom, les différents arguments et leurs types, les différentes sorties et leur type.
`nom(arg_1:type, arg_2:type, etc) -> sortie_1:type, sortie_2:type, etc`

On **définit une fonction** grâce au mot clé `def` en suivant la structure suivante :

>`def` nom`(`arguments séparés par des virgules`)` `:`\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;< *corps de la fonction contenant les différentes instructions* >

La définition d'une fonction est une instruction.

```python
def addition(a,b):
		c = a+b
		print(c)
```
On appelle une fonction en utilisant son nom et en affectant chaque argument dans les parenthèses qui suivent son nom.\
Les instructions du corps de la fonction sont alors exécutée une par une et si des variables correspondant aux nom des arguments (on parle alors d'*arguments formels*) sont rencontrées, ce sont les valeurs utilisées lors de l'appel (les *arguments effectifs*) qui les remplacent.

```python
addition(5,2)
```
`7`
{{% notice note%}}
On utilise aussi le terme "paramètre" pour désigner les arguments formels, c'est-à-dire les variables qui entrent dans la définition de la fonction. Et on réserve alors le terme argument aux valeurs données à ces variables au moment de l'appel.\
Dans l'exemple, `a` et `b` sont alors les paramètres (= arguments formels) et `5` et `2` sont les arguments (= arguments effectifs).
{{%/notice%}}

{{% notice warning%}} 
Malgré ce que l'affichage peut laisser croire, la fonction précédente ne retourne rien !\
La valeur de `c` est prisonnière du corps de la fonction, elle n'est pas accessible dans le code principal. C'est une **variable locale**.\
Si on veut pouvoir accéder à `c` ailleurs que dans la fonction, il faut l'extirper en utilisant un `return`.\
Il ne faut ainsi pas confondre  `print` et  `return` !\
Le `return` transforme l'appel de la fonction en expression puisqu'une valeur est retournée.\
Le `print` n'a qu'un **effet de bord**. La valeur est affichée mais inutilisable. L'appel de la fonction n'est alors qu'une instruction et on nomme *procédure* une telle fonction. 
{{%/notice%}}


Ainsi, `addition(5,2) + 7` va lever une erreur : `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`.\
En effet, comme `addition` ne retourne rien, Python la considère de type `NoneType` et ne comprend  pas pourquoi on cherche à additionner quelque chose à rien.

Arrangeons cela grâce à un `return` :
```python
def addition(a,b):
		c = a+b
		return c
```
Maintenant, `addition(5,2) + 7` retourne gentiment 12.

Dès que l'instruction `return` est rencontrée lors de l'appel de la fonction le flot d'exécution du code de la fonction est interrompu et reprend à la ligne suivant l'appel.

```python
def demo():
		print("Ligne exécutée car avant le return")
		return
		print("Ligne non exécutée car après le return")
demo()
```
`Ligne exécutée car avant le return`

L'exemple précédent nous montre aussi qu'une fonction n'a pas nécessairement d'argument et qu'un `return` peut ne rien retourner (il ne sert alors qu'à interrompre l'exécution).

Comme on l'a vu précédemment, un `return`, à l'instar d'un `break`, peut donc interrompre une boucle dans le corps d'une fonction.

L'appel d'une fonction *est* la valeur qu'elle retourne, qu'il s'agisse d'un entier, d'une liste, d'un dictionnaire, etc.\
Une fonction peut retourner plusieurs variables séparées par des virgules. L'appel est alors un tuple qui peut être déballé.
```python
def somme_moyenne(liste):
		s = 0
		for e in liste:
				s += e
		m = s/len(liste)
		return s,m
L = [1,2,3,4]
print(type(somme_moyenne(L)))
a,b = somme_moyenne(L)
print("somme :",a,"et moyenne :",b)
print(somme_moyenne(L)[1])
```
`<class 'tuple'>`\
`somme : 10 et moyenne : 2.5`\
`2.5`


Une fonction peut aussi ne pas avoir d'argument :
```python
def HelloWorld():
    print('\x4B\x49\x4C\x4C\n\x41\x4C\x4C\n\x48\x55\x4D\x41\x4E')
```