# import the pygame module, so you can use it
import pygame
import time
 
# define a main function
class rocket_game():
    def __init__(self):
        self.width = 240
        self.height = 400
        self.left = None
        self.top = None
        self.white = (255, 255, 255)
        
        self.screen = None
        self.image = pygame.image.load("rocket.jpg")
        self.size = self.image.get_rect().size
        self.bottom = None
        self.current_y = None

        self.running = True
        self.framerate = 60
        self.jump = 2
        self.acceleration = 0.22
        self.gravity = 0.08        
        
    def main(self):
         
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        pygame.display.set_caption("Rocket game")
        
         
        # create a surface on screen that has the size of 240 x 400
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.left = self.width/2 - self.size[0]/2
        self.bottom = self.height/2 + self.size[1]/2
        self.top = 20
        self.screen.fill((self.white)) 
        self.screen.blit(self.image, (self.left, self.bottom))
        pygame.display.flip()
        
        # define a variable to control the main loop
        time.sleep(0.5)

        self.framerate = 60
        self.jump = 0
        self.acceleration = 0.22
        self.gravity = 0.075
        self.current_y = self.bottom
        
        # main loop
        while self.running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    self.running = False


            if pygame.mouse.get_pressed()[0]:
                self.jump += self.acceleration
                #Set so can't go below min y
                self.current_y = self.current_y - self.jump
                
            self.jump -= self.gravity
            if self.current_y - self.jump > self.bottom:
                self.current_y = self.bottom
                self.jump = 0
            elif self.current_y - self.jump < self.top:
                self.current_y = self.top
                self.jump = 0
            else:
                self.current_y -= self.jump
            
            self.screen.fill(self.white)
            self.screen.blit(self.image,(self.left, self.current_y))
            pygame.display.flip()
            
            time.sleep(1/self.framerate)
    

         
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    game = rocket_game()
    game.main()
