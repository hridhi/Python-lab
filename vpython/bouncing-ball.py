GlowScript 3.0 VPython
ball = sphere(pos=vec(0,0,0), radius=1, color=color.red)
floor = box(pos=vec(0,-10,0), size = vec(10,1,10), color=color.green)
ball.velocity=vec(0,0,0)
dt=0.01
t=0
g=-9.8
while (t < 20):
  rate(100)
  ball.velocity.y=ball.velocity.y+g*dt
  ball.pos=ball.pos+ball.velocity*dt
  if (ball.pos.y < floor.pos.y + 1.25) :
    ball.velocity.y = -ball.velocity.y
  t=t+dt
