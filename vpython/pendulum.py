GlowScript 3.0 VPython
# Pendulum

g=9.8 
bob=sphere(pos=vector(5,2,0),radius=1,color=color.yellow)
pivot=vector(0,20,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.blue)
string=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)
t=0 
dt=0.01 
l=mag(bob.pos-pivot) 
cs=(pivot.y-bob.pos.y)/l
theta=acos(cs) 
vel=0.0 
while (t<100):
  rate(100) 
  acc=-g/l*sin(theta) 
  theta=theta+vel*dt 
  vel=vel+acc*dt 
  bob.pos=vector(l*sin(theta),pivot.y-l*cos(theta),0) 
  string.axis=bob.pos-string.pos 
  t=t+dt 
