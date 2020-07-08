from packages.utilities import *


class Battler(pygame.sprite.Sprite):

    def __init__(self, num, image_path, movement, elems, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image_path)
        self.rect.topleft = movement

        self.elems = {element: power for element, power in elems.items()}
        self.hp = hp
        self.num = num
        self.forward = False

    def attack(self, element):
        if not self.forward:
            self.rect = self.rect.move(((-1) ** self.num * 100, 0))
            self.forward = True
        return self.elems[element]

    def retreat(self):
        self.rect = self.rect.move(((-1) ** self.num * -100, 0))
        self.forward = False