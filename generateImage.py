# Python Code

# importing the matplotlib library
import matplotlib.pyplot as plt
import numpy as np
from fastapi import FastAPI

app = FastAPI()

@app.post("/generate-image")
async def gen():
    # import for input
    # from js import console

    fig, ax = plt.subplots()

    # predefined values
    c = 0.4+0.23j # determine this from input
    size = 1000
    height = size
    width = size
    x = 0
    y = 0
    zoom = 1
    max_iterations = 100

    # input numbers
    #a = Element('input-real').element.value
    #b = Element('input-imag').element.value
    #c = a+bj

    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5*height/width
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
    div_time = np.zeros(z.shape, dtype=int)

    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)

    for i in range(max_iterations):
        z[m] = z[m]**2 + c[m] 
        m[np.abs(z) > 2] = False
        div_time[m] = i

    # actually showing it
    plt.imshow(div_time, cmap='magma')
    plt.show()
    fig