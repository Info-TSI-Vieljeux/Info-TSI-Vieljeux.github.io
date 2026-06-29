GlowScript 3.1 VPython

scene.background = vec(1,1,1)
scene.center = vec(10,9,0)
scene.width,scene.height = 650,400
scene.range = 13
Liste_villes = []
B = sphere(pos=vec(11,11,0),color=vec(165,232,217)/255,emissive=True,name='B',voisins=['C','G','M'])
Liste_villes.append(B)
C = sphere(pos=vec(9,11,0),color=vec(93,223,255)/255,emissive=True,name='C',voisins=['B','D','K'])
Liste_villes.append(C)
D = sphere(pos=vec(8,8,0),color=vec(255,153,128)/255,emissive=True,name='D',voisins=['F','H','C'])
Liste_villes.append(D)
F = sphere(pos=vec(10,6,0),color=vec(255,243,106)/255,emissive=True,name='F',voisins=['D','G','R'])
Liste_villes.append(F)
G = sphere(pos=vec(12,8,0),color=vec(207,178,255)/255,emissive=True,name='G',voisins=['F','B','P'])
Liste_villes.append(G)
H = sphere(pos=vec(4,6,0),color=vec(0,196,181)/255,emissive=True,name='H',voisins=['S','D','J'])
Liste_villes.append(H)
J = sphere(pos=vec(4,10,0),color=vec(160,71,255)/255,emissive=True,name='J',voisins=['H','K','X'])
Liste_villes.append(J)
K = sphere(pos=vec(6,13,0),color=vec(255,208,231)/255,emissive=True,name='K',voisins=['C','J','L'])
Liste_villes.append(K)
L = sphere(pos=vec(10,15,0),color=vec(1,191,244)/255,emissive=True,name='L',voisins=['W','K','M'])
Liste_villes.append(L)
M = sphere(pos=vec(15,13,0),color=vec(67,233,203)/255,emissive=True,name='M',voisins=['B','L','N'])
Liste_villes.append(M)
N = sphere(pos=vec(16,10,0),color=vec(188,128,255)/255,emissive=True,name='N',voisins=['Z','P','M'])
Liste_villes.append(N)
P = sphere(pos=vec(16,6,0),color=vec(255,198,24)/255,emissive=True,name='P',voisins=['Q','G','N'])
Liste_villes.append(P)
Q = sphere(pos=vec(14,3,0),color=vec(255,64,0)/255,emissive=True,name='Q',voisins=['V','P','R'])
Liste_villes.append(Q)
R = sphere(pos=vec(10,2,0),color=vec(255,133,187)/255,emissive=True,name='R',voisins=['Q','F','S'])
Liste_villes.append(R)
S = sphere(pos=vec(6,3,0),color=vec(0,164,214)/255,emissive=True,name='S',voisins=['T','H','R'])
Liste_villes.append(S)
T = sphere(pos=vec(4,0,0),color=vec(0,139,186)/255,emissive=True,name='T',voisins=['X','V','S'])
Liste_villes.append(T)
V = sphere(pos=vec(16,0,0),color=vec(215,85,149)/255,emissive=True,name='V',voisins=['T','Z','Q'])
Liste_villes.append(V)
W = sphere(pos=vec(10,20,0),color=vec(255,174,0)/255,radius=0.4,emissive=True,name='W',voisins=['X','L','Z'])
Liste_villes.append(W)
X = sphere(pos=vec(0,12,0),color=vec(0,150,136)/255,radius=0.4,emissive=True,name='X',voisins=['T','J','W'])
Liste_villes.append(X)
Z = sphere(pos=vec(20,12,0),color=vec(228,58,2)/255,radius=0.4,emissive=True,name='Z',voisins=['N','V','W'])
Liste_villes.append(Z)

rayon = 0.6
for ville in Liste_villes :
  ville.radius = rayon


def arete(A,B) :
  return cylinder(pos=A.pos,axis=B.pos-A.pos, radius=0.05, color=vec(146,146,146)/255, emissive=True)

arete(W,Z)
arete(Z,V)
arete(V,T)
arete(T,X)
arete(X,W)
arete(W,L)
arete(Z,N)
arete(V,Q)
arete(T,S)
arete(X,J)
arete(L,M)
arete(M,N)
arete(N,P)
arete(P,Q)
arete(Q,R)
arete(R,S)
arete(S,H)
arete(H,J)
arete(J,K)
arete(K,L)
arete(M,B)
arete(P,G)
arete(R,F)
arete(H,D)
arete(K,C)
arete(C,B)
arete(B,G)
arete(G,F)
arete(F,D)
arete(D,C)

for ville in Liste_villes :
  label(pos=ville.pos,xoffset=7,yoffset=0,opacity=0,box=False,text=ville.name,line=False)


#nom_ville = input("Vous voulez partir de quelle ville ?")
L1 = label( pos=vec(-5,2,-2), text='Choisir une ville\n de départ',height=20,background=vec(0.4,0.4,0.4),color=vec(1,1,1))
L2 = label( pos=vec(-5,4,-2), text="Quelle est la\n prochaine\n destination ?",height=20,visible=False,background=vec(0.4,0.4,0.4),color=vec(1,1,1))
L3 = label( pos=vec(10,9,-2), text="GAGNÉ !",height=180,visible=False,background=vec(0,0.6,0),color=vec(1,1,1),border=200)
L4 = label( pos=vec(10,9,-2), text="PERDU !",height=180,visible=False,background=vec(1,0,0),color=vec(1,1,1),border=200)

scene.waitfor("draw_complete")

def getevent(L):
    global ville
    ville = scene.mouse.pick


while True :
  scene.pause()
  scene.bind("mousedown", getevent())
  if ville in Liste_villes :
    L1.visible = False
    Dep = ville
    break


MX = ring(pos=Dep.pos, axis=vector(0,0,1), radius=rayon+0.1,thickness=0.2,emissive=True,color=vec(0.5,0.1,0.3),make_trail=True,trail_radius=0.2)
Liste_interdite = [Dep.name]
Prem_dep = Dep.name
scene.waitfor("draw_complete")

while True :
  Voisins = Dep.voisins
  L2.visible = True
  ville = '?'
  while True :
    scene.pause()
    scene.bind("mousedown", getevent())
    if ville in Liste_villes :
      if ville.name in Liste_interdite :
        input("Déjà passé par là !")
        continue
      elif ville.name not in Voisins :
        input("Trop loin !")
      else : break
        
  Arr = ville
  while mag(MX.pos-Arr.pos)>1e-5 :
      rate(1000)
      MX.pos += (Arr.pos-Dep.pos)/200
  Liste_interdite.append(ville.name)
  Dep = Arr
  fin = False
  for ville in Dep.voisins :
    if ville not in Liste_interdite :
      fin = False
      break
    fin = True
  if fin : 
    if len(Liste_interdite)==20 and Prem_dep in Dep.voisins :
      L2.visible = False
      L3.visible = True
      fin = True
      break
    else :
      L2.visible = False
      L4.visible = True
      fin = True
      break
  if fin : break