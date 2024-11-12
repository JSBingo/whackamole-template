import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        a = 0
        b = 0
        screen.fill("light green")
        start_pos = [0, 0]
        end_pos = [0, 512]
        start = [0, 0]
        end = [640, 0]
        for i in range(0, 513):
            pygame.draw.line(screen, 'black', start_pos, end_pos)
            start_pos[0] = i * 32
            end_pos[0] = i * 32
        for i in range(0, 641):
            pygame.draw.line(screen, 'black', start, end)
            start[1] = i * 32
            end[1] = i * 32

        screen.blit(mole_image, mole_image.get_rect(topleft=(a, b)))
        while running:



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if a == event.pos[0]//32 and b == event.pos[1]//32 :
                        screen.fill("light green")
                        for i in range(0, 513):
                            pygame.draw.line(screen, 'black', start_pos, end_pos)
                            start_pos[0] = i * 32
                            end_pos[0] = i * 32
                        for i in range(0, 641):
                            pygame.draw.line(screen, 'black', start, end)
                            start[1] = i * 32
                            end[1] = i * 32
                        a = random.randrange(0, 9)
                        b = random.randrange(0, 9)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(a * 32, b * 32)))

            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
