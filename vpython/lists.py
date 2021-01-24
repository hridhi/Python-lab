GlowScript 3.0 VPython
s1=sphere(pos=vec(-2,-2,-2),color=color.green)
s2=sphere(pos=vec(-2,-2,2),color=color.green)
s3=sphere(pos=vec(-2,2,2),color=color.green)
s4=sphere(pos=vec(-2,2,-2),color=color.green)
s5=sphere(pos=vec(2,-2,-2),color=color.green)
s6=sphere(pos=vec(2,-2,2),color=color.green)
s7=sphere(pos=vec(2,2,2),color=color.green)
s8=sphere(pos=vec(2,2,-2),color=color.green)
particular=[s1,s2,s3,s4,s5,s6,s7,s8]
i=0
while i<len(particular):
    rate(10000)
    particular[i].color=color.cyan
    i=i+1
