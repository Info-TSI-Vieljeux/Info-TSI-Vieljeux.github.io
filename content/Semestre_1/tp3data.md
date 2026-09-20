---
title: "TP 3 : utilisation de modules"
date: 2021-03-06T14:23:56+01:00
weight : 3
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
#debord
{
overflow-x: auto; 
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

<br>

L'idée de ce TP est de constater combien des modules/bibliothèques adaptés peuvent fournir des outils puissants et permettre un gain de temps gigantesque.\
On va se placer dans un des champs les plus porteurs actuellement (et où python est très utilisé), l'analyse de données.

<br>

<p style="text-align: center;">  Cliquez sur <a href="https://classroom.github.com/a/3BZhe_dl">cette invitation</a> pour récupérer le repository du TP. </p>

# Exploration d'un jeu de données

## Statistiques simples


```python
import pandas as pd # bibliothèques dédiée au traitement de jeux de données
import matplotlib.pyplot as plt # bibliothèque graphique
import seaborn as sns # bibliothèque graphique reposant sur matplotlib et dédiée plus particulièrement à la représentation de jeux de données
import numpy as np # bibliothèque puissante permettant de gérer des tableaux multidimensionnels
import plotly.express as px # libraire permettant des graphes interactifs
import plotly.graph_objects as go # complémentaire à la première (seulement utile dans les cas complexes)
```
Pour pouvoir être importé, un module doit avoir été préalablement installé. Les plus importants sont installés par défaut dans certaines distributions (comme Anaconda).<br>
Les gros modules sont généralement importés sous la forme `import module as x` où `x` est un raccourci pour le nom du module (`np` pour `numpy` ou `plt` pour `matplotlib.pyplot`). Se référer au cours Python pour les autres formes d'importation.<br>
Pour obtenir de l'aide sur un module, on peut demander à Python (`help(pd)` par exemple pour avoir de l'aide sur pandas ou `help(pd.read_csv)` pour avoir de l'aide sur la fonction spécifique `read_csv`), mais il y a généralement beaucoup moins indigeste : l'aide en ligne des modules ([pour Pandas par exemple]((https://pandas.pydata.org/docs/user_guide/index.html))).

```python
# paramètres par défaut pour les graphes
plt.rcParams['figure.figsize'] = (15, 6)
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.size'] = 13
sns.set_style("white")
```

Le premier jeu de données qu'on va utiliser est issu du [World Happiness report](https://worldhappiness.report) (une publication annuelle de l'ONU mesurant le degrés de bonheur de la population mondiale par pays à partir de sondages).

```python
url = "https://raw.githubusercontent.com/Info-TSI-Vieljeux/s1-tp3/main/2020.csv"
data_monde = pd.read_csv(url,sep=";",index_col=0) # data_monde est une dataframe Pandas
# Une dataframe est une sorte de dictionnaire dont les clés sont les en-têtes des colonnes et dont les lignes sont indexées.
```

```python
data_monde
```
{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>Écart-type</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
      <th>Score de bonheur en Distopie</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>Western Europe</td>
      <td>7.8087</td>
      <td>0.031156</td>
      <td>10.639267</td>
      <td>0.954330</td>
      <td>71.900825</td>
      <td>0.949172</td>
      <td>-0.059482</td>
      <td>0.195445</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>Denmark</th>
      <td>Western Europe</td>
      <td>7.6456</td>
      <td>0.033492</td>
      <td>10.774001</td>
      <td>0.955991</td>
      <td>72.402504</td>
      <td>0.951444</td>
      <td>0.066202</td>
      <td>0.168489</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>Switzerland</th>
      <td>Western Europe</td>
      <td>7.5599</td>
      <td>0.035014</td>
      <td>10.979933</td>
      <td>0.942847</td>
      <td>74.102448</td>
      <td>0.921337</td>
      <td>0.105911</td>
      <td>0.303728</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>Iceland</th>
      <td>Western Europe</td>
      <td>7.5045</td>
      <td>0.059616</td>
      <td>10.772559</td>
      <td>0.974670</td>
      <td>73.000000</td>
      <td>0.948892</td>
      <td>0.246944</td>
      <td>0.711710</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td>Western Europe</td>
      <td>7.4880</td>
      <td>0.034837</td>
      <td>11.087804</td>
      <td>0.952487</td>
      <td>73.200783</td>
      <td>0.955750</td>
      <td>0.134533</td>
      <td>0.263218</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Central African Republic</th>
      <td>Sub-Saharan Africa</td>
      <td>3.4759</td>
      <td>0.115183</td>
      <td>6.625160</td>
      <td>0.319460</td>
      <td>45.200001</td>
      <td>0.640881</td>
      <td>0.082410</td>
      <td>0.891807</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>Rwanda</th>
      <td>Sub-Saharan Africa</td>
      <td>3.3123</td>
      <td>0.052425</td>
      <td>7.600104</td>
      <td>0.540835</td>
      <td>61.098846</td>
      <td>0.900589</td>
      <td>0.055484</td>
      <td>0.183541</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>Sub-Saharan Africa</td>
      <td>3.2992</td>
      <td>0.058674</td>
      <td>7.865712</td>
      <td>0.763093</td>
      <td>55.617260</td>
      <td>0.711458</td>
      <td>-0.072064</td>
      <td>0.810237</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>South Sudan</th>
      <td>Sub-Saharan Africa</td>
      <td>2.8166</td>
      <td>0.107610</td>
      <td>7.425360</td>
      <td>0.553707</td>
      <td>51.000000</td>
      <td>0.451314</td>
      <td>0.016519</td>
      <td>0.763417</td>
      <td>1.972317</td>
    </tr>
    <tr>
      <th>Afghanistan</th>
      <td>South Asia</td>
      <td>2.5669</td>
      <td>0.031311</td>
      <td>7.462861</td>
      <td>0.470367</td>
      <td>52.590000</td>
      <td>0.396573</td>
      <td>-0.096429</td>
      <td>0.933687</td>
      <td>1.972317</td>
    </tr>
  </tbody>
</table>
<p>153 rows × 10 columns</p>

</div>
{{< /rawhtml >}}

Précisions sur ces données :
- le **score de bonheur** est un score sur 10 correspondant à la moyenne des réponses des sondés (0 correspond à la pire vie possible et 10 à la meilleure)
- ce n'est pas le **PIB par habitant** mais son **logarithme** qui est utilisé pour ne pas avoir des valeurs sur des ordres de grandeur trop différents d'une colonne à l'autre
- **entraide sociale** : moyenne des réponses à la question binaire "en cas de difficultés, pouvez-vous compter sur de la famille ou des amis pour vous aider ?" (0 : non, 1 : oui)
- **liberté des choix de vie** : moyenne des réponses à la question binaire "êtes-vous satisfait ou non de votre liberté à choisir ce que vous voulez faire de votre vie ?" (0 : non, 1 : oui)
- **générosité** : moyenne des réponses à "Avez-vous donné à une association caritative le mois dernier ?" ajustée par rapport au PIB par habitant (valeur résiduelle)
- **corruption perçue** : moyenne des réponses à la question binaire "la corruption est-elle répandue dans le gouvernement ?" (0 : non, 1 : oui)

On simplifie un peu le jeu de données en retirant la colonne 'Écart-type' et 'Score de bonheur en distopie' (score minimal obtenu).


```python
data_monde.drop(columns=['Écart-type','Score de bonheur en Distopie'], inplace=True)
data_monde.head(3)
```
{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>Western Europe</td>
      <td>7.8087</td>
      <td>10.639267</td>
      <td>0.954330</td>
      <td>71.900825</td>
      <td>0.949172</td>
      <td>-0.059482</td>
      <td>0.195445</td>
    </tr>
    <tr>
      <th>Denmark</th>
      <td>Western Europe</td>
      <td>7.6456</td>
      <td>10.774001</td>
      <td>0.955991</td>
      <td>72.402504</td>
      <td>0.951444</td>
      <td>0.066202</td>
      <td>0.168489</td>
    </tr>
    <tr>
      <th>Switzerland</th>
      <td>Western Europe</td>
      <td>7.5599</td>
      <td>10.979933</td>
      <td>0.942847</td>
      <td>74.102448</td>
      <td>0.921337</td>
      <td>0.105911</td>
      <td>0.303728</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}

```python
data_monde.tail(3)
```
{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Zimbabwe</th>
      <td>Sub-Saharan Africa</td>
      <td>3.2992</td>
      <td>7.865712</td>
      <td>0.763093</td>
      <td>55.61726</td>
      <td>0.711458</td>
      <td>-0.072064</td>
      <td>0.810237</td>
    </tr>
    <tr>
      <th>South Sudan</th>
      <td>Sub-Saharan Africa</td>
      <td>2.8166</td>
      <td>7.425360</td>
      <td>0.553707</td>
      <td>51.00000</td>
      <td>0.451314</td>
      <td>0.016519</td>
      <td>0.763417</td>
    </tr>
    <tr>
      <th>Afghanistan</th>
      <td>South Asia</td>
      <td>2.5669</td>
      <td>7.462861</td>
      <td>0.470367</td>
      <td>52.59000</td>
      <td>0.396573</td>
      <td>-0.096429</td>
      <td>0.933687</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}


Traçons un histogramme brut du jeu de données complet pour y voir plus clair (la librairie Seaborn rend cela très simple).
```python
sns.histplot(data=data_monde)
```
![](/histoseaborn.png)

La méthode `describe` s'appliquant à des dataframe pandas retourne un résumé statistique très pratique des données de chaque colonne :


```python
data_monde.describe()
```
{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>153.00000</td>
      <td>153.000000</td>
      <td>153.000000</td>
      <td>153.000000</td>
      <td>153.000000</td>
      <td>153.000000</td>
      <td>153.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.47324</td>
      <td>9.295706</td>
      <td>0.808721</td>
      <td>64.445529</td>
      <td>0.783360</td>
      <td>-0.014568</td>
      <td>0.733120</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.11227</td>
      <td>1.201588</td>
      <td>0.121453</td>
      <td>7.057848</td>
      <td>0.117786</td>
      <td>0.151809</td>
      <td>0.175172</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.56690</td>
      <td>6.492642</td>
      <td>0.319460</td>
      <td>45.200001</td>
      <td>0.396573</td>
      <td>-0.300907</td>
      <td>0.109784</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.72410</td>
      <td>8.350645</td>
      <td>0.737217</td>
      <td>58.961712</td>
      <td>0.714839</td>
      <td>-0.127015</td>
      <td>0.683019</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.51500</td>
      <td>9.456313</td>
      <td>0.829204</td>
      <td>66.305145</td>
      <td>0.799805</td>
      <td>-0.033665</td>
      <td>0.783122</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.22850</td>
      <td>10.265124</td>
      <td>0.906747</td>
      <td>69.289192</td>
      <td>0.877709</td>
      <td>0.085429</td>
      <td>0.849151</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.80870</td>
      <td>11.450681</td>
      <td>0.974670</td>
      <td>76.804581</td>
      <td>0.974998</td>
      <td>0.560664</td>
      <td>0.935585</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}

>Pour confirmer certaines des valeurs, vous allez construire différentes fonctions :
>- une fonction `decompte` qui retourne le nombre d'éléments d'une liste,
>- une fonction `moyenne` qui retourne la moyenne des éléments d'une liste,
>- une fonction `mediane` qui retourne la médiane des éléments d'une liste triée en ordre croissant.
>
>L'utilisation de fonctions statistiques déjà existantes est bien sûr prohibée.

```python
def decompte(L):
    """
    decompte(L: liste) -> entier
    """
    # CODE

def moyenne(L):
    """
    decompte(L: liste) -> flottant
    """
    # CODE
    
def mediane(L):
    """
    decompte(L: liste) -> floattant ou entier (suivant les valeurs de L)
    """
    # CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">def decompte(L):
    return len(L)
</code></pre>
<pre><code class="language-python">def moyenne(L):
    s = 0
    for e in L:
        s += e
    return s/len(L)
</code></pre>
<pre><code class="language-python">def mediane(L):
    N = decompte(L)
    return L[N//2]
</code></pre>
</blockquote>
</details>


>Calculez, pour les 3 formes d'importation du module, l'écart-type des éléments de la liste `Liste_scores` en utilisant la fonction `stdev` du module `statistics`.\
Il s'agit d'évaluer directement l'expresion (le nombre doit s'afficher sous la cellule sans utiliser de `print`).

```python
import statistics
# CODE
```

```python
from statistics import *
# CODE
```

```python
import statistics as st
# CODE
```

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
<pre><code class="language-python">import statistics
statistics.stdev(Liste_scores)
</code></pre>
<pre><code class="language-python">from statistics import *
# Rq : on évite le plus souvent ce type d'importation qui peut générer des conflits de définition.
stdev(Liste_scores)
</code></pre>
<pre><code class="language-python">import statistics as st
# C'est la forme la plus pratique si le module est souvent utilisé
st.stdev(Liste_scores)
</code></pre>
</blockquote>
</details>


Traçons maintenant un diagramme en bâtons des scores de bonheur des 60 premiers pays.

```python
fig,ax = plt.subplots(figsize=(20,4))
sns.barplot(ax = ax,x = data_monde.index[:60], y = data_monde['Score de bonheur'].head(60))
plt.xticks(rotation=90)
ax.set_xlabel('')
```
![](/batonmonde.png)

On remarque que les pays sont classés par score de bonheur décroissant dans le jeu de données d'origine.\
Mais on peut évidemment choisir un autre critère de classement si on le désire :


```python
data_monde.sort_values(by="PIB par habitant (log)",ascending=True).head(10)
```

{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Burundi</th>
      <td>Sub-Saharan Africa</td>
      <td>3.7753</td>
      <td>6.492642</td>
      <td>0.490326</td>
      <td>53.400002</td>
      <td>0.626350</td>
      <td>-0.017552</td>
      <td>0.606935</td>
    </tr>
    <tr>
      <th>Central African Republic</th>
      <td>Sub-Saharan Africa</td>
      <td>3.4759</td>
      <td>6.625160</td>
      <td>0.319460</td>
      <td>45.200001</td>
      <td>0.640881</td>
      <td>0.082410</td>
      <td>0.891807</td>
    </tr>
    <tr>
      <th>Congo (Kinshasa)</th>
      <td>Sub-Saharan Africa</td>
      <td>4.3110</td>
      <td>6.694256</td>
      <td>0.672159</td>
      <td>52.900002</td>
      <td>0.700794</td>
      <td>0.083638</td>
      <td>0.809404</td>
    </tr>
    <tr>
      <th>Niger</th>
      <td>Sub-Saharan Africa</td>
      <td>4.9096</td>
      <td>6.842167</td>
      <td>0.617435</td>
      <td>53.500095</td>
      <td>0.759772</td>
      <td>0.013861</td>
      <td>0.722530</td>
    </tr>
    <tr>
      <th>Liberia</th>
      <td>Sub-Saharan Africa</td>
      <td>4.5579</td>
      <td>7.054380</td>
      <td>0.709281</td>
      <td>56.096313</td>
      <td>0.735269</td>
      <td>0.042273</td>
      <td>0.856376</td>
    </tr>
    <tr>
      <th>Malawi</th>
      <td>Sub-Saharan Africa</td>
      <td>3.5380</td>
      <td>7.062226</td>
      <td>0.544007</td>
      <td>57.592888</td>
      <td>0.803223</td>
      <td>0.021433</td>
      <td>0.731701</td>
    </tr>
    <tr>
      <th>Mozambique</th>
      <td>Sub-Saharan Africa</td>
      <td>4.6236</td>
      <td>7.069346</td>
      <td>0.723874</td>
      <td>54.205822</td>
      <td>0.864452</td>
      <td>0.032376</td>
      <td>0.683019</td>
    </tr>
    <tr>
      <th>Sierra Leone</th>
      <td>Sub-Saharan Africa</td>
      <td>3.9264</td>
      <td>7.268803</td>
      <td>0.636142</td>
      <td>50.865143</td>
      <td>0.715315</td>
      <td>0.088661</td>
      <td>0.861331</td>
    </tr>
    <tr>
      <th>Madagascar</th>
      <td>Sub-Saharan Africa</td>
      <td>4.1656</td>
      <td>7.281686</td>
      <td>0.668196</td>
      <td>59.105427</td>
      <td>0.557574</td>
      <td>-0.011824</td>
      <td>0.817486</td>
    </tr>
    <tr>
      <th>Gambia</th>
      <td>Sub-Saharan Africa</td>
      <td>4.7506</td>
      <td>7.321815</td>
      <td>0.693169</td>
      <td>55.012016</td>
      <td>0.733163</td>
      <td>0.343199</td>
      <td>0.690718</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}



```python
data_monde.sort_values(by="Corruption perçue",ascending=False).head()
```
{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bulgaria</th>
      <td>Central and Eastern Europe</td>
      <td>5.1015</td>
      <td>9.869319</td>
      <td>0.937840</td>
      <td>66.803978</td>
      <td>0.745178</td>
      <td>-0.143908</td>
      <td>0.935585</td>
    </tr>
    <tr>
      <th>Romania</th>
      <td>Central and Eastern Europe</td>
      <td>6.1237</td>
      <td>10.107584</td>
      <td>0.825162</td>
      <td>67.207237</td>
      <td>0.842823</td>
      <td>-0.197815</td>
      <td>0.934300</td>
    </tr>
    <tr>
      <th>Bosnia and Herzegovina</th>
      <td>Central and Eastern Europe</td>
      <td>5.6741</td>
      <td>9.455817</td>
      <td>0.829204</td>
      <td>67.808136</td>
      <td>0.651353</td>
      <td>0.098275</td>
      <td>0.933769</td>
    </tr>
    <tr>
      <th>Afghanistan</th>
      <td>South Asia</td>
      <td>2.5669</td>
      <td>7.462861</td>
      <td>0.470367</td>
      <td>52.590000</td>
      <td>0.396573</td>
      <td>-0.096429</td>
      <td>0.933687</td>
    </tr>
    <tr>
      <th>Kosovo</th>
      <td>Central and Eastern Europe</td>
      <td>6.3252</td>
      <td>9.204430</td>
      <td>0.820727</td>
      <td>63.885555</td>
      <td>0.861536</td>
      <td>0.190934</td>
      <td>0.922328</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}

```python
data_monde.sort_values(by="Générosité",ascending=False).iloc[[45]]
```
{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Denmark</th>
      <td>Western Europe</td>
      <td>7.6456</td>
      <td>10.774001</td>
      <td>0.955991</td>
      <td>72.402504</td>
      <td>0.951444</td>
      <td>0.066202</td>
      <td>0.168489</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}

D'après la cellule précédente, le 46<sup>e</sup> (le 1<sup>er</sup> est à l'indice 0) meilleur score de générosité appartient au Danemark.

> Quel pays correspond à la 59<sup>e</sup> plus courte espérance de vie en bonne santé ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On obtient son nom grâce à l'expression suivante&nbsp;:<br>
<code>data_monde.sort_values(by="Espérance de vie en bonne santé",ascending=True).iloc[[58]]</code><br>
Il s'agit de <code>'Russia'</code>.
</blockquote>
</details>

On peut aussi aisément filtrer le jeu de données en fonction de n'importe quel critère :

```python
data_monde[(data_monde["Espérance de vie en bonne santé"]>60) & (data_monde["Espérance de vie en bonne santé"]<61)]
# Rq : pandas nécessite les opérateurs logiques bit à bit '&' (et) et '|' (ou) 
# plutôt que les opérateurs élément par élément 'and' et 'or' qui lèveraient une erreur.
```
{{< rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Kenya</th>
      <td>Sub-Saharan Africa</td>
      <td>4.5830</td>
      <td>8.029776</td>
      <td>0.702652</td>
      <td>60.096931</td>
      <td>0.829748</td>
      <td>0.294682</td>
      <td>0.831499</td>
    </tr>
    <tr>
      <th>India</th>
      <td>South Asia</td>
      <td>3.5733</td>
      <td>8.849824</td>
      <td>0.592201</td>
      <td>60.215187</td>
      <td>0.881445</td>
      <td>0.057552</td>
      <td>0.772043</td>
    </tr>
  </tbody>
</table>
</div>
{{< /rawhtml >}}

> Quel pays possède un score de bonheur inférieur à 5 malgré une valeur de corruption perçue inférieure à 0.5 ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On obtient son nom grâce à l'expression suivante&nbsp;:<br>
<code>data_monde[(data_monde["Score de bonheur"]<5) & (data_monde["Corruption perçue"]<0.5)]</code><br>
Il s'agit de <code>'Rwanda'</code>.
</blockquote>
</details>


Pour récupérer l'ensemble des données d'un pays en particulier, on utilise :

```python
data_monde.loc['France']
```
```python
Région du monde                    Western Europe
Score de bonheur                           6.6638
PIB par habitant (log)                  10.584223
Entraide sociale                         0.937104
Espérance de vie en bonne santé         73.801933
Liberté des choix de vie                 0.825468
Générosité                              -0.130642
Corruption perçue                        0.583521
Name: France, dtype: object
```

Pour chaque variable mesurée (chaque colonne), on peut facilement tracer des histogrammes illustrant la répartition des valeurs.

```python
sns.displot(data_monde, x="Score de bonheur", bins=20,  kde=True, height=4, aspect=3)
# bins contrôle le nombre de classes
```
![](/histobonhseab.png)

On peut faciliter la lecture des graphes en les rendant interactif.

On utilise pour cela la bibliothèque `Plotly express` qui sait (comme seaborn) parler à une dataframe pandas.\
On peut zoomer sur ces graphiques interactifs et obtenir des informations en survolant avec le curseur.


```python
px.histogram(data_monde,'Corruption perçue',nbins=40,title="Corruption perçue")
# Cette fois-ci, le nombre de classes est désigné par nbins.
```
{{< load-plotly >}}
{{< plotly json="/corrup.json" height="600px" >}}

>Modifiez le graphe précédent pour répondre à cette question : combien la classe la plus peuplée de l'histogramme de l'espérance de vie en bonne santé compte-elle de valeurs si l'histogramme comporte 30 classes ?


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
On écrit maintenant&nbsp;:<br>
<code>px.histogram(data_monde,'Espérance de vie en bonne santé',nbins=30)</code><br>
Et on n'a plus qu'à survoler la classe la plus peuplée pour découvrir le nombre de valeurs qu'elle contient&nbsp;: 29.
</blockquote>
</details>

&nbsp;
&nbsp;

## Regroupement des données

On remarque que le jeu de données contient une colonne catégorielle : "Région du monde".\
Cela va nous permettre d'explorer de possibles dynamiques régionales : est-ce que les pays d'une même zone ont des indicateurs semblables ?


```python
pd.unique(data_monde["Région du monde"]) # permet d'afficher une seule fois chacune des valeurs différentes de la colonne
```

<div id="debord">
<code>array(['Western Europe', 'North America and ANZ','Middle East and North Africa', 'Latin America and Caribbean','Central and Eastern Europe', 'East Asia', 'Southeast Asia','Commonwealth of Independent States', 'Sub-Saharan Africa','South Asia'], dtype=object)</code>
</div>

Traçons des diagrammes en boîte à moustaches représentant les scores de bonheur pour chacune des régions.

{{% notice note %}}
Construction des boîtes à moustaches (ou diagrammes en boîtes de Tukey) :\
Les frontières de la boites sont formées des premier Q1 et troisième quartile Q3 et la barre dans la boite correspond à la médiane (50% des valeurs sont donc dans la boîte).\
Pour les moustaches, on calcule d'abord 1,5 fois la distance interquartile entre le premier et le troisième quartile (la longueur de la boîte) : L=1,5×(Q3-Q1). Si les valeurs ne s'étendent pas au-delà de Q1-L et Q3+L, on trace les moustaches aux valeurs min et max. Sinon, on trace les moustaches au niveau des valeurs précédant immédiatement la limite. Les valeurs au-delà sont représentées par des points et sont le plus souvent considérées comme des anomalies.
{{% /notice %}}

À nouveau Seaborn rend cela très simple...


```python
sns.set_style("white")
fig, ax = plt.subplots(figsize=(12,8))
sns.boxplot(ax = ax, x="Score de bonheur", y="Région du monde", palette="husl", data=data_monde)
sns.despine(offset=10, trim=True)
ax.set_ylabel('')
```
![](/moustacheseab.png)

Traçons maintenant un graphe plus général représentant toutes les relations possibles entre deux axes du jeu de données pour voir si certaines combinaisons discriminent plus nettement les différentes régions.


```python
# Un peu long à s'exécuter (environ 30 s)
g = sns.pairplot(data_monde, hue="Région du monde", corner=True)
g._legend.set_bbox_to_anchor((0.6, 0.8))
```

![png](/pairplotseab.png)

On constate que les groupes régionaux sont relativement homogènes pour la plupart des critères.

Zoomons sur un de ces graphes :

```python
sns.set_style("whitegrid")
sns.jointplot(data=data_monde,x="PIB par habitant (log)", y="Score de bonheur", hue="Région du monde", kind='scatter', height=8, legend=False)
```
![png](/zoompairplot.png)

Une version interactive du même graphique permet de consulter les informations pour chaque point :
```python
px.scatter(data_monde,x='PIB par habitant (log)', y='Score de bonheur', hover_name=data_monde.index, color='Région du monde')
```

{{< plotly json="/zoompairplot.json" height="600px" >}}

> Trouvez la région du monde représentée sur le graphe suivant (le graphe interactif permet de trouver la réponse facilement).
![](/graphemystere.png?width=600)


<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Il s'agit de 'Latin America and Caribbean'.
</blockquote>
</details>

Allons maintenant au-delà de la proximité géographique pour regrouper les pays en 3 grands blocs socioéconomiques : "Nord", "Sud", "Intermédiaire".

```python
conditions = [(data_monde['Région du monde'] == 'Western Europe') | (data_monde['Région du monde'] == 'North America and ANZ'),(data_monde['Région du monde'] == 'South Asia') | (data_monde['Région du monde'] == 'Sub-Saharan Africa')]
choix = ['"Nord"', '"Sud"']
data_monde['Groupe'] = np.select(conditions, choix, default='Autres')
```

```python
# Un peu long à s'exécuter (environ 30 s)
sns.set_style("white")
g = sns.PairGrid(data_monde, diag_sharey=False, hue="Groupe")
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot,common_norm=False)
g.map_diag(sns.histplot,bins=20,kde=True)
g.add_legend(title="Grands groupes",adjust_subtitles=True)
```

![png](/troisblocs.png)

L'homogénéité de ces 3 groupes saute aux yeux.

&nbsp;
&nbsp;

## Corrélations

Les graphiques précédents mettent en évidence des corrélations assez fortes entre certaines grandeurs.<br>
Creusons un peu.


```python
g = sns.PairGrid(data_monde, y_vars=["Score de bonheur"], x_vars=["PIB par habitant (log)", "Corruption perçue"], height=7, aspect=1.5)
g.map(sns.regplot)
```

![png](/pairgrid.png)

On constate sur cet exemple que le score de bonheur est corrélé positivement avec le PIB par habitant et négativement avec le degré de corruption perçue.

Pour avoir un panorama complet, traçons la matrice de corrélation donnant, pour chaque couple de variable, la valeur du coefficient de corrélation $r$ (valeur entre -1 et 1 traduisant le degré de dépendance linéaire entre deux variables) :


```python
fig, ax = plt.subplots(figsize=(12,10))   
cmap = sns.diverging_palette(0, 230, 90, 60, as_cmap=True).reversed() # choix de la palette de couleurs
sns.heatmap(data_monde.iloc[:,1:].corr(), cmap=cmap, center=0, annot=True, fmt=".2f", linewidth = 0.5, ax=ax)
```
![png](/heatmap.png)

> Citez les deux variables les moins corrélées entre elles (donner les noms exacts tels qu'ils apparaissent dans les données, attention à la casse). L'ordre des variables n'est pas important.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Voilà le test utiliser pour vérifier la réponse&nbsp;:
<pre><code class="language-python">assert variable1 == "Générosité" or variable1 == "Entraide sociale"
if variable1 == "Générosité":
    assert variable2 == "Entraide sociale"
else:
    assert variable2 == "Générosité"
</code></pre>
</blockquote>
</details>

&nbsp;
&nbsp;

*Fin du TP3a*
***
# Un chouïa d'apprentissage automatique<br>(machine learning)

On a vu qu'un regroupement des données en 3 grands groupes "Nord", "Sud" et "Intermédiaire" semble plutôt cohérent.<br>
Mais pourquoi pas laisser un algorithme décider lui-même de qui va le mieux ensemble ? Ensuite nous pourrons vérifier si cela recoupe notre découpage fait à la main.<br>
On appelle cela un **apprentissage non supervisé**.

Nous allons utiliser l'algorithme des **k-moyennes** pour partitionner automatiquement nos données.<br>
Il consiste à placer chaque point de données dans un espace à $n$ dimensions où $n$ est le nombre de variables (les descripteurs) et chercher à les regrouper en **clusters** en fonction de leurs distances.<br>
Chaque variable correspondant à un axe du repère. 

Pour aider l'algorithme, on peut tenter de réduire la dimension de l'espace dans lequel chaque point de données est plongé en utilisant une **analyse en composantes principales**.<br>
L'idée est de déterminer les combinaisons des différentes variables expliquant le mieux la variance des données. Chaque nouvel axe ainsi formé (les composantes principales) explique une part décroissante mais complémentaire de la variance (sur la deuxième composante, les données sont moins étalées que sur la première, mais elles s'étalent dans une direction orthogonale, et ainsi de suite).<br>
Projeter les données sur les premières composantes permet de les étaler le plus possible. On peut ainsi réduire l'espace à *n* dimensions du départ à un espace de seulement 2 ou 3 dimensions expliquant la majorité de la variance des données.

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
<a href="https://youtu.be/sRMplEDuEig">Une vidéo</a> pour ceux qui voudraient en savoir plus sur ce sujet.
</blockquote>
</details>

L'animation suivante montre comment serait sélectionné l'axe de la composante principale dans un espace à deux dimensions : il correspond à la position de la droite pour  laquelle la distance cumulée de tous les points à la droite est la plus grande.

![](/acp.gif)

La bibliothèque `Scikit-learn`, destinée à l'apprentissage automatique, contient tout ce qu'il nous faut :


```python
from sklearn.decomposition import PCA # l'algorithme d'analyse en composantes principales (PCA en anglais)
from sklearn.preprocessing import StandardScaler # pour centrer-réduire les données
from sklearn.cluster import KMeans # l'algorithme des k-moyennes
```


```python
variables = data_monde.columns.values[1:-1]
scaler = StandardScaler()
X = scaler.fit_transform(data_monde[variables]) 
# chaque vecteur correspondant à chacune des variables est maintenant centré-réduit
pca = PCA()
components = pca.fit_transform(X)
```

Quelle combinaison des variables de départ utilise la première composante&nbsp;? Les quelqus lignes suivantes permettent de le déterminer.


```python
data = data_monde.copy() # pour pouvoir revenir sur le graphe suivant même après ajout de colonnes à data_monde
```


```python
n_c = 1 # numéro de la composante principale à décrire
px.bar(components.T, x=data.columns.values[1:-1], y=n_c-1, labels={f"{n_c-1}": f"Composante Principale (CP) {n_c}"})
```


{{< plotly json="/compppale.json" height="600px" >}}

> Quelle est le nom de la variable participant le plus à la composante principale n°34 ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
La 'Générosité'.
</blockquote>
</details>

Représentons le pourcentage de variance expliquée par chacune des composantes :


```python
exp_var_cumul = np.cumsum(pca.explained_variance_ratio_)
fig = px.bar(x=range(1, exp_var_cumul.shape[0] + 1),y=pca.explained_variance_ratio_,labels={"x": "composante", "y": "% variance expliquée"})
fig.add_scatter(x=list(range(1, exp_var_cumul.shape[0] + 1)), y=exp_var_cumul, name="", showlegend=False)
```
{{< load-plotly >}}
{{< plotly json="/explvariance.json" height="600px" >}}

Les trois premières composantes expliquent plus de 80% de la variance !

Plaçons les données dans un espace réduit à ces 3 dimensions :

```python
px.scatter_3d(components, x=0, y=1, z=2, 
              color=data_monde['Groupe'],
              labels={'0': 'CP 1', '1': 'CP 2', '2': 'CP 3'},
              hover_name=data_monde.index)
```

{{< plotly json="/scat3Dgpe.json" height="600px" >}}

On constate à nouveau que nos 3 groupes discriminent plutôt très bien nos données même si quelques chevauchements existent.

C'est le moment d'utiliser l'algorithme des k-moyennes pour essayer de former 3 groupes homogènes :

```python
# on ne garde que les 3 premières composantes principales
pca = PCA(n_components = 3)
pca.fit(X)
score_pca = pca.transform(X)
kmeans_pca = KMeans(n_clusters=3,init='k-means++',random_state=42)
kmeans_pca.fit(score_pca)
data_monde["Cluster"]=kmeans_pca.labels_.astype(str)
data_monde.head(3)
```
{{<rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
      <th>Groupe</th>
      <th>Cluster</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>Western Europe</td>
      <td>7.8087</td>
      <td>10.639267</td>
      <td>0.954330</td>
      <td>71.900825</td>
      <td>0.949172</td>
      <td>-0.059482</td>
      <td>0.195445</td>
      <td>"Nord"</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Denmark</th>
      <td>Western Europe</td>
      <td>7.6456</td>
      <td>10.774001</td>
      <td>0.955991</td>
      <td>72.402504</td>
      <td>0.951444</td>
      <td>0.066202</td>
      <td>0.168489</td>
      <td>"Nord"</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Switzerland</th>
      <td>Western Europe</td>
      <td>7.5599</td>
      <td>10.979933</td>
      <td>0.942847</td>
      <td>74.102448</td>
      <td>0.921337</td>
      <td>0.105911</td>
      <td>0.303728</td>
      <td>"Nord"</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml >}}


```python
fig = px.scatter_3d(components, x=0, y=1, z=2, 
              color=data_monde['Cluster'],
              labels={'0': 'CP 1', '1': 'CP 2', '2': 'CP 3'},
              color_discrete_sequence=px.colors.qualitative.Bold,
              hover_name=data_monde.index)
fig.update_layout(legend_title = "Cluster")
```

{{< plotly json="/scat3Dclust.json" height="600px" >}}

Les 3 clusters créés reproduisent à peu de chose près les 3 groupes "Nord", "Sud", "Intermédiaire" construits à la main.
> À quel cluster correspondent approximativement les pays du groupe "Sud" ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Au cluster "1".
</blockquote>
</details>

Mais l'accord n'est pas parfait !
> Citez un pays qui appartient au groupe "Nord" mais qui n'appartient pas au cluster lui correspondant.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Un des pays suivant : "Spain", "Italy", "Cyprus", "North Cyprus", "Portugal", "Greece".<br>
On remarque qu'il s'agit exclusivement de pays du sud de l'Europe.
</blockquote>
</details>

Nous allons voir dans la prochaine partie du TP comment représenter ces données sur une carte pour y voir plus clair.

&nbsp;
&nbsp;

*Fin du TP3b*
***
# Un peu de géographie


Le module suivant va permettre d'ajouter à nos données le code à 3 lettres (SO 3166-1 alpha-3) de chaque pays.\
Mais pourquoi donc ? `plotly express` permet de tracer la carte d'un pays directement à partir de ce petit code de 3 lettres !


```python
import country_converter as coco
```

```python
iso3 = coco.convert(names=data_monde.index, to='ISO3', not_found=None)
data_monde["code"] = iso3
data_monde.head()
```
{{<rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
      <th>Groupe</th>
      <th>Cluster</th>
      <th>code</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>Western Europe</td>
      <td>7.8087</td>
      <td>10.639267</td>
      <td>0.954330</td>
      <td>71.900825</td>
      <td>0.949172</td>
      <td>-0.059482</td>
      <td>0.195445</td>
      <td>"Nord"</td>
      <td>2</td>
      <td>FIN</td>
    </tr>
    <tr>
      <th>Denmark</th>
      <td>Western Europe</td>
      <td>7.6456</td>
      <td>10.774001</td>
      <td>0.955991</td>
      <td>72.402504</td>
      <td>0.951444</td>
      <td>0.066202</td>
      <td>0.168489</td>
      <td>"Nord"</td>
      <td>2</td>
      <td>DNK</td>
    </tr>
    <tr>
      <th>Switzerland</th>
      <td>Western Europe</td>
      <td>7.5599</td>
      <td>10.979933</td>
      <td>0.942847</td>
      <td>74.102448</td>
      <td>0.921337</td>
      <td>0.105911</td>
      <td>0.303728</td>
      <td>"Nord"</td>
      <td>2</td>
      <td>CHE</td>
    </tr>
    <tr>
      <th>Iceland</th>
      <td>Western Europe</td>
      <td>7.5045</td>
      <td>10.772559</td>
      <td>0.974670</td>
      <td>73.000000</td>
      <td>0.948892</td>
      <td>0.246944</td>
      <td>0.711710</td>
      <td>"Nord"</td>
      <td>2</td>
      <td>ISL</td>
    </tr>
    <tr>
      <th>Norway</th>
      <td>Western Europe</td>
      <td>7.4880</td>
      <td>11.087804</td>
      <td>0.952487</td>
      <td>73.200783</td>
      <td>0.955750</td>
      <td>0.134533</td>
      <td>0.263218</td>
      <td>"Nord"</td>
      <td>2</td>
      <td>NOR</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml >}}

```python
fig = px.choropleth(data_monde,
                    locations = "code",
                    color = "Score de bonheur",
                    projection = "orthographic",
                    color_continuous_scale = "Spectral_r",
                    hover_name = data_monde.index,
                    hover_data = {"code" : False})

fig.update_geos(
    showland = True, landcolor = "LightGrey",
    showocean = True, oceancolor = "LightBlue",
    showlakes = True, lakecolor = "LightBlue",
    showframe = False)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

{{< plotly json="/cartechoro1.json" height="600px" >}}

On est maintenant paré pour représenter les 3 clusters obtenus par l'algo des k-moyennes du tp3b.

```python
data_monde["Cluster"] = [f'n°{cluster}' for cluster in data_monde["Cluster"].astype('int64') if cluster != 'nan']
data_monde.head(1)
```
{{<rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Région du monde</th>
      <th>Score de bonheur</th>
      <th>PIB par habitant (log)</th>
      <th>Entraide sociale</th>
      <th>Espérance de vie en bonne santé</th>
      <th>Liberté des choix de vie</th>
      <th>Générosité</th>
      <th>Corruption perçue</th>
      <th>Groupe</th>
      <th>Cluster</th>
      <th>code</th>
    </tr>
    <tr>
      <th>Pays</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Finland</th>
      <td>Western Europe</td>
      <td>7.8087</td>
      <td>10.639267</td>
      <td>0.95433</td>
      <td>71.900825</td>
      <td>0.949172</td>
      <td>-0.059482</td>
      <td>0.195445</td>
      <td>"Nord"</td>
      <td>n°2</td>
      <td>FIN</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml >}}

```python
fig = px.choropleth(data_monde,
                    locations = "code",
                    color = "Cluster",
                    projection = "natural earth",
                    color_discrete_sequence = px.colors.qualitative.Set2,
                    hover_name = data_monde.index,
                    hover_data = {"code" : False}
                   )
#fig.update_geos(fitbounds="locations", visible=True)
fig.update_layout(margin = {"r":0,"t":0,"l":0,"b":0})
fig.update_geos(showframe = False)
fig.show()
```

{{< plotly json="/cartechoro2.json" height="600px" >}}

Terminons en fabriquant une carte régionale.

```python
for reg in pd.unique(data_monde["Région du monde"]):
    print(reg)
```
`Western Europe`<br>
`North America and ANZ`<br>
`Middle East and North Africa`<br> 
`Latin America and Caribbean`<br>
`Central and Eastern Europe`<br>
`East Asia`<br>
`Southeast Asia`<br>
`Commonwealth of Independent States`<br>
`Sub-Saharan Africa`<br>
`South Asia`<br>

```python
region = data_monde[data_monde["Région du monde"] == "Middle East and North Africa"]
```

```python
fig = px.choropleth(region,
                    locations = "code",
                    color = "Score de bonheur",
                    projection = "natural earth",
                    color_continuous_scale = "Temps",
                    hover_name = region.index,
                    hover_data = {"code" : False}
                   )
fig.update_geos(fitbounds = "locations", visible = True)
fig.update_layout(margin = {"r":0,"t":0,"l":0,"b":0})
fig.update_geos(showframe = False, resolution = 50)
fig.show()
```

{{< plotly json="/cartechoro3.json" height="600px" >}}

> Modifiez les cellules qui précèdent pour que le graphique ci-dessus affiche la carte du score de générosité des pays d'Asie du sud-est.

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Voilà les lignes modifiées&nbsp;:
<pre><code class="language-python">region = data_monde[data_monde["Région du monde"] == "Southeast Asia"]
fig = px.choropleth(region,
                    locations="code",
                    color="Générosité",
                    projection="natural earth",
                    color_continuous_scale="Temps",
                    hover_name = region.index,
                    hover_data ={"code" : False}
                   )
fig.update_geos(fitbounds="locations", visible=True)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(showframe = False, resolution=50)
fig.show()
</code></pre>
</blockquote>
</details>


> De quelle couleur est le Vietnam sur cette carte ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
vert
</blockquote>
</details>

&nbsp;
&nbsp;

*Fin du TP3c*
***
# Série temporelle

Utilisons un nouveau jeu de données comprenant des relevés de consommation électrique allemands entre 2006 et 2018 :

```python
url = "http://cordier-phychi.toile-libre.org/Info/github/elec_allemagne.csv"
serie_temp = pd.read_csv(url,sep=",")
serie_temp.drop(columns="Wind+Solar",inplace=True)
serie_temp
```
{{<rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Consumption</th>
      <th>Wind</th>
      <th>Solar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-01-01</td>
      <td>1069.18400</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-01-02</td>
      <td>1380.52100</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2006-01-03</td>
      <td>1442.53300</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2006-01-04</td>
      <td>1457.21700</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-01-05</td>
      <td>1477.13100</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4378</th>
      <td>2017-12-27</td>
      <td>1263.94091</td>
      <td>394.507</td>
      <td>16.530</td>
    </tr>
    <tr>
      <th>4379</th>
      <td>2017-12-28</td>
      <td>1299.86398</td>
      <td>506.424</td>
      <td>14.162</td>
    </tr>
    <tr>
      <th>4380</th>
      <td>2017-12-29</td>
      <td>1295.08753</td>
      <td>584.277</td>
      <td>29.854</td>
    </tr>
    <tr>
      <th>4381</th>
      <td>2017-12-30</td>
      <td>1215.44897</td>
      <td>721.247</td>
      <td>7.467</td>
    </tr>
    <tr>
      <th>4382</th>
      <td>2017-12-31</td>
      <td>1107.11488</td>
      <td>721.176</td>
      <td>19.980</td>
    </tr>
  </tbody>
</table>
<p>4383 rows × 4 columns</p>
</div>
{{</rawhtml >}}

Petit toilettage des données : on transforme les valeurs de la colonne des dates en un type date reconnu par pandas et on les utilise comme index.

```python
serie_temp['Date'] = pd.to_datetime(serie_temp['Date'])
serie_temp = serie_temp.set_index('Date')
serie_temp.head()
```
{{<rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Consumption</th>
      <th>Wind</th>
      <th>Solar</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2006-01-01</th>
      <td>1069.184</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-02</th>
      <td>1380.521</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-03</th>
      <td>1442.533</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-04</th>
      <td>1457.217</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-05</th>
      <td>1477.131</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml >}}

On francise ensuite les noms de colonne...

```python
serie_temp.columns = ["Consommation","Vent","Solaire"]
serie_temp.head()
```
{{<rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Consommation</th>
      <th>Vent</th>
      <th>Solaire</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2006-01-01</th>
      <td>1069.184</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-02</th>
      <td>1380.521</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-03</th>
      <td>1442.533</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-04</th>
      <td>1457.217</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2006-01-05</th>
      <td>1477.131</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml >}}

Et enfin, on ajoute des colonnes "jour", "mois" et "année".

```python
serie_temp['jour'] = serie_temp.index.day_name()
serie_temp['mois'] = serie_temp.index.month
serie_temp['année'] = serie_temp.index.year
serie_temp["date"] = serie_temp.index
serie_temp["date"] = serie_temp["date"].dt.date # pour aider Colab qui a des soucis avec les dates
serie_temp.head()
```
{{<rawhtml >}}
<div id="debord">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Consommation</th>
      <th>Vent</th>
      <th>Solaire</th>
      <th>jour</th>
      <th>mois</th>
      <th>année</th>
      <th>date</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2006-01-01</th>
      <td>1069.184</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunday</td>
      <td>1</td>
      <td>2006</td>
      <td>2006-01-01</td>
    </tr>
    <tr>
      <th>2006-01-02</th>
      <td>1380.521</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Monday</td>
      <td>1</td>
      <td>2006</td>
      <td>2006-01-02</td>
    </tr>
    <tr>
      <th>2006-01-03</th>
      <td>1442.533</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Tuesday</td>
      <td>1</td>
      <td>2006</td>
      <td>2006-01-03</td>
    </tr>
    <tr>
      <th>2006-01-04</th>
      <td>1457.217</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Wednesday</td>
      <td>1</td>
      <td>2006</td>
      <td>2006-01-04</td>
    </tr>
    <tr>
      <th>2006-01-05</th>
      <td>1477.131</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Thursday</td>
      <td>1</td>
      <td>2006</td>
      <td>2006-01-05</td>
    </tr>
  </tbody>
</table>
</div>
{{</rawhtml >}}

```python
px.line(serie_temp[["Consommation","Vent","Solaire"]])
```
{{< plotly json="/linecomplet.json" height="600px" >}}

On constate d'importantes variations saisonnières.

```python
zoom = serie_temp[serie_temp['année']==2016]
fig1 = px.line(zoom,'date','Consommation')
fig2 = px.scatter(zoom,'date','Consommation',color='jour')
fig = go.Figure()
fig.add_traces([fig1.data[0],*[fig2.data[i] for i in range(7)]])
```

{{< plotly json="/zoom2016.json" height="600px" >}}

Une variabilité hebdomadaire se superpose à la tendance saisonnière.

Grâce à la méthode des dataframe pandas `groupby`, on peut facilement grouper les donner de manière à obtenir les statistiques qui nous intéressent.\
Exemple : trouvons combien d'électricité d'origine éolienne a été produite chaque mois en 2016.


```python
serie_temp[serie_temp['année']==2016].groupby("mois")["Vent"].sum()
```

`mois`\
`1     9264.588`\
`2     9814.294`\
`3     6030.177`\
`4     5910.504`\
`5     6089.484`\
`6     3369.069`\
`7     4651.582`\
`8     4742.343`\
`9     4222.315`\
`10    5585.248`\
`11    8076.232`\
`12    9252.290`\
`Name: Vent, dtype: float64`

> Sur le modèle précédent, déterminez le jour de la semaine où l'Allemagne a consommé le plus d'électricité en moyenne en 2016 (vous pourrez utilisez la méthode `mean` à la place de `sum`).

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
Il suffit d'écrire la ligne suivante&nbsp;:<br>
<code>serie_temp[serie_temp['année']==2016].groupby("jour")["Consommation"].mean()</code><br>
Et on constate alors que le mercredi est le jour où les allemands ont le plus consommé en moyenne en 2016.
</blockquote>
</details>

<details>
<summary id="commsum">
Commentaire (cliquer pour afficher)&nbsp;</summary>
<blockquote id="comm">
On retrouve une philosophie proche des fonctions d'agrégations en SQL.
</blockquote>
</details>


Traçons une boîte à moustaches de la répartition des 3 variables mois par mois :

```python
fig, axes = plt.subplots(3, 1, figsize=(15, 10), sharex=True)
for var, ax in zip(['Consommation', 'Solaire', 'Vent'], axes):
    sns.boxplot(data=serie_temp, x='mois', y=var, ax=ax)  
    ax.set_ylabel('GWh')
    ax.set_title(var)  
    if ax != axes[-1]:
        ax.set_xlabel('')
```
![png](/moustachallemagne.png)

On observe que :
- les trois graphes présentent bien une variabilité saisonnière ; la consommation électrique est plus forte en hiver ainsi que la production éolienne (même si l'écart est moins marqué) et la production solaire est beaucoup plus importante en été.
- beaucoup de valeurs se retrouvent à l'extérieur des moustaches supérieures pour la production éolienne, ce qui est probablement dû à des périodes de fort vent.

Regardons maintenant jour par jour :
```python
serie_temp["date"]=(serie_temp.index.strftime('%d %B'))
px.box(serie_temp,x='jour', y='Consommation',hover_data={"date"})
```
{{< plotly json="/jourparjour.json" height="600px" >}}

> Pourquoi y a-t-il autant de points au-delà des moustaches les jours de semaine ?

<details>
<summary id="correcsum">
Correction (cliquer pour afficher)</summary>
<blockquote id="correc">
À cause des jours fériés.
</blockquote>
</details>