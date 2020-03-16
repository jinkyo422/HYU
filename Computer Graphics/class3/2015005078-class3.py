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
space = False
gstack = None
goffset = None
gsize = 0
gframe = None
gchannel = None
gframenum = 0
goffsetnum = 0
t = 0

def render():
    global fovy, atx, aty, atz, xoffset, yoffset, space, t, gframenum
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovy, 1, 1, 1000)
        
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
    if space == False:
        drawSkeleton()
        t = 0
    elif space == True:
        glfw.swap_interval(1)
        t += 1
        t = t%gframenum       
        moveSkeleton(t)

def moveSkeleton(t):
    global gstack, goffset, gsize, gframe, gchannel, gframenum, goffsetnum

    index = 0
    num = 0

    for i in range(gsize):
        if gstack[i] == 1:
            glPushMatrix()
            temp = np.array(goffset[index])
            index += 1
            index = index%goffsetnum
            drawLine(temp)
            glTranslatef(temp[0], temp[1], temp[2])

            if gstack[i+1] == -1:
                continue

            if i == 0:
                if gchannel[num] == "XPOSITION" or gchannel[num] == "Xposition":
                    if gchannel[num+1] == "YPOSITION" or gchannel[num+1] == "Yposition":
                        glTranslate(float(gframe[t][num]), float(gframe[t][num+1]), float(gframe[t][num+2])) #xyz
                    elif gchannel[num+1] == "ZPOSITION" or gchannel[num+1] == "Zposition":
                        glTranslate(float(gframe[t][num]), float(gframe[t][num+2]), float(gframe[t][num+1])) #xzy

                elif gchannel[num] == "YPOSITION" or gchannel[num] == "Yposition":
                    if gchannel[num+1] == "XPOSITION" or gchannel[num+1] == "Xposition":
                        glTranslate(float(gframe[t][num+1]), float(gframe[t][num]), float(gframe[t][num+2])) #yxz
                    elif gchannel[num+1] == "ZPOSITION" or gchannel[num+1] == "Zposition":
                        glTranslate(float(gframe[t][num+2]), float(gframe[t][num]), float(gframe[t][num+1])) #yzx

                elif gchannel[num] == "ZPOSITION" or gchannel[num] == "Zposition":
                    if gchannel[num+1] == "XPOSITION" or gchannel[num+1] == "Xposition":
                        glTranslate(float(gframe[t][num+1]), float(gframe[t][num+2]), float(gframe[t][num])) #zxy
                    elif gchannel[num+1] == "YPOSITION" or gchannel[num+1] == "Yposition":
                        glTranslate(float(gframe[t][num+2]), float(gframe[t][num+1]), float(gframe[t][num])) #zyx
                num += 3

            if gchannel[num] == "XROTATION" or gchannel[num] == "Xrotation":
                if gchannel[num+1] == "YROTATION" or gchannel[num+1] == "Yrotation": #xyz
                    glRotate(float(gframe[t][num]), 1, 0, 0)
                    glRotate(float(gframe[t][num+1]), 0, 1, 0)
                    glRotate(float(gframe[t][num+2]), 0, 0, 1)
                elif gchannel[num+1] == "ZROTATION" or gchannel[num+1] == "Zrotation": #xzy
                    glRotate(float(gframe[t][num]), 1, 0, 0)
                    glRotate(float(gframe[t][num+1]), 0, 0, 1)
                    glRotate(float(gframe[t][num+2]), 0, 1, 0)

            elif gchannel[num] == "YROTATION" or gchannel[num] == "Yrotation":
                if gchannel[num+1] == "XROTATION" or gchannel[num+1] == "Xrotation": #yxz
                    glRotate(float(gframe[t][num]), 0, 1, 0)
                    glRotate(float(gframe[t][num+1]), 1, 0, 0)
                    glRotate(float(gframe[t][num+2]), 0, 0, 1)
                    
                elif gchannel[num+1] == "ZROTATION" or gchannel[num+1] == "Zrotation": #yzx
                    glRotate(float(gframe[t][num]), 0, 1, 0)
                    glRotate(float(gframe[t][num+1]), 0, 0, 1)
                    glRotate(float(gframe[t][num+2]), 1, 0, 0)

            elif gchannel[num] == "ZROTATION" or gchannel[num] == "Zrotation":
                if gchannel[num+1] == "XROTATION" or gchannel[num+1] == "Xrotation": #zxy
                    glRotate(float(gframe[t][num]), 0, 0, 1)
                    glRotate(float(gframe[t][num+1]), 1, 0, 0)
                    glRotate(float(gframe[t][num+2]), 0, 1, 0)
                elif gchannel[num+1] == "YROTATION" or gchannel[num+1] == "Yrotation": #zyx
                    glRotate(float(gframe[t][num]), 0, 0, 1)
                    glRotate(float(gframe[t][num+1]), 0, 1, 0)
                    glRotate(float(gframe[t][num+2]), 1, 0, 0)

            num += 3
                
        elif gstack[i] == -1:
            glPopMatrix()

def drawSkeleton():
    global gstack, goffset, gsize, gframe, gchannel, gframenum
    
    index = 0

    for i in range(gsize):
        if gstack[i] == 1:
            glPushMatrix()
            temp = np.array(goffset[index])
            index += 1
            drawLine(temp)
            glTranslatef(temp[0], temp[1], temp[2])
        elif gstack[i] == -1:
            glPopMatrix()

def drawLine(v):
    glBegin(GL_LINES)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(v)
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

def drop_callback(window, paths):
    global gstack, goffset, gsize, gframe, gchannel, gframenum, goffsetnum

    stack = []
    offset = []
    num = 0
    name = []
    size = 0
    frame = []
    framenum = 0
    fps = 0
    flag = False
    index = 0
    channel = []
    offsetnum = 0

    obj = open(paths[0], 'r')
    lines = obj.readlines()
    for line in lines:
        item = line.lstrip().split()

        if flag == True:
            temp = np.array(item)
            for i in range(temp.size):
                frame[index].append(float(temp[i]))
            index += 1
            
        elif item[0] == "ROOT" or item[0] == "JOINT":
            name.append([])
            name[num] = item[1]
            num += 1
        
        elif item[0] == "{":
            stack.append(1)
            size += 1
            
        elif item[0] == "OFFSET":
            offset.append((float(item[1]), float(item[2]), float(item[3])))
            offsetnum += 1

        elif item[0] == "CHANNELS":
            if item[1] == "6":
                for i in range(2, 8):
                    channel.append(item[i])
            elif item[1] == "3":
                for i in range(2, 5):
                    channel.append(item[i])
            
        elif item[0] == "}":
            stack.append(-1)
            size += 1

        elif item[0] == "Frames:":
            framenum = (int)(item[1])
            for i in range(framenum):
                frame.append([])
            
        elif item[0] == "Frame":
            fps = 1/(float)(item[2])
            flag = True
            
    print("File name : %s"%paths[0])
    print("Number of frames : %d"%framenum)
    print("FPS : %f"%fps)
    print("Number of joints(including root) : %d"%num)
    print("List of all joint names : ")
    print(name)
    
    gstack = stack
    goffset = offset
    gsize = size
    gframe = frame
    gchannel = channel
    gframenum = framenum
    goffsetnum = offsetnum
    
def key_callback(window, key, scancode, action, mods):
    global space
    if action==glfw.PRESS or action==glfw.REPEAT:
        if key==glfw.KEY_SPACE:
            space = not space
                
def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'2015005078-class3', None,None)
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
