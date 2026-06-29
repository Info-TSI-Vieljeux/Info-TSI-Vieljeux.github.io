GlowScript 3.1 VPython
from random import randint

scene.width, scene.height = 600,400
scene.background = vec(241,242,244)/255

N = 5
taux = 150


#scene.pause()

barres = []

scene.center = vec(N/2-1,N/4.2,0)
etapes = 0


############################ COULEURS ##################################

# 100 couleurs issues de la color map viridis
# code pour les afficher pour copier/coller :
#import matplotlib.pyplot as plt
#from matplotlib import cm
#cmap = cm.get_cmap('viridis')
#N = 100
#for i in range(N) :
#    rgba = cmap(i/N)
#    print(f'color[{i}]=vec{rgba[:-1]}')


color = [vec(0,118,186)/255,vec(29,177,0)/255,vec(1,1,1),vec(0,0,0),vec(238,34,12)/255]
################################################################################


barres += box(pos=vec(-0.5,0,0.1),size=vector(1,+1,0.2),color=color[0],emissive=True)
barres += box(pos=vec(1-0.5,1/4,0.1),size=vector(1,1/2+1,0.2),color=color[1],emissive=True)
barres += box(pos=vec(2-0.5,2/4,0.1),size=vector(1,2/2+1,0.2),color=color[2],emissive=True)
barres += box(pos=vec(3-0.5,2/4,0.1),size=vector(1,2/2+1,0.2),color=color[3],emissive=True)
barres += box(pos=vec(4-0.5,3/4,0.1),size=vector(1,3/2+1,0.2),color=color[4],emissive=True)

  
def permuter(L,i,j,taux) :
  pos1 = L[i].pos.x
  pos2 = L[j].pos.x
  dx = (pos2-pos1)/100
  dz = 0.0001
  while L[i].pos.z>-0.2 :
    rate(taux*100)
    L[i].pos.z -= dz*2
    L[j].pos.z += dz
  while abs(L[i].pos.x-pos2) > 1e-3 :
    rate(taux)
    L[i].pos.x += dx
    L[j].pos.x -= dx
  while L[i].pos.z<0.1 :
    rate(taux*100)
    L[i].pos.z += dz*2
    L[j].pos.z -= dz
  L[i] , L[j] = L[j] , L[i]
  return L

def melange(L) :
  global etapes
  for rep in range(N*2) :
    i = randint(0,N-1)
    j = randint(0,N-1)
    L = permuter(L,i,j,taux*2)

melange(barres)

########################## TRI À BULLES #########################
def tri_bulle(L) :
  global etapes
  n = len(L)
  for i in range(n-1):
    for j in range(n-i-1):
      if L[j].height > L[j+1].height :
        L = permuter(L,j,j+1,taux)
##################################################################

########################## TRI FUSION ############################
def fusion(A, B, taux) :
  global etapes
  if A == [] :
    return B
  if B == [] :
    return A
  liste_fusion = A+B
  if A[0].height <= B[0].height :
    return [A[0]] + fusion(A[1:], B, taux)
  else :
    pos1 = A[0].pos.x
    pos2 = B[0].pos.x
    dx = 1/100
    dz = 0.0001
    while A[0].pos.z > -0.2 :
      rate(taux*100)
      B[0].pos.z += dz
      for i in range(len(A)) :
        A[i].pos.z -= dz*2
    while abs(B[0].pos.x-pos1) > 1e-3 :
      rate(taux)
      B[0].pos.x += dx*(pos1-pos2)
      for i in range(len(A)) :
        A[i].pos.x += dx
    while A[0].pos.z < 0.1 :
      rate(taux*100)
      B[0].pos.z -= dz
      for i in range(len(A)) :
        A[i].pos.z += dz*2
    return [B[0]] + fusion(A, B[1:], taux)

def tri_fusion(L) :
  global etapes
  n = len(L)
  if len(L) <= 1 :
    return L
  else :
    return fusion(tri_fusion(L[:n//2]), tri_fusion(L[n//2:]),taux)
#######################################################################

############################ TRI INSERTION ############################
def tri_insertion(L) :
  global etapes
  K = L[:]
  for i in range(1,len(L)) :
    x = K[i]
    j = i
    while j > 0 and K[j-1].height > x.height :
      K[j] = K[j-1]
      j -= 1 
      #J = j # J est l'indice à échanger avec i
    # pour l'affichage
    for k in range(i,j,-1) :
      permuter(L,k-1,k,taux)
    # fin affichage
    K[j] = x
  return K
#####################################################################

############################ QUICKSORT ##############################
def partitionner(L, p, d, pivot) :
  global etapes
  #L[pivot], L[d] = L[d], L[pivot]
  permuter(L,pivot,d,taux)
  j = p
  for i in range(p,d) :
    if L[i].height <= L[d].height :
      #L[i], L[j] = L[j], L[i]
      permuter(L,i,j,taux)
      j += 1
  permuter(L,d,j,taux)
  #L[d], L[j] = L[j], L[d]
  return j

def tri_rapide(L, p, d) :
  global etapes
  if p < d : 
    pivot = randint(p,d)
    pivot = partitionner(L, p, d, pivot)
    tri_rapide(L, p, pivot-1)
    tri_rapide(L, pivot+1, d)
######################################################################

############################ TRI SELECTION ###########################
def  tri_selection(L) :
  global etapes
  n = len(L)
  for i in range(0,n-1) :
    min = i
    for j in range(i+1,n) :
      if L[j].height < L[min].height :
        min = j
    if min != i : 
      #L[i], L[min] = L[min], L[i]
      permuter(L,i,min,taux)
###################################################################

def M1(m):
    global barres, etapes
    if m.index == 1 :
      B.disabled = True
      tri_bulle(barres)
      B.disabled = False
    elif m.index == 2 :
      B.disabled = True
      tri_insertion(barres)
      B.disabled = False
    elif m.index == 3 :
      B.disabled = True
      tri_selection(barres)
      B.disabled = False
    elif m.index == 4 :
      B.disabled = True
      barres = tri_fusion(barres)
      B.disabled = False
    elif m.index == 5 :
      B.disabled = True
      tri_rapide(barres,0,len(barres)-1)
      B.disabled = False
    #for barre in barres :
      #print(barre.height)

scene.append_to_caption('   ')
MEN = menu(choices=["choix algo de tri :",'tri à bulles', 'tri insertion', 'tri sélection', 'tri fusion', 'tri rapide'], bind=M1)

scene.append_to_caption('      ')

def B(b):
    global barres
    melange(barres)
B = button(bind=B, text='Mélanger à nouveau')