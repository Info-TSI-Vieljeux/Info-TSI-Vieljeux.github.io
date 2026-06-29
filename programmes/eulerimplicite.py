# paramètres physiques
l0 = 0.5
m = 1
k = 16
alpha = 0.1
r = 0.05

scene.width,scene.height = 600,150
scene.range = 0.2
scene.background = vec(4,63,97)/255
scene.align = 'left'
scene.center = vec(l0,0,0)

# Valeurs initiales
z1 = 3*l0/2
z2 = 0
t = 0

M = sphere(pos=vec(z1,0,0),radius=r,color=vec(1,0,0),emissive=True)
ressort = helix(pos=vector(0,0,0),axis=M.pos, color=vec(0.7,0.7,0.8),radius=0.05,emissive=True)

# graphes
g1 = graph(width=580,height=200,xtitle='z1',ytitle='z2',align='left',fast=True)
phase = gcurve(graph=g1,color=color.red,dot=True,width=0.5)
g3 = graph(width=580,height=200,xtitle='t',ytitle='z1',align='left',fast=True)
film = gcurve(graph=g3,color=color.blue,dot=True,width=0.5)
filmsol = gcurve(graph=g3,color=vec(0,0.7,0),dot=True,width=0.5)

run = False
def process(ev):
  global run
  run = not run
scene.bind('mousedown', process)

# pas
h = 0.01

while True :
  rate(2/h)
  ### EULER IMPLICITE ###
  z1_old = z1
  z2_old = z2
  z2 = (z2_old-h*k/m*(z1_old-l0))/(1+h*alpha/m+h**2*k/m)
  z1 = z1_old + h*z2
  ########################
  M.pos = vec(z1,0,0)
  ressort.axis = M.pos
  phase.plot(z1,z2)
  film.plot(t,z1)
  filmsol.plot(t,l0+l0/2*exp(-alpha/2/m*t)*cos(sqrt(k/m-(alpha/2/m)**2)*t))
  t += h
  if not run : continue
  scene.pause()
