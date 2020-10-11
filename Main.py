import pygame, sys
from random import randint

#========== let the boredom begin! ==========
class Bore:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Boring game")
        self.font = pygame.font.SysFont('Helvetica', 35)

    def draw(self, x, y):
        pygame.draw.circle(self.screen, RED, (x, y), 10)
        pygame.draw.circle(self.screen, RED, (x, y), 40, 1)
        pygame.draw.rect(self.screen, GREEN, (x-40, y-40, 80, 80), 2)

    def prey(self, color, x, y): pygame.draw.rect(self.screen, color, (x, y, 40, 50))
        
    def main(self):
        global RED, GREEN, WHITE
        x = 350
        y = 270
        vel = 1
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        WHITE = (255, 255, 255)
        Y = 0
        X = randint(12, 690)
        speed = 1
        score = 0
        color = WHITE
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (x > X) and (x<X+40) and (y > Y) and (y <Y+50):
                        score += 1
                        #/*---this can be added depending on preferance---*/#speed += float(0.1)
                        Y = 0
                        X = randint(12, 690)

            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT] and x<800:
                x+= vel
            if key[pygame.K_LEFT] and x>0:
                x-=vel
            if key[pygame.K_UP] and y>0:
                y -= vel
            if key[pygame.K_DOWN] and y<700:
                y += vel
            if Y >600:
                Y -= 700
                X = randint(12, 690)
                score -= 1
            self.screen.fill((0, 0, 0))
            Y += speed
            prey = self.prey(color, X, Y)
            gun = self.draw(x, y)
            self.screen.blit(self.font.render(f'SCORE: {score}', True, WHITE), (550, 30))
            pygame.display.update()
            
if __name__=='__main__':
    AI = Bore()
    AI.main()
