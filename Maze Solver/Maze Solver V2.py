import pygame, sys
import time
import constants as img

pygame.init()

No_of_Cells =4
width=160*No_of_Cells
height=160*No_of_Cells
screen = pygame.display.set_mode( ( width, height) )

start_cell = [0,0]
target_cell = [2,2]
current_cell = [0,0]

direction =3
status = "Not" 

#Selecting the Maze Pattern
imageMap=img.imageMap1


#Set a Title of Screen
pygame.display.set_caption('Maze Solver')
player=pygame.image.load("images/Maze_Images/player.png").convert_alpha()

            
def update_Player():
    
    global current_cell
    global direction
    
    if direction == 1:
        imgpath=pygame.image.load(img.PlayerN)
    elif direction == 2:
        imgpath=pygame.image.load(img.PlayerE)
    elif direction == 3:
        imgpath=pygame.image.load(img.PlayerS)
    elif direction == 4:
        imgpath=pygame.image.load(img.PlayerW)
    
    screen.blit(imgpath,(160*current_cell[1]+40,160*current_cell[0]+40))


def Yincrement():
    current_cell[0] = current_cell[0] +1

def Ydecrement():
    current_cell[0] = current_cell[0] -1

def Xincrement():
    current_cell[1] = current_cell[1] +1

def Xdecrement():
    current_cell[1] = current_cell[1] -1

def solve():
    global start_cell
    global target_cell 
    global current_cell
    global direction
    global status  
    
    deltaX = abs(target_cell[0]-current_cell[0])
    deltaY = abs(target_cell[1]-current_cell[1])
    
    delY=target_cell[1]-current_cell[1]
    delX=target_cell[0]-current_cell[0]
    
    cellNo = imageMap[current_cell[0]][current_cell[1]]
    
    if deltaX == 0 and deltaY == 0:
        status = "reached"
    else:
        print(cellNo, direction)
        
        if cellNo ==3:
            if direction ==2:
                direction =3
                Yincrement()
            elif direction ==1:
                direction = 4
                Xdecrement()
        
        if cellNo == 4:
            
            
            if direction == 1 and deltaX >= deltaY:
                Xincrement()
                direction =2                
            elif direction == 1 and deltaX < deltaY:
                Ydecrement()                
            elif direction ==3 and delY<0:
                Yincrement()
                direction=3
            elif direction ==3 and delY>=0:
                Xincrement()
                direction=2
            
            elif direction ==4 and delX>=0 :
                Yincrement()
                direction=3
            elif direction ==4 and delX<0 :
                Ydecrement()
                direction=1
        
        if cellNo == 5:
            if direction == 1:
                Ydecrement()
            elif direction == 3:
                Yincrement()
        
        if cellNo == 6:
            if direction ==1:
                direction =2
                Xincrement()
            elif direction ==4:
                Yincrement()
                direction =3
            elif direction ==3:
                Yincrement()
                direction =3
                
        if cellNo == 7:
            if direction == 1:
                direction =3
            elif direction ==3:
                Yincrement()
           
         
        if cellNo == 9:
            if direction == 2:
                Ydecrement()
                direction=1
            elif direction ==3 :
                Xdecrement()
                direction = 4
                
        if cellNo == 12:
            if direction == 3:
                Xincrement()
                direction = 2
            elif direction == 4:
                Ydecrement()
                direction = 1
       
        
            
        
        
                
       
                
                
    
    
    return status

def updateMap():
    
    global path
    global screen
    global image
    
    for col in range(4):
        for row in range(4):
            image=imageMap[col][row]
            imageString=img.imgPath+str(image)+".jpg"
#            print(imageString)
            path=pygame.image.load(imageString)
            screen.blit(path,(160*row,160*col))
            

   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
    
    updateMap()
    update_Player()
    pygame.display.update() 
    
    x= solve() 
    if x=="reached":
        print("Reached")
        time.sleep(3)
        pygame.quit()
        break
    
    
    
    time.sleep(1)       

#    pygame.display.update()
#    time.sleep(0.05)