---
title: "IEEE-754"
date: 2021-03-06T14:23:56+01:00
weight : 4
draft: false
---

# IEEE-754

- Réaliser un convertisseur permettant de donner l'écriture d'un flottant sous la forme d'un mot binaire de 64 bits suivant la norme IEEE-754 (cf. [cours sur le codage des nombres](https://info-tsi-vieljeux.github.io/semestre_2/nombre/#norme-ieee-754)).
- Réaliser aussi le convertisseur inverse, du mot 64 bits au nombre décimal.

---

## Pour vérifier

Nombre à convertir en mot machine 64 bits&nbsp;: <input type="text" id="nombre" value="0">

<button onclick="convNb()">Conversion</button>

<p id="res1"></p>

Mot machine 64 bits à convertir en nombre décimal&nbsp;: <input type="text" id="mot">

<button onclick="convMot()">Conversion</button>

<p id="res2"></p>

<script>
function conv_fract(n) {
	n = Math.abs(n);
  n = n - Math.trunc(n);
  n *= 2;
  let count = 0;
  let s = '';
  let eps = 10**(-9);
  while (count < 64) {
  	if (n>=1) {
      	s += '1';
        if (!((1-eps < n) && (n < 1+eps))) {
      	  n = (n-1)*2;
        }
        else {
      	  break;
        }
  	}
    else {
      s += '0';
    	n *= 2
    }
    count += 1
  }
  console.log("yop",s)
  return s
}

function convNb() {
  var mantisse_str;
  var exp;
  var exp_str;
  const element = document.getElementById("res1");
  var n = document.getElementById("nombre").value;
  n = n.replace(",", ".");
  n = parseFloat(n);
  s = '';
  if (n < 0) {
  	s += '1';
    n = Math.abs(n);
    }	
  else {
    s += '0';
    }
  element.innerHTML = "bit de signe : <span style='color:green;'>" + s + "</span><br>";
  n = Math.abs(n);
  if (n > 1) {
  	let mantPartieEntiere = Math.trunc(n).toString(2);
    mantisse_str = mantPartieEntiere.slice(1,);
    mantisse_str += conv_fract(n).slice(0,52-mantisse_str.length);
    exp = mantPartieEntiere.length-1 + 1023;
    exp_str = exp.toString(2);
    s += exp_str.padStart(11, '0');
    }
  else {
    if (n == 0) {
      exp = 0;
      exp_str = '0'*11;
      s += exp_str;
      mantisse_str = '0'*52;
    }
		else {
      let dvlpt = "0"+conv_fract(n);
      let Exp = 0;
      while (dvlpt[Exp] == "0" ){
        Exp += 1;
      }
      exp = Exp*(-1) + 1023
      exp_str = exp.toString(2);
      s += exp_str.padStart(11, '0');
      mantisse_str = conv_fract(n).slice(Exp,);
    }
    }
  element.innerHTML += "exposant (en puissance de 2) : ";
  element.innerHTML += exp-1023;
  element.innerHTML += " + 1023 = ";
  element.innerHTML += exp;
  element.innerHTML += "  d'où en binaire : <span style='color:purple;'>"+exp_str+"</span>";
  s += mantisse_str;
  s = s.padEnd(64, '0');
  s = s.slice(0,64);
  if (s[0]==1) {n=-n}
  element.innerHTML += "<br>mot machine correspondant à "+String(n)+" : <br>"
  element.innerHTML += "<span style='color:green;'>" + s[0] + " </span>";
  element.innerHTML += "<span style='color:purple;'>" + s.slice(1,12) + " </span>";
  element.innerHTML += "<span style='color:blue;'>" + s.slice(12,) + "</span>";
}

function convMot() {
	var nombre;
  const element = document.getElementById("res2");
  var s = document.getElementById("mot").value;
  s = s.replace(/\s/g, '');
	if (parseInt(s) == 0) {
  	nombre = 0
  }
  else {
    let exp = parseInt(s.slice(1,12),2) - 1023
    nombre =  2**exp
    let mantisse = s.slice(12,)
    for (let i = 0; i < 52; i++) {
      exp += -1
      nombre += parseInt(mantisse[i])*2**exp
    }
    if (s[0]==1){
      nombre *= -1
    }
  }
 element.innerHTML = nombre
}
</script>

<br>

---


## Une solution possible

La fonction suivante convertit la partie fractionnaire du nombre `n` en binaire et donne ainsi son développement binaire (équivalent d'un dévelopement décimal).<br>
Tous les nombres auront nécessairement un développement binaire fini (et seront donc des fractions dyadiques) puisque le flottant donné en argument a lui même une écriture fini (il est codé sur 64 bits !).

```python
def conv_fract(n):
    n = abs(n)
    n = n-int(n)
    count = 0
    s = ''
    n *= 2
    eps = 1e-9
    while count < 64:
        print(n)
        if n >= 1:
            s += '1'
            if not 1-eps < n < 1+eps: 
                n = (n-1)*2
            else: # fin du développement binaire
                break
        else:
            s += '0'
            n *= 2
        count += 1
    return s
```

La méthode consiste à multiplié par 2 lorsque le nombre est inférieur à 1 et à retirer 1 lorsqu'il dépasse.<br>
On constate sur l'enchaînement des résultats intermédiaires que le chiffre avant la virgule correspond au développement binaire du nombre&nbsp;:

{{<rawhtml>}}
<div style="font-family:monospace">
>>> conv_fract(0.1)<br>
0.2<br>
0.4<br>
0.8<br>
1.6<br>
1.2000000000000002<br>
0.40000000000000036<br>
0.8000000000000007<br>
1.6000000000000014<br>
1.2000000000000028<br>
0.4000000000000057<br>
0.8000000000000114<br>
1.6000000000000227<br>
1.2000000000000455<br>
0.40000000000009095<br>
0.8000000000001819<br>
1.6000000000003638<br>
1.2000000000007276<br>
0.4000000000014552<br>
0.8000000000029104<br>
1.6000000000058208<br>
1.2000000000116415<br>
0.40000000002328306<br>
0.8000000000465661<br>
1.6000000000931323<br>
1.2000000001862645<br>
0.40000000037252903<br>
0.8000000007450581<br>
1.6000000014901161<br>
1.2000000029802322<br>
0.4000000059604645<br>
0.800000011920929<br>
1.600000023841858<br>
1.2000000476837158<br>
0.40000009536743164<br>
0.8000001907348633<br>
1.6000003814697266<br>
1.2000007629394531<br>
0.40000152587890625<br>
0.8000030517578125<br>
1.600006103515625<br>
1.20001220703125<br>
0.4000244140625<br>
0.800048828125<br>
1.60009765625<br>
1.2001953125<br>
0.400390625<br>
0.80078125<br>
1.6015625<br>
1.203125<br>
0.40625<br>
0.8125<br>
1.625<br>
1.25<br>
0.5<br>
1.0<br>
</div>
{{</rawhtml>}}
`'00011001100110011001100110011001100110011001100110011010001100110011001100110011001100110011001100110011001101'`


<br>

Un code possible pour obtenir l'écriture du nombre sur 64 bits via la norme IEEE-754.

```python
def conv_iee(n: float) -> str:
    s = ''
    if n < 0:
        s += '1'
    else:
        s += '0'
    n = abs(n)
    if n > 1:
        mantisse_str = bin(int(n))[3:] # on enlève le 1er 1
        mantisse_str += conv_fract(n)[:52-len(mantisse_str)]
        exp = len(bin(int(n))[2:])-1 + 1023
        exp_str = bin(exp)[2:]
        s += (11-len(exp_str))*'0'+ exp_str
    else:
        if n == 0:
            exp = 0
            exp_str = '0'*11
            s += exp_str
            mantisse_str = '0'*52
        else:
            dvlpt = "0"+conv_fract(n)
            exp = 0
            while dvlpt[exp] == "0":
                exp += 1
            exp = exp*(-1) + 1023
            exp_str = bin(exp)[2:]
            s += (11-len(exp_str))*'0' + exp_str # on ajoute des 0 à gauche pour compléter à 11 caractères
            mant = conv_fract(n)
            mantisse_str = ""
            test = True
            for i in range(len(mant)):
                if not test or mant[i] != "0": # on enlève les 0 qui précèdent le 1er 1
                    mantisse_str += mant[i]
                    test = False
            mantisse_str = mantisse_str[1:] # on enlève le 1er 1
    if len(mantisse_str) < 52:
        mantisse_str += (52-len(mantisse_str))*'0'
    s += mantisse_str
    s = s[0]+" "+s[1:12]+" "+s[12:]
    return s
```

Enfin, code d'un convertisseur d'un mot machine 64 bits vers sa valeur décimale&nbsp;:

```python
def deconv(s: str) -> float:
    mot = ''
    for c in s:
        if c != ' ':
            mot += c
    if int(mot) == 0:
        return 0
    exp = int(mot[1:12],2) - 1023
    nombre =  2**exp
    mantisse = mot[12:]
    for c in mantisse:
        exp -= 1
        nombre += int(c)*2**exp
    if mot[0] == "1":
        nombre *= -1
    return nombre
```