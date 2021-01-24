GlowScript 3.0 VPython
#moving train till it reaches it station which is indicated with arrow 
N=int(input("give number of compartments for the train "))
compartments=[]
rings1=[]
rings2=[]
l=0.3
h=0.2
w=0.01
for x in range(N):
    b=box(color=color.green, size=vector(l,h,w), axis=vector(0,0,0),pos=vec(-x+0.1,0,0) )
    #t1=ring(color=color.cyan , pos=vec(-x+0.1,-0.1,0), axis=vector(0,0,0),radius =0.1)
    #t2=ring(color=color.cyan , pos=vec(-x+0.1+l,-0.1,0), axis=vector(0,0,0),radius=0.1)
    compartments.append(b)
    #rings1.append(t1)
    #rings2.append(t2)
    
m=100/N
m=m*0.1
a=arrow(pos=vec(0.4+m,0,0), color=color.red, axis=vec(0,0.5,0))
for i in range(100/N):
    for b in compartments :
        rate(100)
        b.pos.x+=0.1
        #t1.pos.x+=0.1
        #t2.pos.x+=0.1
    
    


