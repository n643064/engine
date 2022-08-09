import pygame
from engine.util import *

def main(model_path):
    model = read_model(model_path)
    if not model:
        print("Couldn't load model.")
        quit(1)
    pygame.init()
    window = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen = pygame.Surface((800, 800))

    clock = pygame.time.Clock()


    projection_matrix = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
    ]

    origin_matrix = [
        (1, 0, 0, -300),
        (0, 1, 0, -300),
        (0, 0, 1, 0),

    ]

    model = project(model, origin_matrix)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
        screen.fill((50, 50, 50))

        keys = pygame.key.get_pressed()
        p_model = project(model, projection_matrix)
        for p in p_model:
            pygame.draw.line(screen, (255, 255, 255), (400 + p[0][0], 400 + p[0][1]), (400 + p[1][0], 400 + p[1][1]), 2)
            pygame.draw.circle(screen, (255, 0, 0), (400 + p[0][0], 400 + p[0][1]), 3)

        for i in range(len(model)):
            model[i] = rotate_y(model[i], 1)
            model[i] = rotate_y(model[i], 1)
            model[i] = rotate_x(model[i], 1)
            model[i] = rotate_x(model[i], 1)
        window.blit(pygame.transform.scale(screen, window.get_size()), (0, 0))
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main("cube.model")