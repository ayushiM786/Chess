import pygame,sys

class Main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Chess")
        self.snake_block = 100
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for y in range(0, int(self.screen.get_height())):
                for x in range(0, int(self.screen.get_width())):
                    if (x + y) % 2 == 0:
                        r = pygame.Rect((x * self.snake_block, y * self.snake_block), (self.snake_block,self.snake_block))
                        pygame.draw.rect(self.screen, (89, 77, 43), r)
                    else:
                        rr = pygame.Rect((x * self.snake_block, y * self.snake_block), (self.snake_block,self.snake_block))
                        pygame.draw.rect(self.screen, (232, 210, 149), rr)
            pygame.display.update()


m = Main()