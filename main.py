import pygame
import math


from game import Game
pygame.init()



# generer la fenetre du jeu
pygame.display.set_caption("Hit the minotaure")
screen = pygame.display.set_mode((1080, 720))

# importer et charger le background*
background = pygame.image.load('assets/terre.jpg')
background = pygame.transform.scale(background, (1080, 720))

# importer la bannier
banner = pygame.image.load('assets/banniere.PNG')
banner = pygame.transform.scale(banner, (400, 400))
banner_rect = banner.get_rect()
banner_rect.x = 320
banner_rect.y = 100

# import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = 320
play_button_rect.y = 460

game = Game()

running = True

# boucle tant que running est vrai
while running:

    # appliquer le background
    screen.blit(background, (0,0))

    # verifier si le jeu a commencou ou pas
    if game.is_playing:
        # declencher les instructiond de la partie
        game.update(screen)
    # si le jeu n'est pas lancer
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # update le screen
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # check que l'event est le fait de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu ce ferme")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier que la souris est appyer au bon endroit
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lander
                game.start()
            if game.is_playing:
                for monstre in game.all_monstre:
                    if monstre.rect.collidepoint(event.pos):
                        # mettre le jeu en mode lander
                        game.shoot(True)
                    else:
                        game.shoot(False)
                
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            game.arme.moove(mouse_pos[0], mouse_pos[1])