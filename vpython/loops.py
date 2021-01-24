GlowScript 3.0 VPython
a=sphere(pos=vec(0,0,0),color=color.cyan,radius=1.5)
b=sphere(pos=vec(-5,5,5),color=color.cyan,radius=0.5)
c=arrow(pos=a.pos,axis=b.pos-a.pos,color=color.orange)
r=vec(-5,5,5)
while r.x<10:
    rate(10)
    #sphere(pos=r,color=color.green,radius=0.5)
    b.pos=r
    c.axis=b.pos-a.pos
    r.x=r.x+1
