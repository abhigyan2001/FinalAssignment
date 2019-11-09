# Dust Particle Trajectory

## Problem Formulation:

The given problem is stated below:

> Consider a dust particle that gets flushed down the sink. The particle takes a helical path down as
the liquid swirls around while flowing down as it drains. This can be modeled using the following
assumptions: The radial distance of the particle from the center of the sink decreases with
increasing time. The vertical distance of the particle decreases with increasing time. The angular
velocity of the particle is constant. Model the trajectory of the particle and show the same in a 3D
line plot.

## Proposed Solution Methodology:

First, let us find the equation of the particle. We know that <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.395100000000005pt height=14.155350000000013pt/> and <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode" align=middle width=8.649300000000004pt height=14.155350000000013pt/> should be dependent on time <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode" align=middle width=5.936155500000004pt height=20.222069999999988pt/>, and since it is following a helical path with reducing radius, we can assume that:

<p align="center"><img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/bb6613ded971606c4f591612c591c354.svg?invert_in_darkmode" align=middle width=248.82pt height=16.438356pt/></p>

such that <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/ae6cf54c4c6577b7fdc4b52790a95d00.svg?invert_in_darkmode" align=middle width=68.28195pt height=24.65759999999998pt/> where <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/2f118ee06d05f3c2d98361d9c30e38ce.svg?invert_in_darkmode" align=middle width=11.889405000000002pt height=22.46574pt/> is the time the particle takes to reach the bottom.

Now, we also know that the particle's angular velocity is constant, hence we can say:

<p align="center"><img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/5123cba4ed5534050d34aef0ee163e52.svg?invert_in_darkmode" align=middle width=272.12129999999996pt height=50.472345pt/></p>

Now, let us replace <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/a6ebea7e384d94fa4b530bd4804c6ff3.svg?invert_in_darkmode" align=middle width=292.95040499999993pt height=24.716340000000006pt/> into the equation. This yields:

<p align="center"><img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/8b932d37730cfb25caeffb959f427735.svg?invert_in_darkmode" align=middle width=153.64305pt height=41.52258pt/></p>

On squaring both sides and doing some manipulations, we arrive at:

<p align="center"><img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/aa7a881e4c2030a5489510db0508ecd0.svg?invert_in_darkmode" align=middle width=167.8809pt height=17.935005pt/></p>

When we solve the above differential equation, we get:

<p align="center"><img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/29b3caa709495b496edb270ce6473f24.svg?invert_in_darkmode" align=middle width=257.85375pt height=18.75984pt/></p>

Thus, we choose the equation of the curve to be:

<p align="center"><img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/4625f36e0a5092ce6d46791db39753d9.svg?invert_in_darkmode" align=middle width=449.19105pt height=39.45249pt/></p>

## Implementation
We will use implement this in Python using SageMath, as SageMath provides us with a ready library for plotting 3d parametric plots.

We will plot this using the `parametric_plot3d` function of SageMath: (using arbitrary values of <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/1db75c795ab2c794f72bbe79b8113be1.svg?invert_in_darkmode" align=middle width=13.968900000000003pt height=14.155350000000013pt/> and <img src="https://rawgit.com/abhigyan2001/FinalAssignment/master/svgs/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode" align=middle width=9.075495000000004pt height=22.831379999999992pt/>)

## Documentation

### SageMath functions used:

1. `parametric_plot3d(xdata,ydata,options)`
    
    Basically, `parametric_plot3d` draws a polygon by joining the points given in xdata and ydata

2. `show(options)`

    `show()` is called on a plot object to display it. Here, we have used the aspect_ratio option to display lengths along all the axes on a 1:1:1 aspect ratio.
    
3. `exp(t)`
    This returns $e^{t}$, where $e$ is the Euler constant $= 2.718$.

4. `cos(t)`
    This returns the cosine of $t$ assuming $t$ is expressed in radians.
    
5. `sin(t)`
    This returns the sine of $t$ assuming $t$ is expressed in radians.

### Pure Python functions used:

1. `lambda t: f(t)`

    This basically lets us create a nameless function without the use of the `def` keyword. It is meant to be used for use once, throw away functions.
