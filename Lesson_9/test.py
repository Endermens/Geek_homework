import pygame
pygame.init()

class  Lights(object):
    green  = (0, 255, 0)
    red = (255, 0, 0)
    yellow = (255, 255, 0)


    screen = pygame.display.set_mode((300, 400))
    pygame.display.set_caption("Сфетофор")
    clock = pygame.time.Clock()

    colors = [green, red, yellow]
    current_index = 0


    timer_interval = 2000 # 2.0 seconds
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, timer_interval)

    running = True
    while running:
        clock.tick(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == timer_event:
                current_index += 1


                if current_index >= len(colors):
                    current_index = 0

        screen.fill(25)
        pygame.draw.circle(screen, colors[current_index], (150, 200), 120)

        pygame.display.flip()

def main():
    Lights()

    pygame.quit()
