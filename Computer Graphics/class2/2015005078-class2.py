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
Z = GL_LINE
S = True
gVertexArraySeparate = None
gVertexArrayIndexed = None
gIndexArray = None
normal = None

def render():
    global fovy, atx, aty, atz, xoffset, yoffset, Z, S
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
    
    glPolygonMode( GL_FRONT_AND_BACK, Z )
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_RESCALE_NORMAL)
    
    lightPos = (4.,5.,6.,1.)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    ambientLightColor = (.1,.1,.1,1.)
    diffuseLightColor = (1.,1.,1.,1.)
    specularLightColor = (1.,1.,1.,1.)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLightColor)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLightColor)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specularLightColor)

    lightPos = (-3.,4.,-5.,1.)
    glLightfv(GL_LIGHT1, GL_POSITION, lightPos)
    ambientLightColor = (.1,.1,.1,1.)
    diffuseLightColor = (0.,0.,1.,1)
    specularLightColor = (0.,0.,1.,1)
    glLightfv(GL_LIGHT1, GL_AMBIENT, ambientLightColor)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuseLightColor)
    glLightfv(GL_LIGHT1, GL_SPECULAR, specularLightColor)
    
    objectColor = (1.,0.,0.,1.)
    specularObjectColor = (1.,1.,1.,1.)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, objectColor)
    glMaterialfv(GL_FRONT, GL_SHININESS, 10)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specularObjectColor)

    if S==True:
        drawUnitCube_glDrawArray()
    elif S==False:
        drawCube_glDrawElements()
    
    glDisable(GL_LIGHTING)
    
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

def drop_callback(window, paths):
    global gVertexArraySeparate, gVertexArrayIndexed, gIndexArray, normal

    varr = []
    vparr = []
    vnarr = []
    iarr = []
    smooth = []
    sarr = []
    vnum = 0
    
    count1 = 0
    count2 = 0
    count3 = 0

    obj = open(paths[0], 'r')
    lines = obj.readlines()
    for line in lines:
        item = line.lstrip().split(" ")
        if item[0] == "v":
            vparr.append((float(item[1]), float(item[2]), float(item[3])))
            smooth.append([])
            smooth[vnum] = np.array([0., 0., 0.])
            vnum += 1
            
        elif item[0] == "vn":
            vnarr.append((float(item[1]), float(item[2]), float(item[3])))

        elif item[0] == "f":
            face = np.array(item[1:])
            facesize = np.size(face)
            
            if facesize == 3:
                count1 += 1
            elif facesize == 4:
                count2 += 1
            elif facesize > 4:
                count3 += 1

            temp1 = item[1].split('/')
            varr.append(vnarr[int(temp1[2])-1])
            varr.append(vparr[int(temp1[0])-1])

            i = 2
            while i < facesize:
                temp2 = item[i].split('/')
                varr.append(vnarr[int(temp2[2])-1])
                varr.append(vparr[int(temp2[0])-1])
                    
                temp3 = item[i+1].split('/')
                varr.append(vnarr[int(temp3[2])-1])
                varr.append(vparr[int(temp3[0])-1])
                
                v1 = np.array(vparr[int(temp2[0])-1]) - np.array(vparr[int(temp1[0])-1])
                v2 = np.array(vparr[int(temp3[0])-1]) - np.array(vparr[int(temp1[0])-1])

                vtemp = np.cross(v1,v2)
                v = vtemp/np.sqrt(np.dot(vtemp,vtemp))
                
                smooth[int(temp1[0])-1] += np.array([v[0],v[1],v[2]])
                smooth[int(temp2[0])-1] += np.array([v[0],v[1],v[2]])
                smooth[int(temp3[0])-1] += np.array([v[0],v[1],v[2]])
                
                iarr.append((float(int(temp1[0])-1),
                             float(int(temp2[0])-1), float(int(temp3[0])-1)))
                
                i += 1
                if i == facesize:
                    continue
                varr.append(vnarr[int(temp1[2])-1])
                varr.append(vparr[int(temp1[0])-1])
          
    gVertexArraySeparate = varr
    gVertexArrayIndexed = vparr
    gIndexArray = iarr
    print(vnarr)
    print(vparr)
    for i in range(vnum):
        value = smooth[i]/np.sqrt(np.dot(smooth[i], smooth[i]))
        sarr.append((value[0], value[1], value[2]))
    normal = sarr
    total = count1 + count2 + count3
    print("File name : %s"%paths[0])
    print("Total number of faces : %d"%total)
    print("Number of faces with 3 vertices : %d"%count1)
    print("Number of faces with 4 vertices : %d"%count2)
    print("Number of faces with more than 4 vertices : %d"%count3)
    
def drawUnitCube_glDrawArray():
    global gVertexArraySeparate
    varr = np.array(gVertexArraySeparate)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glNormalPointer(GL_DOUBLE, 6 * varr.itemsize, varr)
    glVertexPointer(3, GL_DOUBLE, 6 * varr.itemsize, ctypes.c_void_p(varr.ctypes.data + 3 * varr.itemsize))
    glDrawArrays(GL_TRIANGLES, 0, int(varr.size / 6))

def drawCube_glDrawElements():
    global gVertexArrayIndexed, gIndexArray, normal
    vparr = np.array(gVertexArrayIndexed)
    iarr = np.array(gIndexArray)
    narr = np.array(normal)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glNormalPointer(GL_DOUBLE, 3*vparr.itemsize, narr)
    glVertexPointer(3, GL_DOUBLE, 3*vparr.itemsize, vparr)
    glDrawElements(GL_TRIANGLES, iarr.size, GL_UNSIGNED_INT, iarr)

def key_callback(window, key, scancode, action, mods):
    global Z, S
    if action==glfw.PRESS or action==glfw.REPEAT:
        if key==glfw.KEY_Z:
            if Z == GL_LINE:
                Z = GL_FILL
            elif Z == GL_FILL:
                Z = GL_LINE
        elif key==glfw.KEY_S:
            S = not S
                
def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'2015005078-class2', None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_cursor_pos_callback(window, cursor_callback)    
    glfw.set_mouse_button_callback(window, button_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    glfw.set_drop_callback(window, drop_callback)
    glfw.set_key_callback(window, key_callback)
    
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
