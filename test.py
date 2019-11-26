# import the pygame module, so you can use it
import pygame
import time
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("Rocket game")
    
     
    # create a surface on screen that has the size of 240 x 400
    width = 240
    height = 400
    screen = pygame.display.set_mode((width, height))


    image = pygame.image.load("rocket.jpg")
    size = image.get_rect().size
    left = width/2 - size[0]/2
    top = height/2 + size[1]/2
    white = (255, 255, 255)
    screen.fill((white)) 
    screen.blit(image, (left, top))
    pygame.display.flip()
    print(image.get_rect())
    
    # define a variable to control the main loop
    running = True

    time.sleep(0.5)

    min_y = image.get_rect()[3]
    framerate = 60
    jump = 2
    acceleration = 0.22
    gravity = 0.1
    current_y = top
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


        if pygame.mouse.get_pressed()[0]:
            jump += acceleration
            #Set so can't go below min y
            current_y = current_y - jump

        #if pos[1] < 20:
         #   jump = 2
          #  continue
        jump -= gravity
        current_y = current_y - jump
        
        screen.fill((white))
        screen.blit(image,(left, current_y))
        pygame.display.flip()
        
        time.sleep(1/framerate)

         
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
