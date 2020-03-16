import numpy as np
import glfw
from OpenGL.GL import *

def render(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_LINE_LOOP)
    
    a = np.linspace(0.0, 360.0, 13)
    for i in range(0, 12):
        a[i] = np.radians(a[i])

    for i in range(0, 12):
        glVertex2f(np.cos(a[i]), np.sin(a[i]))
    glEnd()
    glfw.swap_buffers(window)


def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS :
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        if key == glfw.KEY_1:
            glBegin(GL_POINTS)
        elif key == glfw.KEY_2:
            glBegin(GL_LINES)
        elif key == glfw.KEY_3:
            glBegin(GL_LINE_STRIP)
        elif key == glfw.KEY_4:
            glBegin(GL_LINE_LOOP)
        elif key == glfw.KEY_5 :
            glBegin(GL_TRIANGLES)
        elif key == glfw.KEY_6:
            glBegin(GL_TRIANGLE_STRIP)
        elif key == glfw.KEY_7 :
            glBegin(GL_TRIANGLE_FAN)
        elif key == glfw.KEY_8:
            glBegin(GL_QUADS)
        elif key == glfw.KEY_9:
            glBegin(GL_QUAD_STRIP)
        elif key == glfw.KEY_0 :
            glBegin(GL_POLYGON)
        a = np.linspace(0.0, 360.0, 13)
        for i in range(0, 12):
            a[i] = np.radians(a[i])

        for i in range(0, 12):
            glVertex2f(np.cos(a[i]), np.sin(a[i]))
        glEnd()
        glfw.swap_buffers(window)

def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480,480,"2015005078-2-2", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)

    # Make the window's context current
    glfw.make_context_current(window)
    render(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
