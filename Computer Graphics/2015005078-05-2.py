import glfw
from OpenGL.GL import *
import numpy as np

def render(M):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv( (M @ np.array([0.,0.,1.]))[:-1] )
    glVertex2fv( (M @ np.array([1.,0.,1.]))[:-1] )
    glColor3ub(0, 255, 0)
    glVertex2fv( (M @ np.array([0.,0.,1.]))[:-1] )
    glVertex2fv( (M @ np.array([0.,1.,1.]))[:-1] )
    glEnd()
    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 255)
    glVertex2fv( (M @ np.array([.0,.5,1.]))[:-1] )
    glVertex2fv( (M @ np.array([.0,.0,1.]))[:-1] )
    glVertex2fv( (M @ np.array([.5,.0,1.]))[:-1] )
    glEnd()
    
def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()

def drawTriangle():
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv(np.array([0.,.5]))
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([.5,0.]))
    glEnd()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(480, 480,"2015005078-5-2", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        th = np.radians(30)
        R = np.array([[np.cos(th), -np.sin(th),0.6],
                      [np.sin(th), np.cos(th),0.],
                      [0.,         0.,        1.]])
        
        render(R)
        drawFrame()
        drawTriangle()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
    
