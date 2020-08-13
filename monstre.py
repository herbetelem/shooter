# coding: utf-8

import pygame

# créer la classe des herbes
class Monstre():

    def __init__(self, path, right, y, point):
        # Load le sprite de l'herbe
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Créer le rect
        self.rect = self.image.get_rect()
        if right:
            self.rect.x = -20
        else:
            self.rect.x = 1180
        self.rect.y = y
        self.speed = 8
        self.statut = True
        self.moove_right = right
        self.point = point

    def moove(self):
        if self.moove_right:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
