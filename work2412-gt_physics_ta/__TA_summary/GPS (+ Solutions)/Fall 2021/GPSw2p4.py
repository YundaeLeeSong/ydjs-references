GlowScript 3.0 VPython
## PHYS 2211 Online
## GPS Week 2, Problem 4b
## Last updated: 2021-01-11 EAM


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# Visualization 
ball = sphere(color=color.blue, radius=0.22)
trail = curve(color=color.green, radius=0.02)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.04)

# Graphing 
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

ball.m = 1
ball.pos = vector(2,0,0)
ball.vel = vector(1,0,0)

t = 0           # where the clock starts
deltat = 0.01   # size of each timestep


## ======================================
## CALCULATION LOOP
## (motion prediction and visualization)
## ======================================

while t < 2.0:
    rate(100)
    Fnet=vector(0,0,0)
    ball.vel = ball.vel + (Fnet/ball.m)*deltat
    ball.pos = ball.pos + ball.vel*deltat

    t = t + deltat
    trail.append(pos=ball.pos)

    poscurve.plot(t,ball.pos.x)
    velcurve.plot(t,ball.vel.x)

ball.vel=vector(-2,0,0)

while t < 4.0:
    rate(100)
    Fnet=vector(0,0,0)
    ball.vel = ball.vel + (Fnet/ball.m)*deltat
    ball.pos = ball.pos + ball.vel*deltat

    t = t + deltat
    trail.append(pos=ball.pos)

    poscurve.plot(t,ball.pos.x)
    velcurve.plot(t,ball.vel.x)

print("All done!")