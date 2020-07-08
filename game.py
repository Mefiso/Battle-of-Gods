from packages.players.battler import Battler
from packages.utilities import *


def resolve_battle(sprites, current_attacks):
    for s in sprites.sprites():
        s.retreat()
    print("gg")


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Battle of Gods')
    background, _ = load_image('backgrounds/background.jpeg')
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0, 0))

    elems1 = {'fire': 2, 'water': 3, 'earth': 3, 'air': 1}
    elems2 = {'fire': 1, 'water': 3, 'earth': 2, 'air': 3}

    battlers = (
        Battler(0, 'sprites/test1.jpeg', (0, 200), elems1, 7), Battler(1, 'sprites/test2.jpeg', (500, 200), elems2, 7))
    allsprites = pygame.sprite.RenderPlain(battlers)
    allsprites.draw(screen)
    pygame.display.flip()

    conv1 = {K_q: 'fire', K_w: 'water', K_e: 'earth', K_r: 'air'}
    conv2 = {K_u: 'fire', K_i: 'water', K_o: 'earth', K_p: 'air'}
    current_attacks = [None, None]
    ready = [False, False]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                # Battle
                elif event.key in (K_q, K_w, K_e, K_r):
                    battlers[0].attack(conv1[event.key])
                    current_attacks[0] = conv1[event.key]
                    if ready[1]:
                        resolve_battle(allsprites, current_attacks)
                        ready = [False, False]
                    else:
                        ready[0] = True
                elif event.key in (K_u, K_i, K_o, K_p):
                    battlers[1].attack(conv2[event.key])
                    current_attacks[1] = conv2[event.key]
                    if ready[0]:
                        resolve_battle(allsprites, current_attacks)
                        ready = [False, False]
                    else:
                        ready[1] = True
                for s in allsprites.sprites():
                    screen.blit(background, (0,0))
                allsprites.draw(screen)
                pygame.display.update()
            else:
                allsprites.update()
