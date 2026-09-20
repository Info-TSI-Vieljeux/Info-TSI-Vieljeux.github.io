+++
title = "Introduction"
date = 2021-03-06T14:20:50+01:00
weight = 0
chapter = true
+++


# Informatique en prépa TSI

Compétences visées (d'après le BO)&nbsp;:

<div style="position:relative;margin-left:auto;margin-right:auto;max-width:100%;">
<img src="https://media.tenor.com/7jTIEqj50XoAAAAC/it-crowd-richard-ayoade.gif" style="box-shadow:none;background:none;border-radius:15px;">
</div>

- **analyser et modéliser** un problème ou une situation, notammant en utilisant les objets conceptuels de l'informatique pertinents (table relationnelle, graphe, dictionnaire, etc.)&nbsp;;
- **imaginer et concevoir une solution**, décomposer en blocs, se ramener à des sous-problèmes simples et  indépendants, adopter une stratégie appropriée, décrire une démarche, un algorithme ou une structure de données permettant de résoudre le problème&nbsp;;
- **décrire et spécifier** les caractéristiques d’un processus, les données d’un problème, ou celles manipulées par un algorithme ou une fonction&nbsp;;
- **mettre en œuvre une solution**, par la traduction d’un algorithme ou d’une structure de données dans un langage de programmation ou un langage de requête&nbsp;;
- **justifier et critiquer une solution**, que ce soit en démontrant un algorithme par une preuve mathématique ou en développant des processus d’évaluation, de contrôle, de validation d’un code que l’on a produit&nbsp;;
- **communiquer à l’écrit ou à l’oral**, présenter des travaux informatiques, une problématique et sa solution ; défendre ses choix ; documenter sa production et son implémentation.

Bon, ben voilà... Y a plus qu'à&nbsp;!

<!--
# Préalable

Pour le fonctionnement des 3 prochains trimestres, il faut que vous ayez :
- un compte [Google](https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&hl=fr&flowName=GlifWebSignIn&flowEntry=SignUp) (ancien ou créé pour l'occasion) pour pouvoir utiliser Colaboratory
- un compte [Github](https://github.com) où seront créés les reopositories des TP (répertoires à l'historique sauvegardé).
![](/Octocat.png?width=500)

La vidéo suivante présente le protocole à suivre pour être opérationnel  :

{{<youtube f5O8pkRFkAA>}}

&nbsp;

# Déroulement

Pour chaque TP, on suivra la démarche suivante :

- Vous trouverez un lien à cliquer au début de l'énoncé du TP sur ce site web. Il s'agit d'une invitation générer par Github Classroom. 
- En acceptant l'"assignment" (le travail demandé), un nouveau repository est créé sur Github.\
Il contient un ou plusieurs fichiers notebook python (d'extension ".ipynb") produits par l'application *Jupyter notebook*. Ce sont ces fichiers qu'il va falloir modifier pour gagner des points.
- Un **notebook** est découpé en cellules qui peuvent contenir soit du texte et des images, soit du code. Chaque cellule peut s'exécuter individuellement et fait alors tourner le code qu'elle contient, mais Github n'est pas encore capable d'interagir avec un notebook aujourd'hui.\
On passe par une solution en ligne pour y pallier : **Colaboratory** (ou Colab).
- Pour transiter de Github à Colab, la démarche est très simple (sur le papier...) : une fois qu'on a cliqué sur le notebook, il suffit de modifier l'adresse url en ajoutant "*tocolab*" après github ('https://github.com/blablabla/tpx.ipynb' $\rightarrow$ 'https://githubtocolab.com/blablabla/tpx.ipynb' ).
- Si pour une raison ou une autre, vous n'arrivez pas à passer de Github à Colab directement, il y a une autre méthode, un peu moins confortable, mais qui fonctionnera à coup sûr : vous téléchargez le notebook depuis github sur votre disque (pour cela, il faut d'abord cliquer sur *Raw* pour accéder au code source, puis sauvegarder la page en prenant soin que le navigateur n'ajoute pas une extension après le .ipynb), puis vous l'importez depuis Colab.
![](/githubtocolab.png)
- Le vrai travail commence alors. Des consignes sont disséminées dans le notebook et il faudra modifier les cellules en fonction de ce qui est demandé. Généralement, l'endroit où une modification est attendu est clairement indiqué par le commentaire `# VOTRE CODE`.
- Tout est exécutable, ce qui veut dire que vous pouvez tester immédiatement vos modifications. Vous pouvez aussi ajouter autant de cellules que souhaité, où vous le souhaitez.\
Seules les cellules de test contenant les commentaires `# Cellule de test, ne pas modifier` ne doivent en aucun cas être modifiées ou supprimées.
- Pour être validées, vos modifications devront être sauvegardées dans le repo github du TP. Depuis Colab, il suffit théoriquement d'aller sur *Fichier > Enregistrer une copie dans Github*, puis de sélectionner le repo du TP.\
L'autre solution est d'enregistrer le fichier modifié sur le disque (*Fichier > Télécharger > Télécharger le fichier .ipynb*) puis de le glisser sur la fenêtre Github du repo (ou de cliquer sur *Add file > Upload files*). Pensez alors à **commiter** (= cliquer sur le bouton vert commit) pour valider.\
Attention, il ne faut pas créer un autre fichier ! C'est le notebook portant le nom initial qui sera ramassé et corrigé une fois le temps imparti pour le TP écoulé.
--->

# Cours et TP

<table>
<tr>
<th style="text-align:center;font-size:1.2em;"><a href="./python/">PYTHON</a></th>
</tr>
<tr>
<th style="text-align:center;font-size:1.2em;"><a href="./semestre_1/">SEMESTRE 1</a></th>
</tr>
<tr>
<th style="text-align:center;font-size:1.2em;"><a href="./semestre_2/">SEMESTRE 2</a></th>
</tr>
<tr>
<th style="text-align:center;font-size:1.2em;"><a href="./semestre_3/">SEMESTRE 3</a></th>
</tr>
<tr>
<th style="text-align:center;font-size:1.2em;"><a href="./concours-blanc/">DS</a></th>
</tr>
<tr>
<th style="text-align:center;font-size:1.2em;"><a href="./projets/">PROJETS</a></th>
</tr>
</table>

<br>


# Aide

<div style="position:relative;margin-left:auto;margin-right:auto;max-width:100%;">
<img src="https://media4.giphy.com/media/l46Cbqvg6gxGvh2PS/giphy.gif" style="box-shadow:none;background:none;border-radius:15px;">
</div>

<ul>
<li> La partie <b>Feedback</b> du repository du TP, caché dans l'onglet <b>Pull requests</b>, permet de me demander de l'aide en dehors des TP.</li>
<li> Ou vous pouvez m'envoyer un mail à l'adresse suivante : <span style="color:#929292"> 
    <a id="email-link" href="mailto:" style="font-size:1em;"></a>
</span></li>
</ul>



<script type="text/javascript">
    var part1 = "cordier.info";
    var part2 = "protonmail";
    var part3 = "ch";
    var email = part1 + "@" + part2 + "." + part3;

    // Mettre à jour le lien
    var link = document.getElementById("email-link");
    link.href = "mailto:" + email;
    link.textContent = email;
</script>