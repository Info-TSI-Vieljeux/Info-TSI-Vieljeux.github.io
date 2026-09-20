---
title: "Divers"
chapter : false
date: 2021-03-06T14:23:56+01:00
weight : 0
draft: false
---



# Divers

## Commentaires

Tous les langages de programmations permettent d'introduire des commentaires dans le code qui servent d'aides et de repères à celui qui lit le code, mais qui sont ignorés lors de l'exécution.

En Python, les commentaires sont introduits par le symbole dièse (hashtag) `#`.


&nbsp;
&nbsp;


## Utilisation de print

`print` est la première fonction native que l'on rencontre. C'est une fonction à effet de bord :  elle ne retourne rien (elle est de type `None`), mais elle permet d'afficher une chaîne de caractères, ou le contenu d'une variable, quel que soit son type.

```python
nom = 'Joe'
age = 212
print(nom,'a',age,'ans.')
```
`Joe a 212 ans.`

De plus, `print` affiche par défaut un retour à la ligne.

Les **caractères d'échapement** font partie de la chaîne de caractères, mais sont interprétés par `print` comme des commandes. Le plus utilisé est le retour à la ligne `\n`.
```python
print("a\nb\nc")
```
`a`\
`b`\
`c`

Bien que non exigible, l'utilisation des *f-strings*, introduites depuis Python 3.6, peut s'avérer très pratique. Les f-strings permettent d'inserrer des variables dans des chaînes de caractères et de les mettre en forme avec une syntaxe minimale.

Pour les utiliser, il suffit de mettre un `f` devant la chaîne de caractères et de placer chaque variable entre accolade.

```python
print(f'{nom} a {age} ans.')
print(f'{nom = }, {age = }) # très pratique pour les jeux de tests
```
`Joe a 212 ans.`\
`nom = 'Joe', age = 212`


&nbsp;
&nbsp;


## Importation de modules

### `import module`
Pour importer le module `machin`, il suffit d'écrire `import machin`. Chaque fonction contenue dans le module devra alors être applée en utilisant la notation point : `machin.fonction` (le point désigne ici une relation d'appartenance caractéristique de la programmation orientée objet).

```python
import math
print(f'{math.sqrt(2) = }')
```
`math.sqrt(2) = 1.4142135623730951`

&nbsp;
&nbsp;

### `import module as X`
Lorsqu'on utilise fréquemment un module, il est pratique d'abréger son nom.  Pour cela, on ajoute le raccourci souhaité après un `as` lors de l'import : `import machin as mch`. 

```python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi,np.pi,100)
Y = np.sin(X)
plt.plot(X,Y)
```
![](/sin.png)

&nbsp;
&nbsp;


### `from module import x,y`

On peut aussi  récupérer uniquement certaines fonctions ou variables d'un module afin d'y avoir accès directement (sans utiliser `machin.`).

```python
from math import pi,cos
print(f'{cos(pi) = }')
````
`cos(pi) = -1.0`

&nbsp;
&nbsp;


### `from module import *`

Lorsqu'on est sûr que cela ne va pas poser problème, on peut importer tout le contenu du module de la même manière. On utilise alors l'étoile `*` qui signifie "tout".\
**Ce type d'import est néanmoins déconseillé** à moins de très bien connaître le contenu du module. Le danger est que dans l'ensemble de ce qui est importé, il peut se trouver des variables ou des fonctions ayant un nom déjà attribué. L'import réaffectera alors ces variables contre notre gré et sans nous le dire.

```python
d = 8
e = 2
from math import *
print(sqrt(d ** e))
```
`16.88210319127114`

&nbsp;
&nbsp;


## Manipulation de fichier texte

### Ouvrir et fermer un fichier

Un objet `file` est créé par l'utilisation de la fonction `open(nom du fichier,mode)` qui prend deux arguments.  


```python
f = open('monfichier.txt','w')
```

- Le premier argument, *nom du fichier*, est une chaîne contenant le nom du fichier. Ce nom peut être donné avec le chemin d'accès absolu ou seulement l'arborescence relative au dossier dans lequel le programme est exécuté. \
En écrivant un nom sans chemin, le fichier se trouve dans le répertoire courant.

- Le deuxième argument, *mode*, est une chaîne d'un ou deux caractères décrivant la façon dont le fichier est utilisé.  
  *mode* peut être `r` quand le fichier n'est accédé qu'en lecture, `w` en écriture seulement (un fichier existant portant le même nom sera alors écrasé) 
  et `a` ouvre le fichier en mode ajout (toute donnée écrite dans le fichier est automatiquement ajoutée à la fin). `r+` ouvre le fichier en mode lecture/écriture. L'argument mode est optionnel, sa valeur par défaut est `r`.  
  `b` collé à la fin du mode indique que le fichier doit être ouvert en mode binaire c'est-à-dire que les données sont lues et écrites sous forme d'octets (type bytes). 
  Ce mode est à utiliser pour les fichiers contenant autre chose que du texte.

Les objets `file` sont fermés grâce à la méthode `close()` : `f.close()` par exemple. Python ferme les fichiers automatiquement lorsque le programme se termine.

&nbsp;
&nbsp;

### Écrire dans un fichier {#ecrire}

La méthode `write()` d'un objet `file` écrit une chaîne de caractères dans le fichier et renvoie le nombre de caractères inscrits. 


```python
f.write('Coucou monde !')
```
`14`

Plus pratique, la fonction native `print()` peut accepter en argument un objet `file`. Plutôt que d'être affichée sur le shell, la sortie de `print()` est alors redirigée vers ce fichier.

```python
print('\nKill all humans', file=f)
f.close()
```

Exemple : le programme suivant écrit les quatre premières puissances de tous les entiers entre 1 et 1000, chaque champ étant séparé par une virgule, dans le fichier puissances.txt.


```python
fi = open('puissances.txt','w')
for i in range(1,1001):
    print(i, i**2, i**3, i**4, sep=', ', file=fi)
fi.close()
```

&nbsp;
&nbsp;

### Lire un fichier

Pour lire `n` bytes d'un fichier, on utilise `f.read(n)`. En omettant `n`, tout le fichier est lu. \
`readline()` lit une seule ligne d'un fichier jusqu'au, en l'incluant, caractère `\n` de nouvelle ligne. Un nouvel appel de `readline()` lit la ligne suivante et ainsi de suite.\
`read()` et `readline()` renvoie toutes les deux une chaîne vide lorsque la fin du fichier est atteinte.  
Pour lire en une fois toutes les lignes dans une liste de chaînes, on utilise `f.readlines()`.

Les objet `file` sont itérables. On peut ainsi retourner chaque ligne d'un fichier une à une en utilisant une boucle :


```python
f = open('monfichier.txt')
for ligne in f:
    print(ligne, end='')
f.close()
```

`Coucou monde !`\
`.`\
`.`\
`.`\
`Kill all humans`


Comme `ligne` contient déjà le caractère de nouvelle ligne lorsqu'elle est lue, on utilise `end = ''` pour empêcher `print` d'en ajouter un autre.  
Cette méthode de lecture ligne à ligne est à privilégier pour les gros fichiers à moins de vraiment vouloir contenir en mémoire l'ensemble du fichier.

Grâce à la méthode `split`, on peut transformer un texte en une liste de ces éléments. L’argument de split correspond aux caractères utilisés comme séparateur. Par défaut il s’agit du caractère d’espacement `' '` (si on veut découper un texte en paragraphe, on utilisera le caractère d’échappement de retour à la ligne `\n`).

```python
fo = open('monfichier.txt')
texte = fo.read()
liste1 = texte.split('\n')
liste2 = texte.split()
print(liste1)
print(liste2)
fo.close()
```
`['Coucou monde !', '.', '.', '.', 'Kill all humans']`\
`['Coucou', 'monde', '!', '.', '.', '.', 'Kill', 'all', 'humans']`

Pour lire les nombres du fichier `'puissance.txt'` écrit précédemment, les colonnes doivent être converties en une liste d'entiers.  
Pour cela, chaque ligne doit être décomposée en ses différents champs et chaque champ explicitement converti en entier grâce à `int()` :


```python
fo = open('puissances.txt')
carrés, cubes, puiss4 = [],[],[]
lignes = fo.readlines()
fo.close()
for ligne in lignes:
    champs = ligne.split(',')
    carrés.append(int(champs[1]))
    cubes.append(int(champs[2]))
    puiss4.append(int(champs[3]))
n = 500
print(n, 'au cube vaut', cubes[n-1])
```
`500 au cube vaut 125000000`

{{%notice note%}}

Mais en pratique, il vaut mieux utiliser les bibliothèques NumPy ou Pandas pour des fichiers de données comme celui-ci.\
Vous apprendrez aussi au 3<sup>e</sup> trimestre à utiliser les méthodes des *bases de données*.

{{%/ notice%}}


&nbsp;

## Les assertions

Les assertions sont un moyen simple de s’assurer, avant de continuer, qu’une condition est respectée.

On utilise la syntaxe : `assert test`. Si le test renvoie `True`, l’exécution se poursuit normalement. Sinon, une exception `AssertionError` est levée. 

On peut utiliser les assertions pour s’assurer que les arguments d’une fonction vont permettre son exécution.

On peut par exemple sécuriser la définition d'une fonction racines donnant les racines d'un trinôme du second degré. On va s’assurer que les arguments passés sont bien des nombres (et renvoyer un message explicatif si ce n’est pas le cas) :

```python
import math
def racines(a,b,c):
    """Retourne les racines de ax^2 + bx + c"""
    type_nombre = (float,int)
    assert (type(a) in type_nombre) and (type(b) in type_nombre) and (type(c) in type_nombre),"les arguments doivent être des nombres !"
    d = b**2 - 4*a*c
    r1 = (-b - math.sqrt(d))/2/a
    r2 = (-b + math.sqrt(d))/2/a
    return r1, r2
```
`racines(1,6,5)` retourne `(-5.0, -1.0)`, mais `racines(1,6,'5')` lève l'erreur suivante :\
`AssertionError: les arguments de la fonction racines doivent être des nombres !`