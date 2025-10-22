from vpython import *
#GlowScript 3.0 VPython
## PHYS 2211 Online
## Lab 2: Motion of a Falling Object
## Example of fully working code
## Last updated: 2021-01-11 EAM


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# Uncomment this next line if you prefer a white background
#scene.background = color.white

# Visualization (object, trail, origin)
ball = sphere(color=color.blue, radius=0.22)
trail = curve(color=color.green, radius=0.02)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.04)

# Arrows to represent vector quantities in the visualization window
arrowGrav = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.orange)
arrowDrag = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.cyan)

# Graphing (if needed, you can add more plot and curve lines)
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)



## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# System Mass -- EDIT THIS NEXT LINE
ball.m = 0.12

# Initial Conditions -- EDIT THESE TWO LINES (as necessary)
ball.pos = vector(0,5,0)
ball.vel = vector(0,0,0)

# Time -- EDIT THESE TWO LINES (as necessary)
t = 0            # where the clock starts
deltat = 0.001   # size of each timestep


# Interactions
# Magnitude of the acceleration due to gravity near Earth's surface
g = 9.8

# Unit vector for the positive y axis (pointing up)
jhat = vector(0,1,0)

# Proportionality constant for the magnitude of the drag force -- EDIT AS NECESSARY
# When b=0, the model is gravity only, no air resistance
b = 0.1



## ======================================
## CALCULATION LOOP
## (motion prediction and visualization)
## ======================================

while t < 0.533:
    # Control how fast the program runs (larger number runs faster)
    rate(200)
    
    # Calculate Net Force -- EDIT THIS NEXT LINE, ADDING MORE LINES AS NECESSARY
    # Gravity
    Fgrav = -ball.m * g * jhat
    
    # Turbulent drag, proportional to the square of the speed,
    # in the direction opposite of the ball's motion
    Fdrag = -b * (mag(ball.vel)**2) * norm(ball.vel)

    # Net force
    Fnet = Fgrav + Fdrag

    # Apply the Momentum Principle (Newton's 2nd Law)
    # Update the object's velocity -- EDIT THIS NEXT LINE
    ball.vel = ball.vel + (Fnet/ball.m)*deltat
    # Update the object's position -- EDIT THIS NEXT LINE
    ball.pos = ball.pos + ball.vel*deltat
    
    # Advance the clock
    t = t + deltat
    # Update the object's track
    trail.append(pos=ball.pos)

    # Plot something as a function of time
    # EDIT THIS NEXT LINE, or add more lines as necessary
    poscurve.plot(t,ball.pos.y)
    velcurve.plot(t,ball.vel.y)
    
    # Draw arrows to represent forces
    # EDIT THE NEXT FIVE LINES
    arrowscale = 0.5 # determines how long to draw the arrows that represent vectors
    arrowGrav.pos = ball.pos
    arrowGrav.axis = arrowscale*Fgrav
    arrowDrag.pos = ball.pos
    arrowDrag.axis = arrowscale*Fdrag

    # Uncomment this next line to print time and position in text field
    # (which you can then copy and paste into a spreadsheet)
    #print(t,ball.pos.y)
    
print("All done!")

