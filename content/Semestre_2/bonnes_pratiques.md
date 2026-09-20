---
title: "Les bonnes pratiques"
date: 2021-03-06T14:23:56+01:00
weight : 1
draft: false
---

# Les bonnes pratiques


Beaucoup de personnes amenées à coder plus ou moins régulièrement se sont un jour retrouvées à maudire leur moi du passé en reprenant un programme qu'ils avaient écrit seulement quelques semaines/mois auparavant mais qui leur est subitement devenu  complètement cryptique. 

![](https://c.tenor.com/A7NIlRIBtNoAAAAM/brooklyn99-brooklyn-nine-nine.gif)

Le temps perdu est alors énorme et vécu d'autant plus douloureusement qu'il était facilement évitable...

![](https://c.tenor.com/UsEL0CtIGKwAAAAC/trash-computer.gif)

&nbsp;

## Commenter son code

{{%notice info%}}
**Commenter son code** via l'utilisation de `#` est la principale protection contre de telles autotortures.
{{%/notice%}}

Il ne s'agit pas de commenter chaque ligne comme on voit parfois...
```python
a,b = 2,3	# j'affecte la valeur 2 à la variable a et la valeur 3 à b
c = a+b 	# j'affecte à c le résultat de l'addition entre a et b
print(c) 	# j'affiche le résultat
```
![](https://c.tenor.com/QfyQ4kMW834AAAAM/yuck-gross.gif)
Il faut au contraire se concenter sur les points délicats susceptibles d'échapper à son moi du futur (qui n'a jamais autant de mémoire qu'on le pense). 

C'est souvent intéressant d'y **justifier ses choix de programmation** comme celui d'utiliser une structure de données plutôt qu'une autre (un dictionnaire plutôt qu'une liste par exemple). Ces différents choix sont en effet sensés ne rien devoir au hasard, donc autant noter clairement ce qui vous a fait préférer telle option plutôt qu'une autre, histoire que votre lecteur puisse comprendre votre démarche (et pour aider votre moi du futur à s'y retrouver).

De manière plus systématique, une structure minimale de commentaires permet de cadrer rapidement les points clé d'un bloc d'instruction (qu'il s'agisse d'une boucle ou d'une fonction).\
Un bloc de code utilise généralement un ou plusieurs paramètres appelés paramètres d'entrées et construit à partir d'eux un ou plusieurs paramètres de sortie.\
Dans l'idéal, on commente alors chaque bloc de code en précisant dans la mesure du possibles les 3 éléments suivants :
- **préconditions**
- **postconditions**
- **invariant**

{{%notice def%}}
**préconditions** : ce sont les conditions que doivent vérifier impérativement les paramètres d'entrée pour que le code fasse ce qui est attendu.
{{%/notice%}}
{{%notice def%}}
**postconditions** : ce sont les conditions que doivent vérifier impérativement les paramètres de sortie (après le bloc).
{{%/notice%}}
Par exemple, si le bloc de code est sensé calculer une moyenne sur 20, la postcondition sera que la variable de sortie soit bien un flottant compris entre 0 et 20 valant la moyenne des valeurs en entrée.
{{%notice def%}}
**invariant** : propriété qui devra être vérifiée à chaque itération de manière à ce que la précondition aboutisse bien au final à la poscondition.
{{%/notice%}}

Exemples :
- si l'algorithme correspond à "manger une pizza", une *précondition* est la présence de la pizza et une *postcondition* est l'absence de ladite pizza.
- pour calculer une racine carrée, une *précondition* est que le nombre en entrée ne soit pas négatif et une *postcondition* est que le carré de la sortie valle le nombre en entrée.
- pour utiliser une recherche dichotomique, la *précondition* principale est que la liste soit triée.
- lors d'un tri par sélection l'*invariant* est : "la partie de la liste déjà inspectée est triée".



Exemple complet avec la division euclidienne :
```python
# ce code permet de calculer le quotient et le reste de la division euclidienne de a par b
# préconditions : a et b entiers, a ≥ 0 et b > 0
a, b = 28, 5

r = a
q = 0
while r >= b: # invariant : a = b*q + r
    r = r-b
    q = q+1
    
print(q,r)
# postconditions : a = b*q + r, 0 ≤ r < b, a et b inchangés
```



&nbsp;

## Choisir des noms explicites

Bien nommer ses variables améliore fortement la lisibilité du code.\
Choisir des noms explicites qui se rapportent au rôle et/ou aux types des variables utilisées est en effet un bien meilleur guide pour le lecteur du code que des noms génériques tel `a`, `b`, `c`...

```python
y_0, v_0 = 0.3, 7.2
g = -9.8
t = 0
dt = 1e-3
y, v = y_0, v_0
while y > 0:
    v += g*dt
    y += v*dt
    t += dt
print(t)
```
Un physicien comprend rapidement le but de ce code, mais d'autres choix de noms l'auraient rendu bien plus obscur.

&nbsp;

## Utiliser des fonctions

Autre pratique améliorant son code : l'utilisation de fonctions.

But :
- **éviter de réécrire du code** : on appelle la fonction contenant le code à la place (toute répétition de code est globalement à éviter, comme dans un texte littéraire) ;
- **simplifier la lecture du code** (et plus les noms des fonctions seront clairs, plus la compréhension du code sera simplifiée) ;
- **rendre son code modulaire** : les fonctions construites sont autant d'outils ayant une mission clairement définie. Et on peut très bien utiliser des fonctions au sein d'autres fonctions pour améliorer encore la lisibilité.

&nbsp;


## Documenter ses fonctions 

Les fonctions ont pour vocation d'être réutilisées (par vous ou par d'autres) et demande donc une attention particulière à leur description. Les fonctions ont ainsi droit à une forme de commentaire spéciale, le **docstring**, qui peut être interrogée directement par l'utilisateur (voir note ci-dessous).

On indique les types attendus des entrées (les paramètres) et des sorties (les retours) en inscrivant la **signature** de la fonction dans son docstring et on y ajoute les préconditions et les postconditions ainsi qu'une brêve descritpion.

exemple :

```python
def moyenne(notes):
    """
    calcule une moyenne sur 20 à partir de différentes notes sur 20
    moyenne(notes: list) -> moy: float
    précondition: la liste notes contient des nombres entre 0 et 20
    postcondition: moy est la moyenne des éléments de notes
    """
    moy = 0
    for n in notes:
        moy += n
    moy /= len(notes)
    return moy
```
{{%notice tip%}}
On peut afficher le docstring d'une fonction via la méthode `.__doc__`.
{{%/ notice%}}

```python
print(moyenne.__doc__)
```
`calcule une moyenne sur 20 à partir de différentes notes sur 20`\
`moyenne(notes:list) -> moy:float`\
`précondition : la liste notes contient des nombres entre 0 et 20`\
`postcondition : moy est la moyenne des éléments de notes`


&nbsp;

## Contraindre les spécifications avec des assertions

En sus de noter les préconditions dans les commentaires, on peut aussi tenter de s'assurer qu'elles sont bien vérifiées.
Qui vous assure en effet que votre fonction, par ailleurs parfaitement sage lorsque les entrées respectent les préconditions ne devienne pas folle dans certains cas loufoques&nbsp;? C'est bien vous qui serez blamé lorsque l'entrée farfelue causera une catastrophe...

[L'explosion du vol 501 d'Ariane](https://hownot2code.com/2016/09/02/a-space-error-370-million-for-an-integer-overflow/) est à cet égard un exemple édifiant. Un même programme ayant parfaitement accompli son œuvre de nombreuses années pour Ariane 4 a été réutilisé en toute sérénité dans le nouveau modèle. Mais voilà...
![](/vol501.jpg?width=400)
Le plan de vol différent d'Ariane 5 provoquait des accélérations très supérieures à celles enregistrées sur Ariane 4 jusqu'à déborder la capacité alors allouée au codage de ces mesures dans la station inertielle. La valeur élevée non prévue a planté le programme car elle a d'abord été répercutée sans lever d'erreur et du coup mal interprétée par les dispositifs de correction de trajectoire. Une petite assertion bien placée aurait peut-être pu économiser 1 milliard d'euros...

Exemple (aux répercutions moins coûteuses) : pour s'assurer que le notes passées en argument sont bien des nombres entre 0 et 20, on peut écrire dans le corps de la fonction :

```python
for n in notes:
    assert type(n) in (int,float) and 0<=n<=20
```
&nbsp;


## Tester

> "90% of coding is debugging. The other 10% is writing bugs"

Quand un code ne donne pas le résultat attendu, il faut partir à la recherche de l'erreur. Pour cela, le plus simple est d'utiliser un **jeu de test**.

Il s'agit tout simplement de disposer des `print` tout le long de son code pour afficher conjointement les valeurs réellement prises par les différentes variables à cet endroit du code et les valeurs qu'on souhaiterait.

{{%notice tip%}}
Le plus efficace est d'adopter une démarche dichotomique pour placer ces tests : début-milieu-fin dans un premier temps, puis on découpe en deux début-milieu et milieu-fin, etc.
{{%/notice%}}

Prenons un exemple. Le programme suivant est sensé décider si la suite de caractères qu'on a entré au clavier est un palindrome ou non :

```python
def bug():
    res = []
    fini = False
    print('Ajoutez des caractères un par un en validant avec entrée, puis appuyez sur entrée pour terminer')
    while not fini:
        elem = input('')
        if elem == '':
            fini = True
        else:
            res.append(elem)
    tmp = res
    tmp.reverse()
    Pal = (res == tmp)
    if Pal:
        print('palindrome')
    else:
        print('pas palindrome')
```
Lançons `bug` et entrons les caractères `'a'`,`'2'`,`'a'`.\
La fonction affiche alors :
`palindrome`\
Jusque-là tout va bien.\
Entrons maintenant `'a'`,`'2'`,`'b'`.\
La fonction affiche maintenant...
`palindrome`

![](https://64.media.tumblr.com/tumblr_llbsvgFbS91qc7geho1_400.gif)

Donc ça bugue. Mettons en place note démarche systématique en inserrant un premier `print` à peu près au milieu, juste après le `while`. À ce niveau, on a construit la liste `res`, affichons-la au côté de ce qu'on attend qu'elle soit.

```python
def bug():
    res = []
    fini = False
    print('Ajoutez des caractères un par un en validant avec entrée, puis appuyez sur entrée pour terminer')
    while not fini:
        elem = input('')
        if elem == '':
            fini = True
        else:
            res.append(elem)
    print("res devrait être ['a','2','b'] et est",res)
    tmp = res
    tmp.reverse()
    Pal = (res == tmp)
    if Pal:
        print('palindrome')
    else:
        print('pas palindrome')
```

Après avoir relancé `bug()` et retapé `'a'`,`'2'` et `'b'`, on voit s'afficher : `res devrait être ['a','2','b'] et est ['a', '2', 'b']`\
On sait maintenant que la première partie du code fait son boulot&nbsp;! 

Concentrons-nous sur la deuxième partie en plaçant un `print` avant le `if`. On a ici une nouvelle variable, `tmp`, en plus de `res`. Testons les deux&nbsp;:

```python
def bug():
    res = []
    fini = False
    print('Ajoutez des caractères un par un en validant avec entrée, puis appuyez sur entrée pour terminer')
    while not fini:
        elem = input('')
        if elem == '':
            fini = True
        else:
            res.append(elem)
    #print("res devrait être ['a','2','b'] et est",res)
    tmp = res
    tmp.reverse()
    Pal = (res == tmp)
    print(f'tmp = {tmp}, res = {res}')
    if Pal:
        print('palindrome')
    else:
        print('pas palindrome')
```

S'affiche alors : `tmp = ['b', '2', 'a'] res = ['b', '2', 'a']`

Aha ! `tmp` a la bonne tête, mais`res` aussi a été modifié, et ça, ce n'était pas prévu... Le problème est donc dans les 3 lignes qui précèdent le `print`. On pourrait placer un nouveau test entre ces lignes, mais vous aurez sans doute déjà trouvé le piège dans lequel le codeur est tombé.

{{%notice tip%}}
On aurait pu être tenté de ne pas retester `res` à cette étape puisqu'on venait de le faire au test précédent, mais cela aurait été du coup très mal joué  (un bug dans la chasse au bug)&nbsp;!
{{%/notice%}}

Attention, comme le dit le grand Dijkstra : *"Tester décèle la présence de bugs, pas leur absence."*<br>
Aucun test ne pourra montrer que votre programme ne contient aucun bug...

Une des expériences les plus vexantes et retorses, elle aussi vécue par beaucoup, voit le codeur présenter fièrement un programme qui répond parfaitement à ses attentes, mais qui crashe piteusement à la première utilisation d'une autre personne...

![](https://i.pinimg.com/originals/2a/b4/f8/2ab4f866c5e7dce9cd493a94e6d7beb1.gif)

L'origine probable de cette débâcle est que le codeur n'ait pas testé son programme pour des entrées suffisamment différentes. Et si le testeur n'a pas reçu le mémo l'obligeant à ne tenter que les quelques entrées que le codeur a validées, il se retrouve en terrain miné&nbsp;!

{{%notice warning%}}
Morale : il faut tester le plus largement possible les entrées d'un programme.
{{%/notice%}}

{{%notice info%}}
Pour ne pas non plus se perdre dans une revue systématique, vous gagnerez à **partitionner le domaîne des entrées** en grandes classes.\
Une **classe** est telle qu'à l'intérieur, le programme réagisse de la même façon avec toutes les entrées. Il suffit alors de ne tester qu'une seule valeur par classe.
{{%/notice%}}

Exemple : si on fabrique une fonction valeur absolue, plutôt que de tester des milliers de nombres, on peut se contenter de tester une valeur dans chacune des trois classes suivantes correspondantes aux différents comportements de la fonction (et donc aux différents branchements de son code) : entrées $< 0$, entrées $> 0$ et la frontière entrées $=0$.

En conclusion, mieux vous aurez défini l'ensemble des entrées acceptables et bien inspecté leurs frontières, plus facilement vous pourrez guider le lecteur de votre code à l'intérieur de ces frontières de bon fonctionnement via les préconditions. Car s'il est évident pour votre moi du présent que votre code demande nécessairement un type de données précis et qu'il ne viendrait à l'idée de personne d'utiliser autre chose, attendez seulement quelques temps que le doute vous assaille en le relisant... Et s'il vous arrive d'hésiter un tant soit peu, imaginez quelqu'un d'autre&nbsp;!