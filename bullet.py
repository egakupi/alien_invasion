import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Create bullet at 0,0 position and set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
