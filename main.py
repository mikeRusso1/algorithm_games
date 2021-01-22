import pygame 

# initiate game
pygame.init()

# create the screen
screen = pygame.display.set_mode((900, 600))

# Title and Icon 
pygame.display.set_caption( "Search Algorithm Visualizer") 
img = pygame.image.load('neural.png') 
pygame.display.set_icon(img) 


# Player 
playerImg = pygame.image.load('robot.png')
playerX = 300
playerY = 300
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    screen.fill((224,224,224))

    # get all events happening 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 


    # key stroke 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.3
            if event.key == pygame.K_RIGHT:
                playerX_change = .3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    
    playerX += playerX_change
    player(playerX, playerY)

    pygame.display.update()

    # image by <div>Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>