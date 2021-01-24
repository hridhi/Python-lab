GlowScript 3.0 VPython
scene.width=600
scene.height=600
k=.1
a=1
l0=1.9
m=0.001
g=9.8
scalefactor=50

floor=box(length=5,width=1,height=0.5,color=color.green)
wall = box(pos=vector(-floor.length/2 ,0.5+floor.height/2 , 0) , length=0.1, width=1, height=1.5)
mass = box(pos=vector(0,a/2+floor.height/2 ,0), length=a, width=a)
spring= helix(pos=wall.pos + vector(wall.length/2,0,0))

l=spring.axis
s=mag(l)-l0
l_hat=l/mag(l)
fspring=-k*s*l_hat
fgrav=m*g*vec(0,-1,0)

fspring_arr=arrow(pos=mass.pos,axis=scalefactor*fspring,color=color.red)
