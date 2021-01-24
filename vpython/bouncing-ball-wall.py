GlowScript 3.0 VPython

ball1 = sphere(pos=vector(-2,0,0), radius=0.5, color=color.red)
ball2 = sphere(pos=vector(2,0,0), radius=0.5, color=color.cyan)
wallL = box(pos=vector(-20,0,0), size=vector(0.2,12,12), color=color.green)
wallR = box(pos=vector(20,0,0), size=vector(0.2,12,12), color=color.green)
ball1.velocity = vector(-25,0,0)
ball2.velocity = vector(25,0,0)
deltat = 0.005
t = 0
while t < 10:
    rate(100)
    if ball1.pos.x < wallL.pos.x:
        ball1.velocity.x = -ball1.velocity.x 
    if ball2.pos.x > wallR.pos.x:
        ball2.velocity.x = -ball2.velocity.x
    if ball1.pos.x == ball2.pos.x:
        ball1.velocity.x = -ball1.velocity.x 
        ball2.velocity.x = -ball2.velocity.x
    ball1.pos = ball1.pos + ball1.velocity*deltat
    ball2.pos = ball2.pos + ball2.velocity*deltat
    t = t + deltat
