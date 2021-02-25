import pygame
import random
from config import *
from pygame import mixer
pygame.init()


class Boat(pygame.sprite.Sprite):
    def __init__(self, location, v):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('boat.png')
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.speed = v

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > 700:
            self.rect.right = 0


class Bug(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('bug.png')
        self.rect = self.image.get_rect()
        self.rect.center = location


class Bug2(pygame.sprite.Sprite):
    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('bug2.png')
        self.rect = self.image.get_rect()
        self.rect.center = location


class hazard(pygame.sprite.Sprite):
    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('obs.png')
        self.rect = self.image.get_rect()
        self.rect.center = location

    def change(self):
        self.rect.x = random.random()*400 + 200


class chim(pygame.sprite.Sprite):
    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('obs2.png')
        self.rect = self.image.get_rect()
        self.rect.center = location

    def change(self):
        self.rect.x = random.random()*500 + 100


def player1_start():
    val = True
    while(val):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            val = False
        text = largeText.render(" PLAYER 1 ", 1, (255, 255, 255))
        statement2 = vsmallText.render(
            " PRESS SPACE TO START ROUND " +
            str(level_1 + level_2), 1, (255, 255, 255))
        win.blit(black, (100, 200))
        win.blit(text, (270, 370))
        win.blit(statement2, (210, 430))
        pygame.display.update()
        clock.tick(15)
    return


def player2_start():
    val = True
    while(val):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            val = False
        text = largeText.render(" PLAYER 2 ", 1, (255, 255, 255))
        statement2 = vsmallText.render(
            " PRESS SPACE TO START ROUND " +
            str(level_2 + level_1), 1, (255, 255, 255))
        win.blit(black, (100, 200))
        win.blit(text, (270, 370))
        win.blit(statement2, (210, 430))
        pygame.display.update()
        clock.tick(15)
    return

# end screen


def end_of_round(score1, score2, l1, l2, w):
    val = True
    while(val):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            val = False
        win.blit(black, (100, 200))
        k = l1 + l2 + 1
        text = largeText.render(" Score-Board", 1, (255, 255, 255))
        scores = vsmallText.render("PLAYER 1 SCORE : " + str(score1) +
                                   "  (LEVEL : " + str(level_1) +
                                   " )", 1, (255, 255, 255))
        scores_2 = vsmallText.render(
            "PLAYER 2 SCORE : " + str(score2) + "  (LEVEL : " +
            str(level_2) + " )", 1, (255, 255, 255))
        statement = vsmallText.render(
            "END OF ROUND " + str(l1 + l2), 1, (255, 255, 255))
        winn = vsmallText.render(
            "PLAYER " + str(w) + " WON THE ROUND", 1, (255, 255, 255))
        statement2 = vsmallText.render(
            " PRESS SPACE TO START ROUND " + str(k), 1, (255, 255, 255))

        win.blit(scores, (220, 360))
        win.blit(scores_2, (220, 390))
        win.blit(text, (250, 270))
        win.blit(winn, (250, 450))
        win.blit(statement, (270, 300))
        win.blit(statement2, (210, 470))
        pygame.display.update()
        clock.tick(15)
    return


player = Bug([x, y])
player2 = Bug2([X, Y])
player_group = pygame.sprite.Group()
boat_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
player_group.add(player)
for i in range(5):
    b.append(Boat([0, loc[i]], v[i]))
    boat_group.add(b[i])
for i in range(4):
    a.append(hazard([random.random()*500 + 100, loc2[i]]))
    boat_group.add(a[i])
    obstacles_group.add(a[i])
for i in range(4):
    h.append(chim([random.random()*500 + 100, loc2[i]]))
    boat_group.add(h[i])
    obstacles_group.add(h[i])

run = True

scoreg = 0
scoreg2 = 0
win.blit(back, (0, 0))
player1_start()
start_time1 = pygame.time.get_ticks()

while run:
    current_time = (pygame.time.get_ticks() - start_time1)//1000
    score = -(current_time)
    score2 = -(current_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    # player 1 controls
    if id == 1:
        if keys[pygame.K_LEFT] and player.rect.x > 0:
            player.rect.x -= vel

        if keys[pygame.K_RIGHT] and player.rect.x < 660:
            player.rect.x += vel

        if keys[pygame.K_UP] and player.rect.y > 0:
            player.rect.y -= vel

        if keys[pygame.K_DOWN] and player.rect.y < 800:
            player.rect.y += vel

    # player 2 controls
    if id == 2:
        if keys[pygame.K_LEFT] and player2.rect.x > 0:
            player2.rect.x -= vel

        if keys[pygame.K_RIGHT] and player2.rect.x < 660:
            player2.rect.x += vel

        if keys[pygame.K_UP] and player2.rect.y > 0:
            player2.rect.y -= vel

        if keys[pygame.K_DOWN] and player2.rect.y < 800:
            player2.rect.y += vel
    
    if keys[pygame.K_ESCAPE] and player2.rect.x > 0:
            run = False
    
    # player 1 score
    for i in range(4):
        if(player.rect.y < h[i].rect.y):
            score = score + 5

    if player.rect.y < 80:
        score = score + 10
    if player.rect.y < 250:
        score = score + 10
    if player.rect.y < 420:
        score = score + 10
    if player.rect.y < 590:
        score = score + 10
    if player.rect.y < 750:
        score = score + 10

    # player2 score
    for i in range(4):
        if(player2.rect.y > h[i].rect.y):
            score2 = score2 + 5
    if player2.rect.y > 80:
        score2 = score2 + 10
    if player2.rect.y > 250:
        score2 = score2 + 10
    if player2.rect.y > 420:
        score2 = score2 + 10
    if player2.rect.y > 590:
        score2 = score2 + 10
    if player2.rect.y > 750:
        score2 = score2 + 10

    # collision code
    if(pygame.sprite.spritecollide(player, boat_group, False) or
            player.rect.y == 0):
        pygame.mixer.music.load('pop.mp3')
        pygame.mixer.music.play(0)
        player2.rect.x = 350
        player2.rect.y = 1
        player_group.remove(player)
        player_group.add(player2)
        player.rect.x = 350
        player.rect.y = 800
        id = 2
        player2_start()
        start_time1 = pygame.time.get_ticks()
        scoreg = score
        for i in range(5):
            b[i].speed += level_2 - level_1

    elif(pygame.sprite.spritecollide(player2, boat_group, False) or
            player2.rect.y == 800):
        pygame.mixer.music.load('pop.mp3')
        pygame.mixer.music.play(0)
        # decide winner for round
        scoreg2 = score2
        if scoreg2 > scoreg:
            winner = 2
        else:
            winner = 1
        player.rect.x = 350
        player.rect.y = 800

        # change controls
        player_group.remove(player2)
        player_group.add(player)
        player2.rect.x = 350
        player2.rect.y = 1
        id = 1

        # change map
        for i in range(4):
            h[i].change()
        for i in range(4):
            a[i].change()

        # change level_1
        for i in range(5):
            b[i].speed -= level_2
        if winner == 1:
            level_1 = level_1 + 1
        else:
            level_2 = level_2 + 1

        for i in range(5):
            b[i].speed += level_1

        # display score board
        end_of_round(scoreg, scoreg2, level_1, level_2, winner)
        player1_start()
        start_time1 = pygame.time.get_ticks()

    time = myfont.render("Time : " + str(current_time) +
                         " secs", 20, (255, 255, 255))

    # blit it all out!
    win.blit(back, (0, 0))
    player_group.update()
    boat_group.update()
    boat_group.draw(win)
    player_group.draw(win)

    # print score and time
    win.blit(time, (590, 10))
    if id == 1:
        scoretext = myfont.render(
            "Previous Score  = " + str(scoreg), 20, (255, 255, 255))
        level = myfont.render("Player 1 is at level " +
                              str(level_1), 20, (255, 255, 255))
        current_scoretext = myfont.render(
            "Score = " + str(score), 20, (255, 255, 255))
        win.blit(scoretext, (5, 10))
        win.blit(level, (400, 10))
        win.blit(current_scoretext, (250, 10))
    if id == 2:
        scoretext2 = myfont.render(
            "Previous Score2  = " + str(scoreg2), 20, (255, 255, 255))
        current_scoretext2 = myfont.render(
            "Score2 = " + str(score2), 20, (255, 255, 255))
        level = myfont.render("Player 2 is at level " +
                              str(level_2), 20, (255, 255, 255))
        win.blit(level, (400, 10))
        win.blit(scoretext2, (5, 10))
        win.blit(current_scoretext2, (250, 10))

    pygame.display.update()
    clock.tick(110)
pygame.quit()
