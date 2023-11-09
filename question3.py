# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the complex plane domain
x_min = -2.5
x_max = 1.5
y_min = -1.5
y_max = 1.5
num_iter = 100
n_points = 10000

# Define a function to check if a point belongs to the Mandelbrot set
def mandelbrot(c, num_iter):
    z = 0
    for n in range(num_iter):
        # The divergence condition
        if abs(z) > 2:
            return n
        z = z*z + c
    return num_iter

def pure_random_sampling():
    points = []
    for i in range(n_points):
        x = np.random.uniform(x_min, x_max)
        y = np.random.uniform(y_min, y_max)

        c = complex(x, y)
        m = mandelbrot(c, num_iter)
        points.append((x, y, m))
    return points


def latin_hypercube_sampling():
    points = []
    x_intervals = np.linspace(x_min, x_max, n_points + 1)
    y_intervals = np.linspace(y_min, y_max, n_points + 1)

    np.random.shuffle(x_intervals)
    np.random.shuffle(y_intervals)
    for i in range(n_points):
        x = np.random.uniform(x_intervals[i], x_intervals[i + 1])
        y = np.random.uniform(y_intervals[i], y_intervals[i + 1])
    
        c = complex(x, y)
        m = mandelbrot(c, num_iter)
        points.append((x, y, m))
    return points

def orthogonal_sampling():
    points = []
    n_subspaces = int(np.sqrt(n_points))
    x_subspaces = np.linspace(x_min, x_max, n_subspaces + 1)
    y_subspaces = np.linspace(y_min, y_max, n_subspaces + 1)

    for i in range(n_subspaces):
        for j in range(n_subspaces):
            x_intervals = np.linspace(x_subspaces[i], x_subspaces[i + 1], n_subspaces + 1)
            y_intervals = np.linspace(y_subspaces[j], y_subspaces[j + 1], n_subspaces + 1)
            
            np.random.shuffle(x_intervals)
            np.random.shuffle(y_intervals)
            for k in range(n_subspaces):
                x = np.random.uniform(x_intervals[k], x_intervals[k + 1])
                y = np.random.uniform(y_intervals[k], y_intervals[k + 1])
    
                c = complex(x, y)
                m = mandelbrot(c, num_iter)
                points.append((x, y, m))
    return points


points_pure = pure_random_sampling()
points_latin = latin_hypercube_sampling()
points_ortho = orthogonal_sampling()

# Plot
plt.figure(figsize=(15, 4))
plt.subplot(1, 3, 1)
plt.scatter([p[0] for p in points_pure], [p[1] for p in points_pure], c=[p[2] for p in points_pure], cmap='inferno')
plt.title('Pure random sampling')
plt.subplot(1, 3, 2)
plt.scatter([p[0] for p in points_latin], [p[1] for p in points_latin], c=[p[2] for p in points_latin], cmap='inferno')
plt.title('Latin hypercube sampling')
plt.subplot(1, 3, 3)
plt.scatter([p[0] for p in points_ortho], [p[1] for p in points_ortho], c=[p[2] for p in points_ortho], cmap='inferno')
plt.title('Orthogonal sampling')
plt.show()
print(points_pure)
print(points_latin)
print(points_ortho)
