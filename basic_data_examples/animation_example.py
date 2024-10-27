import streamlit as st
import numpy as np

### A placeholder is a reserved space in an app or interface for dynamic content, updated later.

# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.
# Sidebar sliders for interactive user input.
# 'iterations' slider controls the fractal's level of detail, from 2 to 20, with default 10.
iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
# 'separation' slider controls the spacing factor for the fractal's complex number multiplier.
separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

# Non-interactive elements return a placeholder to their location
# in the app. Here we're storing progress_bar to update it later.
# Sidebar progress bar placeholder, which we update as frames are generated.
progress_bar = st.sidebar.progress(0)

# These two elements will be filled in later, so we create a placeholder
# for them using st.empty()
# Two empty placeholders in the sidebar and main page for dynamic content.
# 'frame_text' shows the current frame count, while 'image' displays the fractal.
frame_text = st.sidebar.empty()
image = st.empty()

# Dimensions and scaling factors for generating the fractal's grid.
# 'm' and 'n' set the grid width and height, while 's' scales the coordinate system.
m, n, s = 960, 640, 400
x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

# Loop to generate 100 frames, with 'a' varying to animate the fractal.
for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
    # Here were setting value for these two elements.
    # Update the progress bar and frame count text as each frame is processed.
    progress_bar.progress(frame_num)
    frame_text.text("Frame %i/100" % (frame_num + 1))

    # Performing some fractal wizardry.
    # Generate complex constant 'c' for this frame, affecting the fractal pattern.
    c = separation * np.exp(
        1j * a
    )  # Uses 'separation' as a multiplier and 'a' as an angle.
    Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))  # Create complex plane matrix 'Z'.
    C = np.full((n, m), c)  # Matrix 'C' with constant 'c' repeated over the grid.
    M = np.full(
        (n, m), True, dtype=bool
    )  # Mask 'M' keeps track of points within bounds.
    N = np.zeros((n, m))  # 'N' tracks the number of iterations per point in the grid.

    # Inner loop runs 'iterations' number of times to calculate the fractal points.
    for i in range(iterations):
        Z[M] = (
            Z[M] * Z[M] + C[M]
        )  # Update points in the complex plane based on Mandelbrot formula.
        M[np.abs(Z) > 2] = False  # Mask out points that escape beyond a set radius.
        N[M] = i  # Record the iteration count for points within bounds.

    # Display the fractal image, normalized to grayscale, updating the image placeholder.
    image.image(1.0 - (N / N.max()), use_column_width=True)

# We clear elements by calling empty on them.
progress_bar.empty()
frame_text.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
