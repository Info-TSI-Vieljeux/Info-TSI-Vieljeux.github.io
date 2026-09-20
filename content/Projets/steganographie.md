---
title: "Stéganographie"
date: 2021-03-06T14:23:56+01:00
weight : 3
draft: false
---

# Stéganographie



## Première mission

Dévoiler le message caché dans les 2 bits de poids faible de l'image fournie (dont l'adresse est [https://info-tsi-vieljeux.github.io/cryptedimage.png](https://info-tsi-vieljeux.github.io/imageprojet.png)).

![](/cryptedimage.png)

Importons d'abord les modules nécessaires&nbsp;:

```python
from PIL import Image
import urllib.request # pour récupérer une image sur le web
from IPython.display import display # pour afficher dans un notebook
import numpy as np
```


Ce petit code suffit pour dévoiler l'image cachée dans l'image&nbsp;:
```python
def decache_image(image):
    image_decrypt = (image % 2**2) * 2**6 + 2**5
    return image_decrypt
```

- `image % 2**2` récupère les deux bits de poids faibles.<br>
- `* 2**6` permet de "dilater" les 4 valeurs $\\\{0,1,2,3\\\}\rightarrow\\\{0,64,128,192\\\}$
- `+ 2**5` permet de décaller les valeurs pour les centrer entre 0 et 255 $\rightarrow\\\{32,96,160,224\\\}$.


Pour l'afficher (sur un notebook type Colab) :

```python
final = decache_image(cache)
affichage = Image.fromarray(comparaison)
display(affichage)
```
![](/imagedevoile.png)

On peut vérifier que l'image obtenue est bien codée sur 2 bits avec le code suivant :

```python
print(set(final.flatten()))
```
`{32, 224, 96, 160}`<br>

`flatten` est une méthode de `numpy` permettant de transformer un tableau multidimensionnel en un tableau unidimensionnel (ici, le tableau image 3D devient donc un tableau 1D de longueur $l\times L \times 3$).<br>
`set` est une fonction native python permettant de convertir une séquence d'objets en une nouvelle structure, l'ensemble (en python, c'est le type`set`). Son grand avantage est d'éliminer automatiquement tout doublon&nbsp;!

<br>

## Deuxième mission

Il faut donc réussir à convertir l'image secrète en 6 bits (2 bits pour chaque pixel) et l'image servant de cache en 18 bits (6 bits pour chaque pixel) avant d'additionner les deux images, faisant en sorte que l'image à cacher corresponde aux deux bits de poids faible de l'image finale.

![](/missionimage.png)

```python
def cache_image(image1,image2):
    """
    cache_image(image1 : numpy.ndarray (H1,L1,3),image2 : numpy.ndarray (H2,L2,3)) -> numpy.ndarray (H1,L1,3)
    cache image2 dans image1 après l'avoir recadrée si besoin
    """
    H1,L1,_ = image1.shape
    H2,L2,_ = image2.shape
    hidden = np.copy(image2)[:H1,:L1,:3] # sans np.copy, le slicing rend image2 mutable
    hidden = (hidden.astype(np.uint16)//2**6).astype(np.uint8)
    image1 = image1//2**2 * 2**2
    imagemix = image1[:,:,:3] # le :3 sert à retirer une éventuelle transparence, codée comme une 4e couleur
    h , l = max((H1-H2)//2,0), max((L1-L2)//2,0)
    imagemix[h:h+H2,l:l+L2] += hidden
    return imagemix
```

Et pour faciliter l'utilisation d'url pour chaque image&nbsp;:

```python
def cachageimage():
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener) # sans ce bazar, certains sites refusent la visite car le fouineur se présente pas comme un browser
    url1 = input("url de l'image à afficher : ")
    urllib.request.urlretrieve(url1, '1')
    url2 = input("url de l'image à cacher : ")
    urllib.request.urlretrieve(url2, '2')
    image1 = np.array(Image.open('1'))
    image2 = np.array(Image.open('2'))
    return cache_image(image1,image2)
```

On obtient finalement&nbsp;:
![](/imagefinproj.png)

Et en "décachant" (pour vérifier)&nbsp;:
![](/findemasked.png)
