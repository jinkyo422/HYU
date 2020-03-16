import glfw
from OpenGL.GL import *
import numpy as np

gComposedM = np.array([[1.,0.,0.],
                      [0.,1.,0.],
                      [0.,0.,1.]])

def render(window):
    global gComposedM
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
    glVertex2fv( (gComposedM @ np.array([.0,.5,1.]))[:-1] )
    glVertex2fv( (gComposedM @ np.array([.0,.0,1.]))[:-1] )
    glVertex2fv( (gComposedM @ np.array([.5,.0,1.]))[:-1] )
    glEnd()
    glfw.swap_buffers(window)

def key_callback(window, key, scancode, action, mods):
    global gComposedM
    if action == glfw.PRESS :
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        if key == glfw.KEY_W:
            newM = np.array([[.9,0.,0.],
                             [0.,1.,0.],
                             [0.,0.,1.]])
            gComposedM = newM @ gComposedM
        elif key == glfw.KEY_E:
            newM = np.array([[1.1,0.,0.],
                             [0.,1.,0.],
                             [0.,0.,1.]])
            gComposedM = newM @ gComposedM
        elif key == glfw.KEY_S:
            th = np.radians(10)
            newM = np.array([[np.cos(th), -np.sin(th),0.],
                          [np.sin(th), np.cos(th),0.],
                          [0.,         0.,        1.]])
            gComposedM = newM @ gComposedM
        elif key == glfw.KEY_D:
            th = np.radians(-10)
            newM = np.array([[np.cos(th), -np.sin(th),0.],
                          [np.sin(th), np.cos(th),0.],
                          [0.,         0.,        1.]])
            gComposedM = newM @ gComposedM
        elif key == glfw.KEY_X:
            newM = np.array([[1.,-0.1,0.],
                             [0.,1.,0.],
                             [0.,0.,1.]])
            gComposedM = newM @ gComposedM         
        elif key == glfw.KEY_C:
            newM = np.array([[1.,0.1,0.],
                             [0.,1.,0.],
                             [0.,0.,1.]])
            gComposedM = newM @ gComposedM          
        elif key == glfw.KEY_R:
            newM = np.array([[1.,0.,0.],
                             [0.,-1.,0.],
                             [0.,0.,1.]])
            gComposedM = newM @ gComposedM 
        elif key == glfw.KEY_1:
            gComposedM = np.array([[1.,0.,0.],
                                  [0.,1.,0.],
                                  [0.,0.,1.]])
        render(window)

def main():
    if not glfw.init():
        return
    window = glfw.create_window(480, 480,"2015005078-3-2", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)

    glfw.make_context_current(window)
    render(window)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
    
