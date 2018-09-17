import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Save coord of ship center
        self.center = float(self.rect.centerx)
        # Moving flag
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """Print ship in current position"""
        self.screen.blit(self.image, self.rect)
