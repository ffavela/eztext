# EzText example
from pygame.locals import *
import pygame, sys, eztext

#defining some colors
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

def check_float(arg):
    try:
        float(arg)
    except:
        print arg,"is no float"
        return False
    return True

def main():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((640,240))
    # fill the screen w/ black
    screen.fill(black)
    ypos=0
    deltay=25
    txtbx=[]
    elemNumber=3
    #For getting the return values
    a=['' for i in range(elemNumber)]
    b=['default' for i in range(elemNumber)]
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here $i: '
    for i in range(elemNumber):
        txtbx.append(eztext.Input(maxlength=6,
                                color=blue,y=ypos,
                                  prompt='type here '+str(i)+': '))
        ypos+=deltay

    foci=0 #The focus index
    txtbx[foci].focus=True
    txtbx[foci].color=red

    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    while True:
        # make sure the program is running at 30 fps
        clock.tick(30)

        # events for txtbx
        events = pygame.event.get()
        # process other events
        for event in events:
            # close it x button si pressed
            if event.type == QUIT: return

        # clear the screen
        screen.fill(black)#I like black better :)
        for i in range(elemNumber):
            # update txtbx and get return val
            a[i]=txtbx[i].update(events)
            if i==foci:
                txtbx[i].focus=True
                txtbx[i].color=red
            else:
                txtbx[i].focus=False
                txtbx[i].color=blue
                
            # blit txtbx[i] on the screen
            txtbx[i].draw(screen)

        #Changing the focus to the next element 
        #every time enter is pressed
        for i in range(elemNumber):
            if a[i] != None:
                b[i]=a[i]
                if check_float(b[i]):
                    print "Doing simple operation"
                    print "2*b["+str(i)+"] = ",2*float(b[i])
                txtbx[i].focus=False
                txtbx[i].color=blue
                txtbx[(i+1)%elemNumber].focus=True
                txtbx[(i+1)%elemNumber].color=red
                foci=(i+1)%elemNumber

        # refresh the display
        pygame.display.flip()

if __name__ == '__main__': main()
