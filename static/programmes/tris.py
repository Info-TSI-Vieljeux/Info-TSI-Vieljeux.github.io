GlowScript 3.1 VPython
from random import randint

scene.width, scene.height = 800,600
scene.background = vec(2,61,96)/255

N = 20
taux = 300

def M0(m):
    global N, taux
    if m.index == 1 :
      N = 20
      taux = 300
    elif m.index == 2 :
      N = 100
      taux = 5000
men = menu(choices=["Nombre éléments", '20', '100'], bind=M0)

scene.pause()
men.delete()

barres = []

scene.center = vec(N/2-1,N/4.2,0)
etapes = 0
T = label(pos=vec(N/2,-5/(100/N)-0.5,0), text=f'{etapes} étapes')


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

color = [0]*100
color[0]=vec(0.267004, 0.004874, 0.329415)
color[1]=vec(0.269944, 0.014625, 0.341379)
color[2]=vec(0.273809, 0.031497, 0.358853)
color[3]=vec(0.276022, 0.044167, 0.370164)
color[4]=vec(0.278791, 0.062145, 0.386592)
color[5]=vec(0.280267, 0.073417, 0.397163)
color[6]=vec(0.281924, 0.089666, 0.412415)
color[7]=vec(0.282656, 0.100196, 0.42216)
color[8]=vec(0.283197, 0.11568, 0.436115)
color[9]=vec(0.283072, 0.130895, 0.449241)
color[10]=vec(0.282623, 0.140926, 0.457517)
color[11]=vec(0.281412, 0.155834, 0.469201)
color[12]=vec(0.280255, 0.165693, 0.476498)
color[13]=vec(0.278012, 0.180367, 0.486697)
color[14]=vec(0.276194, 0.190074, 0.493001)
color[15]=vec(0.273006, 0.20452, 0.501721)
color[16]=vec(0.270595, 0.214069, 0.507052)
color[17]=vec(0.26658, 0.228262, 0.514349)
color[18]=vec(0.262138, 0.242286, 0.520837)
color[19]=vec(0.258965, 0.251537, 0.524736)
color[20]=vec(0.253935, 0.265254, 0.529983)
color[21]=vec(0.250425, 0.27429, 0.533103)
color[22]=vec(0.244972, 0.287675, 0.53726)
color[23]=vec(0.241237, 0.296485, 0.539709)
color[24]=vec(0.235526, 0.309527, 0.542944)
color[25]=vec(0.229739, 0.322361, 0.545706)
color[26]=vec(0.225863, 0.330805, 0.547314)
color[27]=vec(0.220057, 0.343307, 0.549413)
color[28]=vec(0.21621, 0.351535, 0.550627)
color[29]=vec(0.210503, 0.363727, 0.552206)
color[30]=vec(0.206756, 0.371758, 0.553117)
color[31]=vec(0.201239, 0.38367, 0.554294)
color[32]=vec(0.197636, 0.391528, 0.554969)
color[33]=vec(0.192357, 0.403199, 0.555836)
color[34]=vec(0.187231, 0.414746, 0.556547)
color[35]=vec(0.183898, 0.422383, 0.556944)
color[36]=vec(0.179019, 0.433756, 0.55743)
color[37]=vec(0.175841, 0.44129, 0.557685)
color[38]=vec(0.171176, 0.45253, 0.557965)
color[39]=vec(0.168126, 0.459988, 0.558082)
color[40]=vec(0.163625, 0.471133, 0.558148)
color[41]=vec(0.160665, 0.47854, 0.558115)
color[42]=vec(0.15627, 0.489624, 0.557936)
color[43]=vec(0.151918, 0.500685, 0.557587)
color[44]=vec(0.149039, 0.508051, 0.55725)
color[45]=vec(0.144759, 0.519093, 0.556572)
color[46]=vec(0.141935, 0.526453, 0.555991)
color[47]=vec(0.13777, 0.537492, 0.554906)
color[48]=vec(0.135066, 0.544853, 0.554029)
color[49]=vec(0.131172, 0.555899, 0.552459)
color[50]=vec(0.127568, 0.566949, 0.550556)
color[51]=vec(0.125394, 0.574318, 0.549086)
color[52]=vec(0.122606, 0.585371, 0.546557)
color[53]=vec(0.121148, 0.592739, 0.544641)
color[54]=vec(0.119738, 0.603785, 0.5414)
color[55]=vec(0.119423, 0.611141, 0.538982)
color[56]=vec(0.120081, 0.622161, 0.534946)
color[57]=vec(0.12138, 0.629492, 0.531973)
color[58]=vec(0.12478, 0.640461, 0.527068)
color[59]=vec(0.130067, 0.651384, 0.521608)
color[60]=vec(0.134692, 0.658636, 0.517649)
color[61]=vec(0.143303, 0.669459, 0.511215)
color[62]=vec(0.150148, 0.676631, 0.506589)
color[63]=vec(0.162016, 0.687316, 0.499129)
color[64]=vec(0.170948, 0.694384, 0.493803)
color[65]=vec(0.185783, 0.704891, 0.485273)
color[66]=vec(0.196571, 0.711827, 0.479221)
color[67]=vec(0.214, 0.722114, 0.469588)
color[68]=vec(0.232815, 0.732247, 0.459277)
color[69]=vec(0.24607, 0.73891, 0.452024)
color[70]=vec(0.266941, 0.748751, 0.440573)
color[71]=vec(0.281477, 0.755203, 0.432552)
color[72]=vec(0.304148, 0.764704, 0.419943)
color[73]=vec(0.319809, 0.770914, 0.411152)
color[74]=vec(0.344074, 0.780029, 0.397381)
color[75]=vec(0.369214, 0.788888, 0.382914)
color[76]=vec(0.386433, 0.794644, 0.372886)
color[77]=vec(0.412913, 0.803041, 0.357269)
color[78]=vec(0.430983, 0.808473, 0.346476)
color[79]=vec(0.458674, 0.816363, 0.329727)
color[80]=vec(0.477504, 0.821444, 0.318195)
color[81]=vec(0.506271, 0.828786, 0.300362)
color[82]=vec(0.525776, 0.833491, 0.288127)
color[83]=vec(0.555484, 0.840254, 0.269281)
color[84]=vec(0.585678, 0.846661, 0.249897)
color[85]=vec(0.606045, 0.850733, 0.236712)
color[86]=vec(0.636902, 0.856542, 0.21662)
color[87]=vec(0.657642, 0.860219, 0.203082)
color[88]=vec(0.688944, 0.865448, 0.182725)
color[89]=vec(0.709898, 0.868751, 0.169257)
color[90]=vec(0.741388, 0.873449, 0.149561)
color[91]=vec(0.762373, 0.876424, 0.137064)
color[92]=vec(0.79376, 0.880678, 0.120005)
color[93]=vec(0.82494, 0.88472, 0.106217)
color[94]=vec(0.845561, 0.887322, 0.099702)
color[95]=vec(0.876168, 0.891125, 0.09525)
color[96]=vec(0.89632, 0.893616, 0.096335)
color[97]=vec(0.926106, 0.89733, 0.104071)
color[98]=vec(0.945636, 0.899815, 0.112838)
color[99]=vec(0.974417, 0.90359, 0.130215)

if N == 20 :
  color2 = [] 
  for i in range(100) :
    if i%5 == 0 :
      color2 += color[i]
  color = color2
################################################################################

for i in range(N) :
  barres += box(pos=vec(i-0.5,i/4,0.1),size=vector(1,i/2+1,0.2),color=color[i],emissive=False)
  
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
    L = permuter(L,i,j,taux*N)
  etapes = 0
  T.text = f'{etapes} étapes'
    
melange(barres)

########################## TRI À BULLES #########################
def tri_bulle(L) :
  global etapes
  n = len(L)
  for i in range(n-1):
    for j in range(n-i-1):
      etapes += 1
      T.text = f'{etapes} étapes'
      if L[j].height > L[j+1].height :
        L = permuter(L,j,j+1,taux)
        etapes += 1
        T.text = f'{etapes} étapes'
##################################################################

########################## TRI FUSION ############################
def fusion(A, B, taux) :
  global etapes
  if A == [] :
    etapes += 1
    T.text = f'{etapes} étapes'
    return B
  if B == [] :
    etapes += 1
    T.text = f'{etapes} étapes'
    return A
  liste_fusion = A+B
  etapes += 1
  T.text = f'{etapes} étapes'
  if A[0].height <= B[0].height :
    etapes += 1
    T.text = f'{etapes} étapes'
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
    etapes += 1
    T.text = f'{etapes} étapes'
    return [B[0]] + fusion(A, B[1:], taux)

def tri_fusion(L) :
  global etapes
  n = len(L)
  if len(L) <= 1 :
    return L
  else :
    etapes += 1
    T.text = f'{etapes} étapes'
    return fusion(tri_fusion(L[:n//2]), tri_fusion(L[n//2:]),taux)
#######################################################################

############################ TRI INSERTION ############################
def tri_insertion(L) :
  global etapes
  K = L[:]
  for i in range(1,len(L)) :
    x = K[i]
    j = i
    etapes += 1
    T.text = f'{etapes} étapes'
    while j > 0 and K[j-1].height > x.height :
      K[j] = K[j-1]
      j -= 1 
      #J = j # J est l'indice à échanger avec i
    # pour l'affichage
    for k in range(i,j,-1) :
      permuter(L,k-1,k,taux)
      etapes += 1
      T.text = f'{etapes} étapes'
    # fin affichage
    K[j] = x
  return K
#####################################################################

############################ QUICKSORT ##############################
def partitionner(L, p, d, pivot) :
  global etapes
  #L[pivot], L[d] = L[d], L[pivot]
  permuter(L,pivot,d,taux)
  T.text = f'{etapes} étapes'
  etapes += 1
  j = p
  for i in range(p,d) :
    etapes += 1
    T.text = f'{etapes} étapes'
    if L[i].height <= L[d].height :
      #L[i], L[j] = L[j], L[i]
      permuter(L,i,j,taux)
      j += 1
      etapes += 1
      T.text = f'{etapes} étapes'
  permuter(L,d,j,taux)
  etapes += 1
  T.text = f'{etapes} étapes'
  #L[d], L[j] = L[j], L[d]
  return j

def tri_rapide(L, p, d) :
  global etapes
  etapes += 1
  T.text = f'{etapes} étapes'
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
      etapes += 1
      T.text = f'{etapes} étapes'
      if L[j].height < L[min].height :
        min = j
        etapes += 1
    if min != i : 
      #L[i], L[min] = L[min], L[i]
      permuter(L,i,min,taux)
      etapes += 1
      T.text = f'{etapes} étapes'
###################################################################

def M1(m):
    global barres, etapes
    if m.index == 1 :
      etapes = 0
      T.text = f'{etapes} étapes'
      B.disabled = True
      tri_bulle(barres)
      B.disabled = False
    elif m.index == 2 :
      etapes = 0
      T.text = f'{etapes} étapes'
      B.disabled = True
      tri_insertion(barres)
      B.disabled = False
    elif m.index == 3 :
      etapes = 0
      T.text = f'{etapes} étapes'
      B.disabled = True
      tri_selection(barres)
      B.disabled = False
    elif m.index == 4 :
      etapes = 0
      T.text = f'{etapes} étapes'
      B.disabled = True
      barres = tri_fusion(barres)
      B.disabled = False
    elif m.index == 5 :
      etapes = 0
      T.text = f'{etapes} étapes'
      B.disabled = True
      tri_rapide(barres,0,len(barres)-1)
      B.disabled = False
    #for barre in barres :
      #print(barre.height)

#scene.append_to_caption('   ')
MEN = menu(choices=["choix algo de tri :",'tri à bulles', 'tri insertion', 'tri sélection', 'tri fusion', 'tri rapide'], bind=M1)

#scene.append_to_caption('      ')

def B(b):
    global barres
    melange(barres)
B = button(bind=B, text='Mélanger à nouveau')
