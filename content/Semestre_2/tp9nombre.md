---
title: "TP 9 : nombres en machine"
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
/* 1. Rétablir la déclaration que votre reset a écrasée */
details > summary:first-of-type {
  display: list-item;     /* remet le triangle + l’accessibilité */
  cursor: pointer;        /* optionnel : feedback visuel */
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

# TP9 : nombres

<p style="text-align: center;">  Cliquez sur <a href="https://classroom.github.com/a/m2zkkfNO">cette invitation</a> pour récupérer le repository du TP. </p>

## Exo 1 : nombres palindromiques

> Déterminer grâce à un code Python le plus petit nombre supérieur ou égal à $10\,000$ dont l'écriture est palindromique (se lisant pareil dans les deux sens) à la fois en base 10 et en base 2.


```python
### VOTRE CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">a = False
b = False
i = 10000
while not (a and b):
    str_i_10 = str(i)
    str_i_2 = bin(i)[2:]
    a = str_i_10 == str_i_10[::-1] # i palindromique en base 10
    b = str_i_2 == str_i_2[::-1]   # i palindromique en base 2
    i += 1
print(str_i_10,str_i_2)
</code></pre>
Saffiche alors&nbsp;:<br>
<code>15351 11101111110111</code>
</blockquote>
</details>


```python
# Affectez votre réponse (l'écriture en base 10 du nombre entier trouvé) à la variable nb
nb = 3
```
<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
$15\,351$
</blockquote>
</details>

&nbsp;

## Exo 2 : missiles Patriot

Une batterie de missiles Patriot détecte les missiles ennemis et les intercepte avec un contre-missile. La batterie mesure le temps pour prévoir le déplacement des missiles ennemis.<br>
Elle dispose d’un compteur (un entier) que nous appellerons `c` qui compte le nombre de dixièmes de secondes écoulés depuis sa mise en marche. Le temps écoulé `t` est calculé par l’opération `t=c*0.1`. Nous nous intéressons à l’erreur de calcul commise lors de cette multiplication.<br>
D’après un [rapport du General Accounting Office](https://www.gao.gov/assets/220/215614.pdf), le logiciel du Patriot utilise des nombres à virgule fixe stockés dans un registre de 24 bits.<br>
La représentation en virgule fixe utilisée est le format $Q1.23$ où seulement 1 bit est utilisé pour la partie entière et 23 bits le sont pour la partie fractionnaire.<br>
La partie fractionnaire d'un réel $\{x\}=x-\lfloor x\rfloor$ est stockée sur les 23 bits en la transformant en l'entier $\lfloor \{x\}\times 2^{23}\rfloor$ (où $\lfloor\rfloor$ est la partie entière), les chiffres au delà du 23<sup>ème</sup> après la virgule sont donc tronqués.<br>

![](/patriot.jpg?width=800)

> Écrivez en base 2 le nombre 0,1 en ne gardant que 24 chiffres (23 après la virgule). On notera $z$ le nombre obtenu.<br>
Vous pourrez vous aidez du code suivant (après l'avoir modifié de manière adéquate) pour déterminer la réponse ou utiliser la dernière phrase de l'énoncé (mais attention alors au petit piège).


```python
a = 2.7
avt = bin(int(a))[2:] + ','
n = a - int(a)
apres = ''
while len(apres)<9 :
    n *= 2
    if n > 1 :
        apres += '1'
        n -= 1
    else :
        apres += '0'
print(avt+apres)
```
`10,101100110`


```python
# Affectez à la variable z la chaîne de caractères correspondant à l'écriture binaire demandée :
z = '0,...'
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">a = 0.1
avt = bin(int(a))[2:] + ','
n = a - int(a)
apres = ''
while len(apres)<23:
    n *= 2
    if n > 1:
        apres += '1'
        n -= 1
    else:
        apres += '0'
print(avt+apres)
</code></pre>
Saffiche alors&nbsp;:<br>
<code>0,00011001100110011001100</code>
</blockquote>
</details>

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)</summary>
<blockquote id="comm">
On aurait aussi pu obtenir l'écriture en moins de lignes en utilisant <code>bin</code> sur $\lfloor 0,1\times2^{23} \rfloor$ (ce qui revient à décaler la virgule de 23 rangs en binaire)&nbsp;:
<pre><code class="language-python">a = bin(int(0.1*2**23))[2:23] # mais attention, il manque des zéros avant !
z = '0,'+'0'*(23-len(a))+a
</code></pre>
</blockquote>
</details>


On note $\varepsilon = |0,1 − z|$. La batterie de missiles Patriot fait une erreur de $\varepsilon$ en approximant 0,1.<br>
>Faites calculer par Python la valeur de $\varepsilon$ et affectez cette valeur à une variable epsilon.

```python
# Vous affecterez la valeur à la variable epsilon
epsilon = 
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">z = '0,00011001100110011001100'
eps = abs(0.1*2**23-int(z[2:],2))/2**23
</code></pre>
</blockquote>
</details>

Début février 1991, l’armée israélienne a empiriquement constaté qu’au bout de 8h, la précision des missiles est significativement réduite. Puis, le 25 février 1991, six batteries de missiles Patriot (un bataillon) ont été déployées à Dhahran, en Arabie Saoudite, pendant 100h. 

Nous noterons $e_8$ et $e\_{100}$ l’erreur commise sur $t$ par la batterie au bout de 8h puis au bout de 100h.<br>
> Calculez des deux erreurs précédentes. 

```python
# Vous affecterez les valeurs aux variables e_8 et e_100
e_8 = 
e_100 = 
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">e8 = eps*8*3600*10
e100 = eps*100*3600*10
</code></pre>
</blockquote>
</details>

Un Scud a une vitesse de croisière de 1676 m/s (Mach 5).<br>
>Pendant une durée $e\_{100}$, de quelle distance $d$ (en m) se déplace un Scud ? 


```python
# Vous affecterez la valeur à la variable d
d =
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">d = e100*1676
</code></pre>
</blockquote>
</details>

Suite à cette imprécision, un Scud irakien ne fut pas intercepté et causa 28 morts parmi les soldats américains.

&nbsp;

## Exo 3 : overflows

Les 3 "évènements" suivant correspondent au même bug : un dépassement de capacité d'entiers (signés ou non) codés sur 32 bits.

La FAA (Federal Aviation Administration) publie en 2015 une [Airworthiness Directive ou AD](https://s3.amazonaws.com/public-inspection.federalregister.gov/2015-10066.pdf) (notification technique que les compagnies aériennes sont obligées de suivre) concernant un bug dans le logiciel des Boeing 787 : "This AD was prompted by the determination that a Model 787 airplane that has been powered continuously for 248 days can lose all alternating current (AC) electrical power due to the generator control units (GCUs) simultaneously going into failsafe mode." Le logiciel mesure le temps depuis sa mise en route en incrémentant un compteur toutes les centisecondes.
![](/B787.jpg?width=800)

> D'après les informations fournies et vos réflexions, au bout de combien de centisecondes exactement, la capacité du compteur se trouve dépassée, expliquant le bug&nbsp;?


```python
# Vous affecterez la valeur entière à la variable nb_centi
nb_centi = 
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On cherche un nombre de centisecondes correspondant à 248 jours.<br>
Comme 2<sup>31</sup> cs correspondent à 248,6 jours, on peut supposer que le nombre de cs est codé en 32 bits signés.
</blockquote>
</details>

En 2004, l'oubli d'un technicien de rebooter un serveur a provoqué une immense pagaille dans le ciel californien. En effet, le 14 septembre, les aiguilleurs du ciel des aéroports du sud californien ont perdu le contact vocal avec 400 avions pendant plus de 3 heures, heureusement sans graves conséquences (grâce à la réaction rapide des contrôleurs qui ont tout de suite utilisé leurs portables pour contacter d'autres centres de contrôle aérien). La maintenance de routine du système de communication consistait à le rebooter tous les 30 jours. Ce système mesure le temps depuis sa mise en route en incrémentant un compteur toutes les millisecondes.
![](http://cordier-phychi.toile-libre.org/Info/github/radar.jpeg?width=800)


> D'après les informations fournies et vos réflexions, au bout de combien de millisecondes exactement, la capacité du compteur s'est trouvée dépassée, expliquant le bug&nbsp;?

```python
# Vous affecterez la valeur entière à la variable nb_milli
nb_milli = 
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On cherche un nombre de millisecondes dépassant les 30 jours (mais pas trop).<br>
Comme 2<sup>32</sup> ms correspondent à 49,7 jours. On peut supposer que le nombre de ms est codé en 32 bits non signés.
</blockquote>
</details>

Le bug de l'an 2038 concerne les horloges des systèmes unix 32 bits dont le temps 0, appelé *epoch*, est le 1 janvier 1970 à 00:00:00 UT.

```python
import time
time.gmtime(0)
```
`time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0`
{{%notice tip%}}
Cela montre que les serveurs hébergeant Colab tournent sous Unix.
{{%/notice%}}

>Au bout de combien de secondes exactement le problème lié au bug de 2038 se pose&nbsp;?

```python
# Vous affecterez la valeur entière à la variable 
nb_sec = 
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On cherche un nombre de secondes correspondant à 68 ans.<br>
Comme 2<sup>31</sup> s correspondent à 68,05 années. On peut supposer que le nombre de secondes est codé en 32 bits signés.
</blockquote>
</details>

Les overflows peuvent aussi avoir des conséquences plus sympatiques comme la machine à sous d'un casino qui a décidé un jour d'imprimer un ticket de **42&nbsp;949&nbsp;672,96&nbsp;$** !! Malheureusement pour le gagnant, le casino a refusé de payer sous prétexte que la machine indiquait un prix maximum de 10&nbsp;000&nbsp;$ et le tribunal a finalement donné raison au casino...

![](http://cordier-phychi.toile-libre.org/Info/github/courtois.png)
