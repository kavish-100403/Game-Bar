def flappy_bird():

    import pygame
    import sys
    import random


    def draw_floor():
        screen.blit(floor_surface,(floor_x_pos,550))
        screen.blit(floor_surface,(floor_x_pos + 490,550))

    def create_pipe():
        random_pipe_pos = random.choice(pipe_height)
        bottom_new_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
        top_new_pipe = pipe_surface.get_rect(midbottom = (500,random_pipe_pos - 150))
        return bottom_new_pipe,top_new_pipe

    def move_pipes(pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw_pipes(pipes):
        for pipe in pipes:
            if pipe.bottom >=624:
                screen.blit(pipe_surface,pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface,False,True)
                screen.blit(flip_pipe,pipe)

    def check_collision(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                return False
            

        if bird_rect.top <= -20 or bird_rect.bottom >= 550:
            return False
            
        return True

    def score_display(game_state):
        if game_state == "main_game":
            score_surface = game_font.render(str(int(score)),True,(255,255,255))
            #True is anti alias text so true means it just makes it sharper
            #255,255,255 is the Red Green Blue colour for the score
            score_rect = score_surface.get_rect(center = (250,100))
            screen.blit(score_surface,score_rect)
        if game_state == "game_over":
            score_surface = game_font.render(f'Score: {int(score)}' ,True,(255,255,255))
            #True is anti alias text so true means it just makes it sharper
            #255,255,255 is the Red Green Blue colour for the score
            score_rect = score_surface.get_rect(center = (250,190))
            screen.blit(score_surface,score_rect)

            high_score_surface = game_font.render(f'High Score: {int(high_score)}' ,True,(255,255,255))
            high_score_rect = score_surface.get_rect(center = (250,500))
            screen.blit(high_score_surface,high_score_rect)

    def update_score(score,high_score):
        if score > high_score:
            high_score = score
        return high_score

    pygame.init()
    screen = pygame.display.set_mode((500,624))
    clock = pygame.time.Clock()
    game_font = pygame.font.Font('04B_19.TTF',40)
    #04B_19.TTF is the font type file used in the game

    #Game Variables

    gravity = 0.15     
    bird_movement = 0

    game_active = True
    score = 0
    high_score = 0

    bg_surface = pygame.image.load('pictures/background.png').convert()
    bg_surface = pygame.transform.scale2x(bg_surface)
    floor_surface = pygame.image.load("pictures/base.png").convert()
    floor_surface = pygame.transform.scale2x(floor_surface)

    floor_x_pos = 0
    bird_surface = pygame.image.load("pictures/bird.png").convert()

    bird_rect = bird_surface.get_rect(center = (100,312))

    pipe_surface = pygame.image.load("pictures/pipe.png")
    pipe_surface = pygame.transform.scale2x(pipe_surface)
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE,1200)
    pipe_height = [300,500,550,350,370,400,450,470,250]

    game_over_surface = pygame.transform.scale2x(pygame.image.load("pictures/message.png").convert_alpha())
    game_over_rect = game_over_surface.get_rect(center = (250,312))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 6
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (100,312)
                    bird_movement = 0
                    score = 0
            
            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())
        
        screen.blit(bg_surface,(0,0))

        if game_active:
            #Bird
            bird_movement += gravity
            bird_rect.centery += bird_movement
            screen.blit(bird_surface,bird_rect)
            game_active = check_collision(pipe_list)
            
            #Pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            #score display
            score += 0.01 #This score depends on the time the game is played
            score_display("main_game")
        else:
            screen.blit(game_over_surface,game_over_rect)
            high_score = update_score(score , high_score)
            score_display("game_over")

        #Floor
        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -500:
            floor_x_pos = 0


        


        pygame.display.update()
        clock.tick(120)
