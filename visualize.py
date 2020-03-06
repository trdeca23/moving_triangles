
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.collections import PolyCollection
import matplotlib as mpl


#can we have main and main0 overlap?
#regardless, turn them both into one function (main) with an option for triangles=True

def main(triangle_coords, dist_p0, personal_space, plt_type='points'):

# First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(-.2, 1.2), ylim=(-.2, 1.2))
    z = np.random.random(triangle_coords.n) * 500
    scatter = ax.scatter([], [], s=10, c='black')
#    col0 = PolyCollection([], array=z, cmap=mpl.cm.jet, edgecolors='none', alpha=0.4)
#    ax.add_collection(col0)
    #fig.colorbar(col0, ax=ax)
    #unrelated coolness: https://jakevdp.github.io/blog/2013/05/28/a-simple-animation-the-magic-triangle/
    
# initialization function: plot the background of each frame
    def init():
        return ax,
    
# animation function.  This is called sequentially
    def animate_points(i):
        #print(triangle_coords.p0) #for testing, delete later
        scatter.set_offsets(triangle_coords.p0)
#        scatter = ax.scatter(triangle_coords.p0[:,0],triangle_coords.p0[:,1], s=10, c='black')
        triangle_coords.step(dist_p0, personal_space)
        return scatter,

# animation function.  This is called sequentially
    def animate_triangles(i):
        #print(triangle_coords.p0) #for testing, delete later
        verts = np.concatenate((triangle_coords.p0.reshape(triangle_coords.n,1,2),
                                triangle_coords.p1.reshape(triangle_coords.n,1,2),
                                triangle_coords.p2.reshape(triangle_coords.n,1,2)), axis=1)
        col = PolyCollection(verts, array=z, cmap=mpl.cm.jet, edgecolors='none', alpha=0.4)
        poly = ax.add_collection(col)
        triangle_coords.step(dist_p0, personal_space)
        return poly,

    if plt_type == 'points':
        anim = animate_points
    elif plt_type == 'triangles':
        anim = animate_triangles
    
# call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, anim, init_func=init, #fargs=(triangle_coords,),
                                   frames=None, interval=10, blit=True, save_count=100)
    
# save the animation as an mp4.
#    anim.save('basic_animation.htm', fps=10)

    plt.show()


"""
def main(triangle_coords, dist_p0):

# First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(-.2, 1.2), ylim=(-.2, 1.2))
    scatter = ax.scatter([], [], s=10, c='black')
    
# initialization function: plot the background of each frame
    def init():
        scatter.set_offsets([])
        return scatter,
    
# animation function.  This is called sequentially
    def animate(i):
        #print(triangle_coords.p0) #for testing, delete later
        scatter.set_offsets(triangle_coords.p0)
        triangle_coords.step(dist_p0)
        return scatter,
    
# call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=None, interval=10, blit=True, save_count=100)
    
# save the animation as an mp4.
#    anim.save('basic_animation.htm', fps=10)

    plt.show()
"""

"""
'''
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
"""
