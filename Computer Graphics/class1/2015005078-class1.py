import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

fovy = 120.
gCamAng = np.radians(45)
gCamHeight = 2.
x = 0.
y = 0.
atx = 0
aty = 0
atz = 0
xoffset = 0.
yoffset = 0.
left = False
right = False

def render():
    global fovy, atx, aty, atz, xoffset, yoffset
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovy, 1, 1,1000)
        
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    eye = np.array([3*np.sin(gCamAng),gCamHeight,3*np.cos(gCamAng)])
    at = np.array([atx,aty,atz])
    up = np.array([0,1,0])
    gluLookAt(eye[0],eye[1],eye[2],at[0],at[1],at[2],0,1,0)
    temp1 = eye-at
    w = temp1/np.sqrt(np.dot(temp1,temp1))
    temp2 = np.cross(up, w)
    u = temp2/np.sqrt(np.dot(temp2,temp2))
    v = np.cross(w, u)
    glTranslatef(u[0]*xoffset, u[1]*xoffset, u[2]*xoffset)
    glTranslatef(v[0]*yoffset, v[1]*yoffset, v[2]*yoffset)

    drawFrame()
    glColor3ub(100, 100, 100)
    drawGrid()
    glColor3ub(255, 255, 255)
    drawCube()
    t = glfw.get_time()

    #body
    glPushMatrix()
    glTranslatef(0, 1+np.sin(6*t)/5, 0)
    glColor3ub(233, 228, 206)
    
    glPushMatrix()
    glScalef(.5,1.5,.5)
    drawSphere()
    glPopMatrix()

    #head
    glPushMatrix()
    glTranslatef(0, 1.65, 0.)
    glRotatef(15*np.sin(6*t), 0, 0, 1)
    glScalef(.2, .2, .2)
    drawSphere()
    glPopMatrix()

    #leftuparm
    glPushMatrix()
    glTranslatef(0, 1.25+np.sin(6*t)/30, -.5-np.sin(6*t)/30)
    
    glPushMatrix()
    glRotatef(30,1,0,0)
    glScalef(.2,.4,.2)
    drawSphere()
    glPopMatrix()
    
    #leftunderarm
    glPushMatrix()
    glTranslatef(0, -.7, -.3)
    glRotatef(15*np.sin(-6*t), 0, 0, 1)
    glScalef(.2,.4,.2)
    drawSphere()
    glPopMatrix()
    glPopMatrix()

    #leftupleg
    glPushMatrix()
    glTranslatef(0, -1.65, -0.3)

    glPushMatrix()
    glScalef(.2,.5,.2)
    drawSphere()
    glPopMatrix()

    #leftunderleg
    glPushMatrix()
    glTranslatef(0, -1., 0)

    glPushMatrix()
    glScalef(.2,.5,.2)
    drawSphere()
    glPopMatrix()

    #leftfoot
    glPushMatrix()
    glTranslatef(.2, -.5, 0)
    glRotate(90,0,0,1)
    glScalef(.1,.2,.1)
    drawSphere()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

    #rightuparm
    glPushMatrix()
    glTranslatef(0, 1.3+np.sin(6*t)/30, .7+np.sin(6*t)/30)
    glRotatef(90,1,0,0)
    theta = np.sin(6*t)*(180/np.pi) - 180/np.pi
    glRotatef(theta,0,1,0)
    
    glPushMatrix()
    glScalef(.2,.4,.2)
    drawSphere()
    glPopMatrix()

    #rightunderarm
    glPushMatrix()
    glRotatef(-90,1,0,0)
    glTranslatef(0, .3, .3)
    glScalef(.2,.4,.2)
    drawSphere()
    glPopMatrix()
    glPopMatrix()

    #rightupleg
    glPushMatrix()
    glTranslatef(0.3, -1.65, 0.3)
    glRotate(30,0,0,1)
    theta = np.sin(6*t)*(60/np.pi)
    glRotatef(-theta,0,0,1)

    glPushMatrix()
    glScalef(.2,.5,.2)
    drawSphere()
    glPopMatrix()

    #rightunderleg
    glPushMatrix()
    glTranslatef(-.3, -.7, 0)
    glRotate(-60,0,0,1)
    theta = np.sin(6*t)*(90/np.pi) + 30/np.pi
    glRotatef(-theta,0,0,1)

    glPushMatrix()
    glScalef(.2,.5,.2)
    drawSphere()
    glPopMatrix()

    #rightfoot
    glPushMatrix()
    glTranslatef(.2, -.5, 0)
    glRotate(90,0,0,1)
    glScalef(.1,.2,.1)
    drawSphere()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

    glPopMatrix()

# draw a sphere of radius 1, centered at the origin.
# numLats: number of latitude segments
# numLongs: number of longitude segments
def drawSphere(numLats=12, numLongs=12):
    for i in range(0, numLats + 1):
        lat0 = np.pi * (-0.5 + float(float(i - 1) / float(numLats)))
        z0 = np.sin(lat0)
        zr0 = np.cos(lat0)
        
        lat1 = np.pi * (-0.5 + float(float(i) / float(numLats)))
        z1 = np.sin(lat1)
        zr1 = np.cos(lat1)
        
        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)
        
        for j in range(0, numLongs + 1):
            lng = 2 * np.pi * float(float(j - 1) / float(numLongs))
            x = np.cos(lng)
            y = np.sin(lng)
            glVertex3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr1, y * zr1, z1)

        glEnd()

def drawCube():
    glBegin(GL_QUADS)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)

    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)

    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)

    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)

    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glEnd()

def drawFrame():
    # draw coordinate: x in green, y in blue, z in red
    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,0.,1.]))
    glEnd()

def drawGrid():
    glBegin(GL_QUADS)
    for i in range(-5, 6):
        for j in range (-5, 6):
            glVertex3f( i+1.0, 0.,j-1.0)
            glVertex3f( i-1.0, 0.,j-1.0)
            glVertex3f( i-1.0, 0.,j+1.0)
            glVertex3f( i+1.0, 0.,j+1.0)
    glEnd()

def cursor_callback(window, xpos, ypos):
    global gCamHeight, gCamAng, x, y, left, right, xoffset, yoffset
    if left == True:
        gCamAng = gCamAng + (x-xpos)/20
        x = xpos
        gCamHeight = gCamHeight + (ypos-y)/10
        y = ypos
    if right == True:
        xoffset = xoffset + (xpos-x)/20
        x = xpos
        yoffset = yoffset + (y-ypos)/10
        y = ypos
        
def button_callback(window, button, action, mod):
    global x, y, left, right, at
    if button==glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS or action == glfw.REPEAT:
            x, y = glfw.get_cursor_pos(window)
            left = True
        elif action == glfw.RELEASE:
            left = False
    if button==glfw.MOUSE_BUTTON_RIGHT:
        if action == glfw.PRESS or action == glfw.REPEAT:
            x, y = glfw.get_cursor_pos(window)
            right = True
        elif action == glfw.RELEASE:
            right = False
                
def scroll_callback(window, xoffset, yoffset): #zooming
    global fovy
    fovy -= yoffset
    
def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'2015005078-class1', None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_cursor_pos_callback(window, cursor_callback)    
    glfw.set_mouse_button_callback(window, button_callback)
    glfw.set_scroll_callback(window, scroll_callback)
     
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
