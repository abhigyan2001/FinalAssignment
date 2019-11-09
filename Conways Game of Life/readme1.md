# Conway's Game of Life

## Problem Formulation:

The given problem is stated below:
>Convay’s game of life is an interesting but simple game. Consider a 2D array of pixels of which a fraction of them – randomly picked – are colored black and called alive. Rest are white and dead. We visit each pixel and look at its neighbors. If the number of neighbors alive are less than 2 then the pixel dies of underpopulation. If the neighbors are more than 3 then it dies of overpopulation. The pixels evolve to certain fixed patterns and are therefore interesting. The wiki page on this topic is reasonably elaborate.

>Model the Convay’s game for a domain of 100 x 100 size. Feel free to modify the rules for the pixels to live or die.

## Proposed Solution Methodology:

We will randomly generate a matrix of given size to begin with, which will contain ones and zeros only. Ones will represent live cells, and will be drawn in black, while zeros will represent dead cells in white.

We will restrict the game to avoid edges, as edges are implemented differently in different versions of the game, as mentioned later on.

We will try to keep the rules of survival and dying easily changeable, so that someone may change the rules if they wish to by just changing numbers.

Now, we will go through the entire playground while counting neighbours, and we will set the state of the cell depending on it's neighbours to generate the next generation of the playground. We will repeat this a set number of times.

## Implementation:
We will implement this in Octave, due to the easy availability of Matrix operations in Octave.


In the cell below, change the values of size_x and size_y to change the size of the playground in which this game will be played.

We'll now set the rules for the cells to survive and be born. Set `num_born` to zero if you want it to only survive or die without new cells being born.

The starting grid is constructed randomly, with any cell that has a value greater than 0.9 being made 1 and the rest are set to 0. 

(Change the value from 0.1 to smaller if you want more black spots in the original matrix.)

Also, this version of the Conway's game will ignore the edges as the edges could be implemented in a plethora of different ways, such as them being connected across the edges, while others could want the edges not to be connected, while yet others will consider that the grid is an infinite plane, of which we can only see a part. 

Thus, by considering that the edges are non-existent, we are leaving it to interpretation, and to advanced implementations to possibly cover this in the future.

Now, colouring this using imshow...

...but, that's wayyy too small to see clearly... 

Let's make it N-times bigger, and add horizontal and vertical lines to make a clear grid for this

Look at how this already makes things so much easier to see...

(Point to note here is that the rendering of this grid takes longer than the finding of the next generation... That shows just how expensive i/o operations are in any program!)

Algorithm to find the next generation:

Now saving the original `playground` value in a matrix, so that we could use it later if needed.

Now, printing to files...

(Note that the image shown at the bottom of the next cell will be the last image generated by the algorithm, as it shows the figure which was last plotted).

See the video made from the output of these 50 pictures as a .avi file in the `Conway's Game of Life.avi` file in this directory.

## Documentation

### Octave Functions used:
1. `rand(y,x)`
    This creates a matrix of size y$\times$x, where each value is a random number lying between 0 and 1.
    
2. `rand(y,x)>t`
    The `>t` basically converts each value greater than t to a 1, and all remaining values to a 0.
    
3. `imshow(!x)`
    `imshow` renders the matrix `x` as an image. The `!` symbol inverts the matrix, as without it, 0 corresponds to black and 1 corresponds to white, which is the opposite of what we want to display.
    
4. `zeros(y,x)`
    This creates a matrix of size y$\times$x, with each value set as 0.

5. `floor(n)`
    This returns the number `n` rounded down to an integer.

6. `print -options filename`
    This prints the current figure to a file, whose filename is specified and file type is specified using the options.

7. `sprintf(args)`
    This returns a string representation of `args` using the printf syntax used in the C programming language.

8. `eval(code_string)`
    This evaluates the code written in `code_string` treating it as if it were a line of code written in the actual program itself.

### Self-Defined Functions used:
1. `scaleNx(matrix, N)`
    This returns `matrix` scaled up `N` times, such that when it is rendered by `imshow`, each box corresponds to a pixel of the original `matrix` magnified `N` times. It also adds cell boundaries to make it easier to demarcate boundaries.

2. `evalNextGen(currgen,survive_min,survive_max,born)`
    This evaluates the next generation of the Conway's Game, subject to the survival and new-born rules specified by `survive_min`, `survive_max`, and `born`.
