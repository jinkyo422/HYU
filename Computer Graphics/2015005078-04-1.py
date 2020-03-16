import glfw
from OpenGL.GL import *
import numpy as np

T = np.array([[1.,0.,0.],
              [0.,1.,0.],
              [0.,0.,1.]])

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv( (T @ np.array([.0,.5,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.0,.0,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.5,.0,1.]))[:-1] )
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global T
    if action == glfw.PRESS :
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        if key == glfw.KEY_Q:
            newM = np.array([[1.,0.,-0.1],
                             [0.,1.,0.],
                             [0.,0.,1.]])
            T = newM @ T
        elif key == glfw.KEY_E:
            newM = np.array([[1.,0.,0.1],
                             [0.,1.,0.],
                             [0.,0.,1.]])
            T = newM @ T
        elif key == glfw.KEY_A:
            th = np.radians(10)
            newM = np.array([[np.cos(th), -np.sin(th),0.],
                          [np.sin(th), np.cos(th),0.],
                          [0.,         0.,        1.]])
            T = T @ newM
        elif key == glfw.KEY_D:
            th = np.radians(-10)
            newM = np.array([[np.cos(th), -np.sin(th),0.],
                          [np.sin(th), np.cos(th),0.],
                          [0.,         0.,        1.]])
            T = T @ newM
        elif key == glfw.KEY_1:
            T = np.array([[1.,0.,0.],
                        [0.,1.,0.],
                        [0.,0.,1.]])

def main():
    if not glfw.init():
        return
    window = glfw.create_window(480, 480,"2015005078-3-2", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(T)
        glfw.set_key_callback(window, key_callback)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
