from asyncio.windows_events import NULL
import pygame
import CLASSES as c
import random as r
import CONVEXHULL as cv 
import cosmetics as cm
import setpoints as se
import CVHscreen as cvhp
import setline as sl
import LIINESEC as lint
import linescreen as ll
import WHAT as w
import creds
#pygame kachra =-=-=-=--=-=-
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()
background =(0,15,15)
exiet = 0
def ext(a = 0):
    global exiet
    exiet = 1
pygame.mouse.set_visible(False)    

#mouse effects
firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
tr = c.trail(firstset,7)

#menu text
hcolor = (0,158,158)
headin = c.Text("Geometric Algorithms",cm.fonts[0],50,hcolor,320,90)
dot = c.point(0,0,(0,27,27),10)
dotbig = c.point(0,0,(0,17,17),5)
dotvbig = c.point(0,0,(0,16,16),5)
dot_interval = 400
last_dot_time = 0
l = c.line(1,10,(50,50,50))
screen.fill(background)


#buttons
def dummdumm(screen = NULL):
    print("dumdum")
b1 = 540
b2 = 180
o = 35
buttoncolor = (0,170,170)

button0 = c.Button("Set Points"       ,b1-10 ,b2      ,150,25,cm.fonts[0],20,buttoncolor,se.sets)
button1 = c.Button("Set Line"         ,b1-10 ,b2+(o*1),150,25,cm.fonts[0],20,buttoncolor,sl.setline)
button2 = c.Button("Convex Hull"      ,b1-20 ,b2+(o*2),170,25,cm.fonts[0],20,buttoncolor,cvhp.conv)
button3 = c.Button("Line Intersection",b1+3  ,b2+(o*3),130,25,cm.fonts[0],20,buttoncolor,ll.conv)
button4 = c.Button("What is a...?"    ,b1    ,b2+(o*4),130,25,cm.fonts[0],20,buttoncolor,w.what)
button5 = c.Button("Credits"          ,b1    ,b2+(o*5),130,25,cm.fonts[0],20,buttoncolor,creds.creds)
button6 = c.Button("Exit"             ,b1    ,b2+(o*6),130,25,cm.fonts[0],20,buttoncolor,ext)
butt = [button0,button1,button2,button3,button4,button5,button6] 
page_requested = None
#=-=-=-
fps = round(clock.get_fps(),2)
fp = str(fps)
fm = c.Text(fp,cm.fonts[0],12,(0,50,50),10,700)
dframe = c.point(10,700,(0,10,10),70)

while running:
    if exiet == 1 :
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:  
            for a in butt:           
                a.is_hovered = a.x < event.pos[0] < a.x + a.width and a.y < event.pos[1] < a.y + a.height
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for a in butt:
                if a.is_hovered:
                   a.is_clicked = True       
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for a in butt:
                if a.is_hovered and a.is_clicked:
                    a.is_clicked = False
                    page_requested = a.action 
                    break
    if page_requested:
        screen.fill(background)  
        page_requested(screen)  
        screen.fill(background)
        page_requested = None 

    #for n,a in enumerate(butt):
    #    print(n,a.is_hovered,a.is_clicked)
    mouse = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()
    if current_time - last_dot_time > dot_interval:
        dotvbig.update_coords((r.randint(0,width),r.randint(0,height)))
        dot.update_coords((r.randint(0,width),r.randint(0,height)))
        dotbig.update_coords((r.randint(0,width),r.randint(0,height)))
        dotvbig.draw(screen)
        dotbig.draw(screen)
        dot.draw(screen)
        last_dot_time = current_time
    #-=-=-=-=-==# Add a random dot
    for a in butt:
        a.draw(screen)
    print(mouse)
    headin.draw(screen)
    fm.update_text(str(round(clock.get_fps(),2)))
    dframe.draw(screen)
    fm.draw(screen)
    #trailstart
    tr.erasetrail(screen,background)
    tr.updatetrail(mouse)
    tr.drawtrail(screen)
    #trailend

    pygame.display.flip()

    clock.tick(60)


