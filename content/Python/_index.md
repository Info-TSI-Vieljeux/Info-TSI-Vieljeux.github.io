+++
title = "Python"
date = 2021-03-06T14:20:50+01:00
weight = 1
chapter = true
+++



# Python



### Extrait du programme :



<div style="text-align:left !important;">
<p style="text-align:left !important;font-size:16px">
Cette annexe liste limitativement les éléments du langage Python (version 3 ou supérieure) dont la connaissance est exigible des étudiants. Aucun concept sous-jacent n'est exigible au titre de la présente annexe.<br>
Aucune connaissance sur un module particulier n'est exigible des étudiants.<br>
Toute utilisation d'autres éléments du langage que ceux que liste cette annexe, ou d'une fonction d'un module, doit obligatoirement être accompagnée de la documentation utile, sans que puisse être attendue une quelconque maîtrise par les étudiants de ces éléments.

<h4><a href="./traitsgaux">Traits généraux</a></h3>
<ul style="font-size:16px">
<li>Typage dynamique : l'interpréteur détermine le type à la volée lors de l'exécution du code.</li>
<li>Principe d'indentation.</li>
<li>Portée lexicale : lorsqu'une expression fait référence à une variable à l'intérieur d'une fonction, Python cherche la valeur définie à l'intérieur de la fonction et à défaut la valeur dans l'espace global du module.</li>
<li>Appel de fonction par valeur : l'exécution de $f(x)$ évalue d'abord $x$ puis exécute $f$ avec la valeur calculée.</li>
</ul>


<h4><a href="./typesbase">Types de base</a></h3>
<ul style="font-size:16px">
<li>Opérations sur les entiers (<code>int</code>) : <code>+</code>, <code>-</code>, <code>*</code>, <code>//</code>, <code>**</code>, <code>%</code> avec des opérandes positifs.</li>
<li>Opérations sur les flottants (<code>float</code>) : <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>**</code>.</li>
<li>Opérations sur les booléens (<code>bool</code>) : <code>not</code>, <code>or</code>, <code>and</code> (et leur caractère paresseux).</li>
<li>Comparaisons <code>==</code>, <code>!=</code>, <code><</code>, <code>></code>, <code><=</code>, <code>>=</code>.</li>
</ul>


<h4><a href="./typesstruct">Types structurés</a></h3>
<ul style="font-size:16px">
<li>Structures indicées immuables (chaînes, tuples) : <code>len</code>, accès par indice positif valide, concaténation <code>+</code>, répétition <code>*</code>, tranche.</li>
<li>Listes : création par compréhension <code>[𝑒 for 𝑥 in 𝑠]</code>, par <code>[𝑒] * n</code>, par <code>append</code> successifs ; <code>len</code>, accès par indice positif valide; concaténation <code>+</code>, extraction de tranche, copie (y compris son caractère superficiel) ; <code>pop</code> en dernière position.</li>
<li>Dictionnaires : création, accès, insertion, <code>len</code>, <code>copy</code>.</li>
</ul>


<h4><a href="./structcontr">Structures de contrôle</a></h3>
<ul style="font-size:16px">
<li>Instruction d’affectation avec <code>=</code>. Dépaquetage de tuples.</li>
<li>Instruction conditionnelle : <code>if</code>, <code>elif</code>, <code>else</code>.</li>
<li>Boucle <code>while</code> (sans <code>else</code>). <code>break</code>, <code>return</code> dans un corps de boucle.</li>
<li>Boucle <code>for</code> (sans <code>else</code>) et itération sur <code>range(𝑎, 𝑏)</code>, une chaîne, un tuple, une liste, un dictionnaire au travers des méthodes <code>keys</code> et <code>items</code>.</li>
<li>Définition d’une fonction <code>def f(𝑝<sub>1</sub>,...,𝑝<sub>𝑛</sub>)</code>, <code>return</code>.</li>
</ul>


<h4><a href="./divers">Divers</a></h3>
<ul style="font-size:16px">
<li>Introduction d’un commentaire avec <code>#</code>.</li>
<li>Utilisation simple de <code>print</code>, sans paramètre facultatif.</li>
<li>Importation de modules avec <code>import <i>module</i></code>, <code>import <i>module</i> as <i>alias</i></code>, <code>from <i>module</i> import 𝑓,𝑔,...</code></li>
<li>Manipulation de fichiers texte (la documentation utile de ces fonctions doit être rappelée ; tout problème relatif aux encodages est éludé) : <code>open</code>, <code>read</code>, <code>readline</code>, <code>readlines</code>, <code>split</code>, <code>write</code>, <code>close</code>.</li>
<li>Assertion : <code>assert</code> (sans message d’erreur).</li>
</ul>

</p>
</div>

