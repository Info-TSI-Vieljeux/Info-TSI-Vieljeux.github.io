---
title: "Traits généraux"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
---



# Traits généraux



## Introduction



### Shell et IDE

Python est un langage de programmation interprété développé par Guido van Rossum en 1989. Langage impératif de haut-niveau doté d'une syntaxe simple, Python s'adapte à de nombreux contextes grâce à sa modularité ; une importante librairie de modules et packages permet en effet d'étendre ses capacités.

Python possède son propre shell (interface en ligne de commande) : l'utilisateur entre une commande Python qui est interprétée immédiatement lorsque `Entrée` est tapée.  
Au lancement, le shell Python, poli, se présente : 

<div style="position:relative;margin-left:auto;margin-right:auto;width:550px;max-width:100%;">
<img src="/shell0.png" style="box-shadow:none;background:none;border-radius:3px;">
</div>

Les 3 chevrons sont l'invite (ou prompt) où les commandes seront écrites.  
IPython, un shell plus évolué, utilise `[1]` comme invite (où le chiffre dans les crochets s'incrémente à chaque commande).  
Pour sortir du shell classique, il faut taper `exit()`, et `exit` ou `quit` pour sortie du shell IPython.

On peut tout à fait exécuter des commandes Python une à une dans le shell.  
Une commande qui renvoie un résultat est appelée **expression**, alors qu'une commande qui ne renvoie rien est une **instruction**.  
Toute fonction est une expression, mais certaines ont en plus un **effet**  sur l'environnement comme `print()` qui permet d'afficher une chaîne de caractères dans le shell ou dans un fichier (elle retourne aussi la valeur `None` qui est omise dans ce cas par le shell).

<div style="position:relative;margin-left:auto;margin-right:auto;width:350px;max-width:100%;">
<img src="/shell.png" style="box-shadow:none;background:none;border-radius:3px;">
</div>

{{% notice note%}}
Par une mauvaise traduction de l'anglais *side effect*, les fonctions qui modifient un état en dehors de leur environnement local comme une modification de la mémoire (écriture d'un fichier) ou une modification d'un périphérique (affichage sur l'écran par exemple) sont dites à **effet de bord**.
{{%/notice%}}

Pour les projets plus complexes nécessitant d'enchaîner les instructions, on écrit l'ensemble de ces commandes (le programme) dans un éditeur de texte et on enregistre le fichier avec une extension `.py`.  
On demande alors à l'interprète Python d'exécuter l'ensemble du script en utilisant la commande `python nom_du_fichier.py` dans le shell de l'OS. Les différents retours dans le shell ne sont alors plus affichés, seuls les effets ont un... effet.  

Le plus simple pour coder est d'utiliser un environnement de travail (**IDE** pour "integrated development environment") qui combine un éditeur de code et un shell Python permettant d'exécuter le script entier ou une partie directement via l'interface.<br>

![](/pyzo.png)


### Installation

L'installation d'[Anaconda](https://www.anaconda.com/products/individual) rend disponible les principales bibliothèques scientifiques Python ainsi que le preformant IDE **Spyder** ou encore **Jupyterlab** (très intéressant pour les présentations de projets car associant dans une même interface texte et code pour former un *notebook*).<br>

---


&nbsp;


Passons maintenant en revue quelques caractéristiques du langage Python.<br>
## Typage dynamique

Contrairement à des langages à typage statique comme le C, **le type de la variable n'a pas besoin d'être déclarée en Python**. On parle alors de **typage dynamique**.\
L'interprète Python détermine par lui-même le type en fonction de l'objet affecté à la variable.

<div style="position:relative;margin-left:auto;margin-right:auto;width:350px;max-width:100%;">
<img src="/shell2.png" style="box-shadow:none;background:none;border-radius:3px;">
</div>

&nbsp;


## Principe d'indentation

Beaucoup de langage de programmation (C++, Java par exemple) utilisent des accolades `{}` pour définir un **bloc de code** (boucles,fonctions, instructions conditionnelles). Python utilise l'**indentation** ([décalage d'un nombre constant d'espaces blancs, généralement 4, ou une tabulation](https://www.youtube.com/watch?v=SsoOG6ZeyUI&t=2s)).
```Python
for i in range(3):
    mot = ''
    for lettre in ('a','b','c'):
        mot += lettre*i
    print(mot)
```
>Qu'est-ce qui s'affiche ?


&nbsp;



## Portée lexicale

Les variables définies à l'intérieur d'une fonction ont une **portée locale**. Elles ne sont pas reconnues dans le code principal (en dehors du bloc de la fonction).\
À l'inverse, les variables affectées dans le programme principal peuvent être utilisées partout (y compris dans la fonction) et sont dites **globales**.

Exemple :
```python
def foo():
    a = 'locale'
    print(a)
    print(b)
b = 'globale'
foo()
```
`locale`\
`globale`


Comme `b` n'est pas définie dans la bloc de la fonction, Python va la chercher dans le champ global. Mais il faut que `b` soit affectée avant l'appel de la fonction.

Que se passe-t-il si une fonction définit une variable locale avec le même nom qu'une variable globale ?\
Le champ local est scruté en premier.

Exemple :
```python
def foo():
    a = 'locale'
    print(a)
a = 'globale'
foo()
print(a)
```
`locale`\
`globale`

Notons bien que la variable locale `a` n'existe que dans le bloc de définition, qu'elle ait ou non le même nom qu'une variable globale ne change rien. 
Elle disparait quand l'interprète sort de la fonction et n'écrase donc pas la variable globale `a`.

{{% notice info%}}
Dans l'ordre, Python regarde d'abord le champ *local*, puis *non local* (le champ englobant la fonction intérieure dans le cas de fonctions imbriquées), 
puis *global*, puis *built-in* (les fonctions natives qu'il convient donc de ne pas redéfinir).
{{%/notice%}}


Une fonction ne peut pas modifier une variable globale sans préciser qu'elle le souhaite.

Exemple :
```python
x = 2
def fct1():
    print(x)

def fct2():
    x += 1
    print(x)
```


>Que se passe-t-il lorsqu'on appelle `fct1()` ? Et `fct2()` ?

Pour régler le problème, il faut utiliser le mot clé `global` qui permet de réaffecter la variable globale à l'intérieur de la fonction.

```python
def fct2():
    global x
    x += 1
    print(x)
```
L'appel de `fct2()` se fait maintenant sans heurt et `3` s'affiche. 

{{% notice warning%}}
Ce type de réaffectation est néanmoins à éviter, car il amène pas mal de confusion. C'est souvent plus logique de passer `x` en argument de la fonction.
{{%/notice%}}



&nbsp;


## Appel de fonction par valeur

Lors de l'appel d'une fonction, les arguments sont copiés et la fonction travaille alors uniquement sur cette copie.\
La copie disparaît lors du retour au programme principal.\
Si la fonction modifie la valeur d'un de ses arguments, seule la copie sera modifiée, pas la variable du programme principal.\
On dit que les arguments d'une fonction sont transmis **par valeurs** (par contraste avec la transmission par référence ou adresse comme dans le langage Java où une modification de l'argument dans la fonction se répercute dans le programme principal).


Exemple :
```python
def foo(a):
    print("valeur de 'a' au début de la fonction :",a)
    a = a*2
    print("valeur de 'a' à la fin de la fonction :",a)

a = 2
print("valeur de 'a' dans le programme principal avant l'appel de la fonction :",a)
foo(a)
print("valeur de 'a' dans le programme principal après l'appel de la fonction :",a)
```

<p style="overflow-x:auto;">
<code>
valeur de 'a' dans le programme principal avant l'appel de la fonction : ...<br>
valeur de 'a' au début de la fonction : ...<br>
valeur de 'a' à la fin de la fonction : ...<br>
valeur de 'a' dans le programme principal après l'appel de la fonction : ...
</code>
</p>

Notons toutefois que si l'argument est une liste, c'est sa référence qui est cette fois transmise... Toute modification de la liste dans la fonction se répercute à l'extérieur. La fonction a alors un effet de bord. C'est dû au statut mutable des listes dans Python. Et cela sera donc la même chose avec les dictionnaires, autre objet mutable.