# coding : utf-8

import pygame
import random
from viseur import Viseur
from monstre import Monstre

# créer une classe game
class Game:

    def __init__(self):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        self.arme = Viseur("assets/viseur.png", 0, 0)
        # créer les bloc de timer et score
        self.create_bloc_timer()
        self.create_bloc_score()
        # * set le timer
        self.clock = pygame.time.Clock()
        # * set la limite de bonus
        self.timer = 120000
        # definit les path des monstre
        self.monstre_path = [["assets/mino/mino_1.png", 1], ["assets/mino/mino_2.png", 1], ["assets/mino/mino_3.png", 5], ["assets/mino/mino_4.png", -20]]
        self.all_monstre = []
        # initie le score
        self.score = 0

    def start(self):
        self.is_playing = True
        
    def end(self):
        self.is_playing = False
        
    def create_bloc_timer(self):
        self.bloc_timer = pygame.image.load("assets/timer.png")
        self.bloc_timer = pygame.transform.scale(self.bloc_timer, (400, 100))
        self.bloc_timer_rect = self.bloc_timer.get_rect()
        self.bloc_timer_rect.x = 340
        self.bloc_timer_rect.y = 0
        
    def create_bloc_score(self):
        self.bloc_score = pygame.image.load("assets/panneau.png")
        self.bloc_score = pygame.transform.scale(self.bloc_score, (150, 200))
        self.bloc_score_rect = self.bloc_timer.get_rect()
        self.bloc_score_rect.x = 20
        self.bloc_score_rect.y = 300



    def update(self, screen):
        if self.timer > 0:
            self.timer -= self.clock.tick(60)
            screen.blit(self.bloc_timer, self.bloc_timer_rect)
            screen.blit(self.bloc_score, self.bloc_score_rect)
            self.update_timer(screen)
            self.update_score(screen)
            self.manage_monster(screen)
            screen.blit(self.arme.image, self.arme.rect)
        else:
            self.end()

    def shoot(self, shoot):
        if shoot:
            self.score += self.all_monstre[0].point
            self.all_monstre = []
        else:
            self.score -= 1
        print(self.score)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    
    def update_timer(self, screen):
        font = pygame.font.Font(None, 80)
        format_timer = round(self.timer / 1000)
        if format_timer >= 60:
            seconde = format_timer % 60
            if seconde < 10:
                seconde = f"0{seconde}"
            phrase = f"01 : {seconde}"
        elif format_timer < 60:
            seconde = format_timer % 60
            if seconde < 10:
                seconde = f"0{seconde}"
            phrase = f"00 : {seconde}"
        text = font.render(phrase, 1, (255,255,255))

        # * blit le timer
        screen.blit(text,(450, 15))
        
    def update_score(self, screen):
        font = pygame.font.Font(None, 50)
        score = str(self.score)
        if self.score < 0:
            color = (255,0,0)
        else:
            color = (0,0,0)
        text = font.render(score, 1, color)

        # * blit le score
        screen.blit(text,(70, 335))
        
    def manage_monster(self, screen):
        if len(self.all_monstre) == 0:
            nb_monstre = random.randint(0, 3)
            right = random.randint(1, 2)
            if right == 1:
                right = True
            else:
                right = False
            self.all_monstre.append(Monstre(self.monstre_path[nb_monstre][0], right, random.randint(480, 600), self.monstre_path[nb_monstre][1]))
        for monstre in self.all_monstre:
            monstre.moove()
            if monstre.statut:
                screen.blit(monstre.image, monstre.rect)
                
            if monstre.rect.x < -50:
                self.all_monstre = []
            elif monstre.rect.x > 1230:
                self.all_monstre = []
            
