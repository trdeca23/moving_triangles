This is a simulation of n points moving in space with the objective of forming equilateral triangles with two randomly assigned pre-specified other points. Meanwhile each of those points is also moving to form equilateral triangles with other points. 

This was inspired by a popular warm-up exercise that takes place in countless dance classes, workshops, etc. People are instructed to move in the dance space while tracking one or more other people. One variant of this exercise instructs people to not only track two other people in the room but to additionally move in order to form an equilateral triangle with those people. Of course much movement ensues at this point. Surely, there are many other variants of these exercises. But here we simply explore this one to understand what this simple rule produces.

We do end up imposing a couple of additional limitations. Everyone is assumed to be inside of a square room (though we could easily change the shape of the room). Sometimes forming an equilateral triangle would require moving to a point outside the room. In addition, people cannot overlap the same point/s in space; in fact, they require a certain margin of room around them to avoid collisions. There are rules in place to address these constraints. 


# INSTRUCTIONS:


1. Create a working directory for the project with the name of your choice and clone GitHub repository https://github.com/trdeca23/moving_triangles to it.


2. Install required libraries to your environment. Required libraries are:
  * os
  * matplotlib
  * numpy


3. Make sure that correct paths and names are specified for:
  * `project_path`, specified at the top of `main.py` script, should point to your project's working directory
  * `plt_type`, specified at the top of `main.py` script, indicates whether to plot points (scatter plot) or triangles. The latter is not recommended since it creates a complex visualization of overlapping transparent triangles. In future updates this might be reworked.
  * `n`, specified at the top of the main.py script, will be the number of points; perhaps start simply with `n=3`, in which case we are guaranteed that each point's objective is the same: namely, to form an equilateral triangle among itself and the other two points
  * `v`, the array of velocities for the points can also be changed. High velocities mean that a point gets closer to its objective position during each step. If the velocity is very high, a point will take one single step to arrive at its objective position. However the other two points will have also moved during this same step. Therefore smaller velocities create more stable moves towards equilibrium positions.


4. Run `main.py`. This will call the other .py scripts to compute positions and visualize them.





# NOTES: 

- Ran this on my Mac ..I don't think I've used any os specific protocols.
