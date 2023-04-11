import numba
from numba import jit, prange, vectorize

@jit(nopython=True, cache=False, parallel=True, nogil=True)
def julia_set_jit(c:complex=z, height:numba.int8=heightsize, width:numba.int8=widthsize, x:numba.int8=0, y:numba.int8=0, zoom:numba.int8=1, max_iterations:numba.int8=100):
    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5 * height/width
    x_from = x - x_width/zoom
    x_to = x + x_width/zoom
    y_from = y - y_height/zoom
    y_to = y + y_height/zoom



    # Here the actual algorithm starts and the z paramter is defined for the Julia set function
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y

    # Initialize c to the complex number obtained from the quantum circuit
    c = np.full(z.shape, c)

    # To keep track in which iteration the point diverged
    divtime = np.zeros(z.shape, dtype=numba.int8)
    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=numba.bool)

    for i in range(max_iterations):
        for row in range(height):
            for col in range(width):
                if m[row][col]:
                    z[row][col] = z[row][col]**2 + c[row][col]
                    if abs(z[row][col]) > 2:
                        m[row][col] = False
                        div_time[row][col] = i

    return div_time