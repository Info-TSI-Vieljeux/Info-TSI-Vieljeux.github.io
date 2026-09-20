---
title: "TP 8 : correction et complexité"
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


# TP 8 : correction et complexité

<p style="text-align: center;">  Cliquez sur <a href="https://classroom.github.com/a/U71v16BO">cette invitation</a> pour récupérer le repository du TP. </p>

## Multiplication égyptienne

Considérons le code suivant, qui implémente un ancien algorithme égyptien.<br>
`a` et `b` sont supposés être des entiers positifs.


```python
def multegy(a, b):
    p = 0
    while a > 0:
        if a%2 == 1:
            p += b
        b *= 2
        a //= 2
    return p
```

>Qui est le **variant de boucle** permettant de prouver que `multegy` termine toujours ?
>- a : a
>- b : b
>- c : p
>- d : autre réponse

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<code>a</code> est une suite d'entiers positifs strictement décroissante, c'est donc un variant de boucle.
</details>

>Détaillez l'éxécution de `multegy(23,5)` en affectant à `a_i`, `b_i`, `p_i`, les valeurs rencontrées en début de chaque itération.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def multegy(a, b):
    p = 0
    i = 0
    while a > 0:
        print(f"itération {i} : {a = }, {b = }, {p = }")
        if a%2 == 1:
            p += b
        b *= 2
        a //= 2
        i += 1
    print(f"itération {i} : {a = }, {b = }, {p = }")
    return p
multegy(23,5)
</code></pre>
Ce code affiche&nbsp;:<br>
<code>itération 0 : a = 23, b = 5, p = 0</code><br>
<code>itération 1 : a = 11, b = 10, p = 5</code><br>
<code>itération 2 : a = 5, b = 20, p = 15</code><br>
<code>itération 3 : a = 2, b = 40, p = 35</code><br>
<code>itération 4 : a = 1, b = 80, p = 35</code><br>
<code>itération 5 : a = 0, b = 160, p = 115</code>
</blockquote>
</details>

Construisons la preuve de l'algorithme :<br>

on va montrer que $a\times b + p$ est un **invariant de boucle** et l'utiliser pour prouver que l'algorithme retourne bien le produit entre $a$ et $b$.<br>

Notons $a_k$, $b_k$, $p_k$, les valeurs de $a$, $b$ et $p$ après la k<sup>e</sup> itération et supposons $a_k\times b_k + p_k = cste$.
- initialisation : pour $k=0$, $a_0=a$, $b_0=b$ et $p_0=0$. D'où $a_0\times b_0+p_0=a\times b$
- conservation : à la boucle $k+1$, deux cas se présentent :
    - si $a$ est impair : $a_{k+1} = X$, $b_{k+1} = Y$ et $p_{k+1}= Z$.<br>
    D'où $a_{k+1}\times b_{k+1} + p_{k+1} =  a_k\times b_k - b_k +p_k+ b_k = a_k\times b_k+p_k$
    - si $a$ est pair : $a_{k+1} = \frac{a_k}{2}$, $b_{k+1} = b_k\times 2$ et $p_{k+1}=p_k$.<br>
    D'où $a_{k+1}\times b_{k+1} + p_{k+1} =  a_k\times b_k + p_k$<br>
    Par conséquent, $a_k\times b_k + p_k$ est bien un invariant pour tout $k$.
- terminaison : en sortie de boucle (itération $f$), $a_f = 0$, donc $a_f\times b_f+p_f = p_f$. Or comme l'invariant est... invariant, il garde toujours la valeur qu'il possède en entrée (pour $k=0$) : d'où $p_f = a\times b$. Et comme la fonction retourne $p_f$, cqfd.

> Que vallent X,Y et Z ?
>- a : $a_k$, $b_k$, $p_k+b_k$
>- b : $\frac{a_k-1}{2}$, $b_k\times 2$, $p_k+b_k$
>- c : $\frac{a_k+1}{2}$, $b_k\times 2$, $p_k$


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$\displaystyle X = \frac{a_k+1}{2}$, $Y = b_k\times 2$, $Z = p_k+b_k$
</blockquote>
</details>

>Quelle est la complexité de `multegy` (en supposant chacun des calculs comme élémentaire) ?
>- a : $O(a)$
>- b : $O(a\times b)$
>- c : $O(a\log b)$
>- d : $O(\log a)$
>- e : $O(b)$

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Il y aura autant de tours dans la boucle <code>while</code> que le nombre de fois qu'on peut diviser <code>a</code> par 2 (division euclidienne) avant d'arriver sur 0. Ce nombre est en $O(\log a)$.<br>
Et à chaque tour, il y a soit $c$ étapes, soit $c+1$ où $c$ est une constante.<br>
La complexité globale reste donc en $O(\log a)$.

</blockquote>
</details>

&nbsp;


## Deux fonctions de recherche


```python
def cherche(s, m):  
    for k in range(len(s) - len(m) + 1):  
        b = True  
        for i in range(len(m)):  
            if s[k + i] != m[i]:  
                b = False  
        if b:  
            return True  
    return False 
```


```python
def cherche2(s, m):  
    for k in range(len(s) - len(m) + 1):  
        if s[k:k + len(m)] == m:  
            return True  
    return False 
```

>Quelle est la complexité de la fonction cherche ? Et celle de cherche2 ?<br>
Appelons `len(s)` n et `len(m)` p. 
>- a : les deux en $O(n\times p)$
>- b : `cherche` en $O(n\times p)$ et `cherche2` en en $O(n)$
>- c : une autre réponse

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Les deux sont en $O(n\times p)$.<br>
Il ne faut pas simplement compter les imbrications de boucles (même si c'est souvent suffisant)&nbsp;; dans le cas de <code>cherche2</code>, $m$ étapes sont cachées dans la comparaison <code>s[k:k + len(m)] == m</code> puisque l'interprète python ne peut faire autrement que de comparer les caractères un par un pour s'assurer que les deux chaînes sont bien les mêmes.
</blockquote>
</details>

Exécuter le code suivant peut vous aider à confirmer votre réponse.


```python
import time
from random import randint

abc = 'abcdefghijklmnopqrstuvwxyz'
def motdenlettres(n): 
    mot = ''
    for i in range(n):
        mot += abc[randint(0,25)]
    return mot

print('-'*30)
print('|    n    |    p   | cherche2 |')
print('-'*30)
for j in range(2,6):
    n = 10**5*2**j
    s = motdenlettres(n)
    for k in range(3):
        p = 10**4*2**k
        m = motdenlettres(p)
        
        d = time.time()
        cherche2(s,m)
        f = time.time()
        t = f - d
        
        print(f'|{n:^9d}|{p:^8d}|{t:^10.2E}|')
    print('-'*30)
```

{{<rawhtml>}}
<div style="font-family:monospace;">
------------------------------<br>
|&nbsp;&nbsp;&nbsp;&nbsp;n&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;p&nbsp;&nbsp;&nbsp;|&nbsp;cherche2&nbsp;|<br>
------------------------------<br>
|&nbsp;400000&nbsp;&nbsp;|&nbsp;10000&nbsp;&nbsp;|&nbsp;2.04E-01&nbsp;|<br>
|&nbsp;400000&nbsp;&nbsp;|&nbsp;20000&nbsp;&nbsp;|&nbsp;4.65E-01&nbsp;|<br>
|&nbsp;400000&nbsp;&nbsp;|&nbsp;40000&nbsp;&nbsp;|&nbsp;9.72E-01&nbsp;|<br>
------------------------------<br>
|&nbsp;800000&nbsp;&nbsp;|&nbsp;10000&nbsp;&nbsp;|&nbsp;4.20E-01&nbsp;|<br>
|&nbsp;800000&nbsp;&nbsp;|&nbsp;20000&nbsp;&nbsp;|&nbsp;8.94E-01&nbsp;|<br>
|&nbsp;800000&nbsp;&nbsp;|&nbsp;40000&nbsp;&nbsp;|&nbsp;2.06E+00&nbsp;|<br>
------------------------------<br>
|&nbsp;1600000&nbsp;|&nbsp;10000&nbsp;&nbsp;|&nbsp;8.25E-01&nbsp;|<br>
|&nbsp;1600000&nbsp;|&nbsp;20000&nbsp;&nbsp;|&nbsp;1.85E+00&nbsp;|<br>
|&nbsp;1600000&nbsp;|&nbsp;40000&nbsp;&nbsp;|&nbsp;4.20E+00&nbsp;|<br>
------------------------------<br>
|&nbsp;3200000&nbsp;|&nbsp;10000&nbsp;&nbsp;|&nbsp;1.66E+00&nbsp;|<br>
|&nbsp;3200000&nbsp;|&nbsp;20000&nbsp;&nbsp;|&nbsp;3.64E+00&nbsp;|<br>
|&nbsp;3200000&nbsp;|&nbsp;40000&nbsp;&nbsp;|&nbsp;8.30E+00&nbsp;|<br>
------------------------------<br>
</div>
{{</rawhtml>}}

<br>

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)</summary>
<blockquote id="comm">
On constate bien sur le tableau que pour un $n$ fixé, le temps de calcul de <code>cherche2</code> semble proportionnel à $p$, et que pour un $p$ fixé, il semble proportionnel à $n$...
</blockquote>
</details>


>Quelle est la complexité au meilleur de la fonction cherche ?
>- a : $O(n)$
>- b : $O(p)$
>- c : $O(1)$

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Le meilleur des cas possible correspond à un mot à cherché placé au tout début du texte. Il faudra alors $p$ comparaisons (la longueur du mot) avant de sortir de la fonction.<br>
D'où $O(p)$ au meilleur.
</blockquote>
</details>


{{%notice note%}}
On peut déterminer ce que fait la fonction `cherche` en mettant en lumière deux **invariants**, un pour chaque boucle.<br>
La boucle interne a pour invariant "`b` équivaut à `s[k:k+i]==m[:i]`".<br>
Et la boucle externe a pour invariant "`s[j:j+len(m)] != m pour tout j<k`" car s'il y avait égalité, on serait sorti de la  boucle avec le `return True`.<br>
On en conclut que si la boucle n’est jamais interrompue par le `return True` alors `m` n’est pas un sous-mot de `s`.<br>
Si la boucle est interrompue, d’après l’invariant de la boucle intérieure, on a trouvé `m` dans `s`. 
{{%/notice%}}


<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)</summary>
<blockquote id="comm">
Vous trouverez des exemples de calcul de complexité et une <a href="https://presentationssite.github.io/info/defis/#/9/3">démonstration de correction</a> dans la section recensant <a href="https://presentationssite.github.io/info/defis/#/">les défis algorithmiques</a> ( le défi est souvent de réussir à diminuer la classe de complexité en passant d'un algo naïf à un algo plus malin).
</details>