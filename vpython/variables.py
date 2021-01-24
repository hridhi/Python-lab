GlowScript 3.0 VPython
a=sphere(pos=vec(0,0,0),color=color.green,radius=1)
b=sphere(pos=vec(0,-6,-5),color=color.green,radius=1)
c=sphere(pos=vec(-6,0,-5),color=color.green,radius=1)
arrow(pos=a.pos,color=color.yellow,axis=b.pos-a.pos)
arrow(pos=b.pos,color=color.yellow,axis=c.pos-b.pos)
arrow(pos=c.pos,color=color.yellow,axis=a.pos-c.pos)
